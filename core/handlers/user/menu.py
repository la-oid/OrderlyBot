from aiogram import Router, F
from aiogram.filters import Command, StateFilter
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from core.utils.filters import ChatType
from core.utils.states import Other
from core.utils.operations import try_delete
from core.utils.google_sheets import gt
from core.texts.messages_texts import Texts
from core.texts.buttons_texts import ButtonsTexts as bt
from core.keyboards.keyboards import Keyboards
from core.database.database import db
from core.utils.message_manager import MessageManager
from core.utils.operations import active_topic, create_topic

from config import conf

r = Router()
r.message.filter(ChatType('private'))


@r.message(F.text.in_(bt.user.menu.all), StateFilter('*'))
@r.message(F.text, Command('start'), StateFilter('*'))
async def start(msg: Message, state: FSMContext, texts: Texts, kb: Keyboards, msg_manager: MessageManager):
    if msg.text == '/start':
        text = texts.menu.start
    else:
        text = texts.menu.to_menu

    await state.set_state(None)
    to_del = await msg.answer(
        text=text,
        reply_markup=kb.user.menu()
    )
    await msg_manager.del_all()
    msg_manager.add_to_delete_list(to_del, msg)

    user = db.get_user(msg.from_user.id)
    if not await active_topic(user.topic_id):
        await create_topic(msg.from_user)


@r.message(F.text.in_(bt.user.order_status.all))
async def order_status(msg: Message, state: FSMContext, texts: Texts, kb: Keyboards, msg_manager: MessageManager):
    to_del = await msg.answer(texts.menu.order_status, reply_markup=kb.user.to_menu())
    await msg_manager.del_all()
    msg_manager.add_to_delete_list(to_del, msg)
    await state.set_state(Other.get_order_id)


@r.message(F.text, StateFilter(Other.get_order_id))
async def get_order_id(msg: Message, state: FSMContext, texts: Texts, kb: Keyboards, msg_manager: MessageManager):
    order_id = msg.text.lower()
    order = gt.get_user_order(order_id)
    db_order = db.get_order(order_id)

    if order is None or db_order is None:
        to_del = await msg.answer(texts.errors.unknown_order, reply_markup=kb.user.to_menu())
        await msg_manager.del_all()
        msg_manager.add_to_delete_list(to_del, msg)
        return

    if db_order.user_id is None:
        to_del = await msg.answer(texts.errors.unknown_order, reply_markup=kb.user.to_menu())
        await msg_manager.del_all()
        msg_manager.add_to_delete_list(to_del, msg)
        return

    to_del = await msg.answer(texts.menu.processing)
    user_order = gt.get_user_order(order_id)

    await try_delete(to_del)
    to_del = await msg.answer(
        f'{texts.menu.order} {order.id} {conf.status_asociate()[user_order.status][texts.lang]}',
        reply_markup=kb.user.menu()
    )
    await msg_manager.del_all()
    msg_manager.add_to_delete_list(to_del, msg)
    await state.set_state(None)
