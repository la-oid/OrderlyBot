import asyncio
from datetime import datetime, timedelta

import os

from aiogram.types import Message, InlineKeyboardButton
from art import tprint
from loguru import logger

from core.utils.midlewares import UpdateLogger, MessageChecker, SetLanguage, IdentificateUser
from core.utils.operations import set_loggers, try_send_message, try_send_photo
from core.utils.google_sheets import gt
from core.texts.buttons_texts import ButtonsTexts as bt
from core.texts.messages_texts import Texts
from core.keyboards.keyboards import Keyboards
from core.database.database import db
from core.utils.models import ServerOrderStatusesRow
from core.database.orders import OrdersTable
from core.database.users import UsersTable
from core.utils.google_drive import gd

from helper import bot, dp, scheduler
from config import conf


async def on_startup():
    scheduler.add_job(update_orders, "interval", minutes=5)
    bot_info = await bot.get_me()
    await bot.delete_webhook()
    tprint(f'@{bot_info.username}    online')
    scheduler.start()
    logger.warning(f'bot info: @{bot_info.username} {bot_info.first_name} {bot_info.id}')


async def update_orders():
    orders = gt.get_server_orders()
    for order in orders:
        db_order = db.get_order(order.id)

        if db_order is None: continue
        if db_order.user_id is None: continue
        user = db.get_user(db_order.user_id)
        if order.status == 'к отгрузке' and not db_order.sended: await order_ready(db_order, order, user)

        condition = (
            ((datetime.now() - db_order.last_update_date) >= timedelta(5)) and
            (db_order.rate is None) and
            (order.status == 'закрыт')
        )
        if condition and not db_order.mark_asked: await rate_us(db_order)


async def rate_us(order: OrdersTable.Orders):
    logger.info(f'Просьба оценить заказ {order}')

    user = db.get_user(order.user_id)
    if user: lang = user.lang
    else: lang = 'ru'
    kb = Keyboards(lang)
    texts = Texts(lang)
    text = texts.misc.ask_rate.format(order_id=order.order_id)
    error = await try_send_message(
        chat_id=order.user_id,
        text=text,
        reply_markup=kb.general.inline_markup_from_buttons(
            InlineKeyboardButton(
                text=bt.user.rate[lang],
                callback_data=f'rate_{order.order_id}'
            )
        )
    )
    topic_notification = None
    if user:
        if isinstance(error, str): text = f'Не отправлено пользователю {text} по причине:\n\n{error}'
        else: text = 'Отправлено пользователю:\n\n' + text
        topic_notification = await try_send_message(
            chat_id=conf.get_support_chat_id(),
            topic_id=user.topic_id,
            text=text,
        )
    if isinstance(error, str):
        if isinstance(topic_notification, Message):
            await try_(
                chat_id=conf.get_admin_id(),
                text=(
                    f'Не удалось спросить оценку у пользователя {order.user_id} о заказе {order.order_id} '
                    f'по причине:\n {error}\n\nПользователь отвязан'
                ),
            )
            db.edit_order_user_id(order.order_id, None)
            if user:
                db.edit_user_banned(user.id)
    else:
        db.edit_order_rate_asked(order.order_id)


