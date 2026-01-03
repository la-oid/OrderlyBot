from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, KeyboardButton
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext

from core.utils.filters import ChatType
from core.texts.messages_texts import Texts
from core.texts.buttons_texts import ButtonsTexts as bt
from core.utils.states import Other
from core.utils.operations import is_int, try_delete, try_send_message, active_topic, create_topic
from core.database.database import db
from core.keyboards.keyboards import Keyboards
from core.utils.message_manager import MessageManager

from config import conf

r = Router()
r.message.filter(ChatType('private'))


@r.callback_query(F.data.startswith('rate_'), StateFilter('*'))
async def rate(call: CallbackQuery, state: FSMContext, kb: Keyboards, texts: Texts, msg_manager: MessageManager):
    order_id = int(call.data.split('_')[1])
    order = db.get_order(order_id)

    if order is None:
        to_del = await call.message.answer(
            texts.errors.unknown_order_for_user,
            reply_markup=kb.user.menu()
        )
        await msg_manager.del_all()
        msg_manager.add_to_delete_list(to_del)
    else:
        await state.update_data(order_id=order_id)
        to_del = await call.message.answer(texts.misc.rate_rank.format(order_id=order_id))
        await msg_manager.del_all()
        msg_manager.add_to_delete_list(to_del)
        await state.set_state(Other.rate)

    await try_delete(call.message)


@r.message(F.text, StateFilter(Other.rate))
async def get_rate(msg: Message, state: FSMContext, texts: Texts, kb: Keyboards, msg_manager: MessageManager):
    if not is_int(msg.text):
        to_del = await msg.answer(texts.errors.not_int)
        await msg_manager.del_all()
        msg_manager.add_to_delete_list(to_del, msg)
        return

    if int(msg.text) not in range(1, 11):
        to_del = await msg.answer(texts.errors.rate_not_in_range)
        await msg_manager.del_all()
        msg_manager.add_to_delete_list(to_del, msg)
        return

    data = await state.get_data()
    db.edit_order_rate(data['order_id'], int(msg.text))
    to_del = await msg.answer(texts.misc.thx_for_rate, reply_markup=kb.user.menu())
    await msg_manager.del_all()
    msg_manager.add_to_delete_list(to_del, msg)

    user = db.get_user(msg.from_user.id)
    if not await active_topic(user.topic_id):
        await create_topic(msg.from_user)
        user = db.get_user(msg.from_user.id)

    await try_send_message(
        conf.get_support_chat_id(),
        f'Пользователь оценил заказ {data["order_id"]} на {msg.text} из 10',
        user.topic_id
    )
    await state.set_state(None)
    await state.set_data({})


@r.message(F.text.in_(bt.user.language.all))
async def language(msg: Message, state: FSMContext, texts: Texts, kb: Keyboards, msg_manager: MessageManager):
    markup = kb.general.reply_markup_from_buttons(
        *[KeyboardButton(text=i) for i in conf.get_langs().values()],
        kb.btn.user.menu
    )
    to_del = await msg.answer(
        texts.misc.choose_language,
        reply_markup=markup
    )
    await msg_manager.del_all()
    msg_manager.add_to_delete_list(to_del, msg)
    await state.set_state(Other.get_language)


@r.message(F.text, StateFilter(Other.get_language))
async def get_language(msg: Message, state: FSMContext, texts: Texts, kb: Keyboards, msg_manager: MessageManager):
    lang = None
    for key, value in conf.get_langs().items():
        if value == msg.text:
            lang = key
            break
    else:
        markup = kb.general.reply_markup_from_buttons(
            *[KeyboardButton(text=i) for i in conf.get_langs().values()],
            kb.btn.user.menu
        )
        to_del = await msg.answer(texts.errors.not_in, reply_markup=markup)
        await msg_manager.del_all()
        msg_manager.add_to_delete_list(to_del, msg)
        return

    db.edit_user_language(msg.from_user.id, lang)
    texts = Texts(lang)
    kb = Keyboards(lang)
    user = db.get_user(msg.from_user.id)
    if not await active_topic(user.topic_id):
        await create_topic(msg.from_user)
        user = db.get_user(msg.from_user.id)

    await try_send_message(
        conf.get_support_chat_id(),
        f'Пользователь изменил язык на {lang}',
        user.topic_id
    )
    to_del = await msg.answer(texts.misc.lang_edited, reply_markup=kb.user.menu())
    await msg_manager.del_all()
    msg_manager.add_to_delete_list(to_del, msg)
    await state.set_state(None)


@r.message(F.text, StateFilter(Other.init_user))
async def init_user(msg: Message, state: FSMContext, msg_manager: MessageManager):
    lang = None
    for key, value in conf.get_langs().items():
        if value == msg.text:
            lang = key
            break
    else:
        kb = Keyboards()
        to_del = await msg.answer(
            f"Xato, noma'lum til ({msg.text}), tavsiya etilgan variantlardan birini tanlang.\n\nОшибка, неизвестный язык({msg.text}), выберите один из предложенных вариантов.",
            reply_markup=kb.general.reply_markup_from_buttons(
                *[KeyboardButton(text=i) for i in conf.get_langs().values()]
            )
        )
        await msg_manager.del_all()
        msg_manager.add_to_delete_list(to_del, msg)
        return

    user = msg.from_user
    db.add_user(
        user.id,
        user.first_name,
        user.last_name,
        user.username,
        None,
        lang,
    )
    await create_topic(user)

    texts = Texts(lang)
    kb = Keyboards(lang)
    await state.set_state(None)
    to_del = await msg.answer(
        text=texts.menu.start,
        reply_markup=kb.user.menu()
    )
    await msg_manager.del_all()
    msg_manager.add_to_delete_list(to_del, msg)
