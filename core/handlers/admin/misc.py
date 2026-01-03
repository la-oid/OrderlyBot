from typing import List

from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, ContentType
from aiogram.filters import Command

from aiogram_media_group import media_group_handler

from core.database.database import db
from core.utils.google_sheets import gt
from core.utils.filters import ChatsIds
from core.utils.operations import try_send_files_pack, try_send_message, try_delete, try_copy
from core.texts.messages_texts import Texts

from config import conf

r = Router()
r.message.filter(
    ChatsIds(conf.get_support_chat_id())
)


@r.message(F.text, Command('help'))
async def help(msg: Message):
    await msg.reply(
        'Список команд:\n\n'
        '/info - информация о заказах пользователя\n'
        '/set_id <id заказа> - начать отслеживание заказа, скобки писать не нужно\n'
        '/unset_id <id заказа> - перестать отслеживать заказ, скобки писать не нужно\n'
    )


@r.message(F.text, Command('info'))
async def info(msg: Message):
    user = db.get_user_by_topic_id(msg.message_thread_id)
    orders = db.get_user_orders(user.id)
    rates = []

    for order in orders:
        if order.rate:
            rates.append(order.rate)

    middle_mark = 0
    for rate in rates: middle_mark += rate
    if len(orders) > 0:
        middle_mark = round(middle_mark / len(orders), 1)
        last_order = f'#{orders[0].order_id}'
    else:
        middle_mark = 0
        last_order = 'не имеется'

    await msg.reply(
        user.readable_info() + '\n\n'
        f'Всего заказал: {len(orders)}\n'
        f'Последний заказ: {last_order}\n'
        f'Средняя оценка за все время: {middle_mark}'
    )


@r.message(F.text, Command('set_id'))
async def set_id(msg: Message):

    params = msg.text.split()
    if len(params) != 2:
        await msg.reply(
            'Неверное количество параметров, команда должна содержать параметр(id заказа без пробелов)\n'
            'Пример: /set_id 1235123'
        )
        return

    server_order = gt.get_server_order(params[1])
    user_order = gt.get_user_order(params[1])
    if not server_order:
        await msg.reply(
            'Не могу найти такой заказ, проверьте правильность запроса или наличие заказа в '
            '<a href="https://docs.google.com/spreadsheets/d/1sjCkNySGA5_oKC2YtnZbF4D0Qrl_mc3ExWftLHPal2c/edit?gid=0#gid=0">'
            'таблице с заказами</a>',
            parse_mode='html'
        )
        return

    if not user_order:
        await msg.reply(
            'Не могу найти такой заказ, проверьте правильность запроса или наличие заказа в '
            '<a href="https://docs.google.com/spreadsheets/d/1VRyB8EgNHG3BBTHyOsVLf2rRhjtHpRDDb5dVtU1c_ok/edit">'
            'таблице с заказами</a>',
            parse_mode='html'
        )
        return

    user = db.get_user_by_topic_id(msg.message_thread_id)
    if not user:
        await msg.reply('Не могу найти этот топик в моей бд, возможно она была удалена. Рекомендуется удалить этот топик')
        return

    user_id = user.id
    db_order = db.get_order(server_order.id)
    if db_order:
        if db_order.user_id:
            await msg.reply(
                f'Заказ #{db_order.order_id} уже привязан к пользователю {db_order.user_id}!'
            )
            return
        else:
            db.edit_order_user_id(server_order.id, user_id)
    else:
        db.add_order(
            server_order.id,
            user_id,
        )

    db_order = db.get_order(server_order.id)
    texts = Texts(user.lang)

    text = texts.misc.order_number.format(order_id=db_order.order_id) + '\n'
    if server_order.price: text += texts.misc.order_price.format(price=server_order.price) + '\n'
    if server_order.payed: payed = server_order.payed
    else: payed = 0

    text += texts.misc.order_payed.format(payed=payed) + '\n'
    text += texts.misc.order_end_date.format(end_date=user_order.end_date)

    await msg.reply('Отправлено пользователю:\n\n' + text)
    result = await try_send_message(db_order.user_id, text)
    if isinstance(result, str):
        await msg.reply(result)


@r.message(F.text, Command('unset_id'))
async def unset_id(msg: Message):

    params = msg.text.split()
    if len(params) != 2:
        await msg.reply(
            'Неверное количество параметров, команда должна содержать параметр(id заказа без пробелов)\n'
            'Пример: /unset_id 1235123'
        )
        return

    order = db.get_order(params[1])
    if not order:
        await msg.reply(
            f'Заказ #{params[1]} еще ни к кому не привязан'
        )
        return
    elif order.user_id is None:
        await msg.reply(
            f'Заказ #{params[1]} еще ни к кому не привязан'
        )
        return

    db.edit_order_user_id(order.order_id, None)
    await msg.reply(f'Заказ #{order.order_id} отвязан!')


@r.message(F.text)
async def answer_ticket_text(msg: Message):
    user = db.get_user_by_topic_id(msg.message_thread_id)
    if not user:
        await msg.reply('Не могу найти этот топик в моей бд, возможно она была удалена. Рекомендуется удалить этот топик')
        return

    user_id = user.id
    result = await try_send_message(
        chat_id=user_id,
        text=f'<b>{msg.from_user.first_name}:</b> ' + msg.html_text,
        parse_mode='html'
    )
    if isinstance(result, str):
        await msg.answer(f'Сообщение не было отправлено по причине {result}')
    elif user.banned_bot:
        db.edit_user_banned(user_id, False)


@r.message(F.media_group_id)
@media_group_handler
async def media_group(msgs: List[Message]):
    user = db.get_user_by_topic_id(msgs[0].message_thread_id)
    if not user:
        await msgs[0].answer('Не могу найти этот топик в моей бд, возможно она была удалена. Рекомендуется удалить этот топик')
        return

    user_id = user.id
    await try_send_files_pack(
        files=msgs,
        chat_id=user_id
    )


@r.message()
async def answer_ticket(msg: Message):
    if msg.content_type == ContentType.FORUM_TOPIC_CREATED:
        return

    user = db.get_user_by_topic_id(msg.message_thread_id)
    if not user:
        await msg.reply('Не могу найти этот топик в моей бд, возможно она была удалена. Рекомендуется удалить этот топик')
        return

    user_id = user.id
    result = await try_copy(
        msg,
        user_id
    )
    if result:
        await msg.answer(f'Сообщение не было отправлено по причине {result}')


@r.callback_query(F.data.startswith('untrack_'))
async def untrack_callback(call: CallbackQuery):
    order_id = call.data.split('_')[1]
    order = db.get_order(order_id)
    if not order:
        await call.answer(
            f'Странно... Не могу найти заказ {order_id} в бд, похоже он больше не отслеживается',
            show_alert=True
        )
        await try_delete(call.message)
        return

    db.edit_order_user_id(order_id, None)
    await call.answer(f'Заказ больше {order_id} не отслеживается')
    await try_delete(call.message)