async def order_ready(order: OrdersTable.Orders, server_order: ServerOrderStatusesRow, user: UsersTable.Users):
    logger.info(f'Отправка уведомления о заказе {order}')

    if user: lang = user.lang
    else: lang = 'ru'

    texts = Texts(lang)
    text = texts.misc.order_ready.format(order_id=order.order_id) + '\n'

    if server_order.price: text += texts.misc.order_price.format(price=server_order.price) + '\n'
    if server_order.to_pay: text += texts.misc.order_to_pay.format(to_pay=server_order.to_pay)

    files = gd.find_photo_id(order.order_id)
    if files is None or len(files) == 0:
        error = await try_send_message(
            chat_id=order.user_id,
            text=text
        )
        await try_send_message(
            chat_id=conf.get_support_chat_id(),
            topic_id=user.topic_id,
            text=(
                f'Ошибка при поиске фотографии для заказа {order.order_id}, '
                'убедитесь, что фотография в наличии и имеет правильное расширение'
            )
        )
    else:
        gd.download_file(files['id'], files['name'])
        error = await try_send_photo(
            user.id,
            'core/source/drive_photos/' + files['name'],
            caption=text
        )
        if isinstance(error, str):
            error = await try_send_photo(
                chat_id=conf.get_support_chat_id(),
                photo_path='core/source/drive_photos/' + files['name'],
                topic_id=user.topic_id,
                caption=text
            )
            await try_send_message(
                chat_id=conf.get_support_chat_id(),
                topic_id=user.topic_id,
                text=f'Пользователь не получил фото по заказу {order.order_id} по причине {error}, отправлен текст'
            )
            if isinstance(error, str):
                await try_send_message(
                    chat_id=conf.get_support_chat_id(),
                    topic_id=user.topic_id,
                    text=f'Не удалось оповестить пользователя о готовности заказа {order.order_id} по причине {error}'
                )
        else:
            await try_send_message(
                chat_id=conf.get_support_chat_id(),
                topic_id=user.topic_id,
                text=f'Пользователю отправлена фотография по заказу {order.order_id}'
            )
            error = await try_send_photo(
                chat_id=conf.get_support_chat_id(),
                photo_path='core/source/drive_photos/' + files['name'],
                topic_id=user.topic_id,
                caption=text
            )
        os.remove('core/source/drive_photos/' + files['name'])
        if isinstance(error, str):
            await try_send_message(
                chat_id=conf.get_support_chat_id(),
                topic_id=user.topic_id,
                text=(
                    f'Ошибка при отправке фотографии для заказа {order.order_id}, текст ошибки:\n{error}'
                )
            )

    user = db.get_user(order.user_id)
    topic_notification = None
    if user:
        if isinstance(error, str): text = f'Не отправлено пользователю {text} по причине:\n\n{error}'
        else: text = 'Отправлено пользователю:\n\n' + text
        topic_notification = await try_send_message(
            chat_id=conf.get_support_chat_id(),
            topic_id=user.topic_id,
            text=text
        )
    if isinstance(error, str):
        if isinstance(topic_notification, Message):
            await try_send_message(
                chat_id=conf.get_admin_id(),
                text=(
                    f'Не удалось оповестить пользователя {order.user_id} о том, что заказ {order.order_id} готов '
                    f'по причине:\n {error}\n\nПользователь отвязан'
                ),
            )
            db.edit_order_user_id(order.order_id, None)
            if user:
                db.edit_user_banned(user.id)
    else:
        db.edit_order_sended(order.order_id)


def include_admin_routers():
    from core.handlers.admin import (
        misc,
        great_func
    )
    dp.include_routers(
        misc.r,
        great_func.r,
    )


# Обработчик ниже должен идти самым последним, поскольку содержит обработчик без фильтров, на случай,
# если пользователь пишет менеджеру, а режим не активирован
def include_user_routers():
    from core.handlers.user import (
        company_info,
        get_price,
        menu,
        misc,
        manager_chating
    )
    dp.include_routers(
        misc.r,
        menu.r,
        company_info.r,
        get_price.r,
        # Обработчик ниже должен идти самым последним, поскольку содержит обработчик без фильтров, на случай,
        # если пользователь пишет менеджеру, а режим не активирован
        manager_chating.r,
    )


def main():
    set_loggers()
    include_admin_routers()
    # Обработчик ниже должен идти самым последним, поскольку содержит обработчик без фильтров, на случай,
    # если пользователь пишет менеджеру, а режим не активирован
    include_user_routers()

    dp.update.middleware(UpdateLogger())
    dp.update.middleware(IdentificateUser())
    dp.update.middleware(SetLanguage())
    dp.message.middleware(MessageChecker())

    dp.startup.register(on_startup)
    asyncio.run(dp.start_polling(bot))


if __name__ == "__main__":
    main()
