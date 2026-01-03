from typing import List

from aiogram import Router, F
from aiogram.filters import StateFilter
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from aiogram_media_group import media_group_handler

from core.utils.filters import ChatType
from core.utils.operations import try_send_files_pack, try_copy
from core.database.database import db
from core.keyboards.keyboards import Keyboards
from core.texts.messages_texts import Texts
from core.texts.buttons_texts import ButtonsTexts as bt
from core.utils.message_manager import MessageManager

from config import conf

r = Router()
r.message.filter(ChatType('private'))


@r.message(F.text.in_(bt.user.write_to_manager.all), StateFilter('*'))
async def write_to_manager(msg: Message, kb: Keyboards, texts: Texts, msg_manager: MessageManager, state: FSMContext):
    to_del = await msg.answer(
        texts.menu.write_to_manager,
        reply_markup=kb.user.menu()
    )
    await msg_manager.del_all()
    msg_manager.add_to_delete_list(to_del, msg)
    await state.set_state(None)


@r.message(F.media_group_id, StateFilter('*'))
@media_group_handler
async def media_group(msgs: List[Message]):
    user = db.get_user(msgs[0].from_user.id)
    await try_send_files_pack(
        files=msgs,
        chat_id=conf.get_support_chat_id(),
        thread_id=user.topic_id,
    )


@r.message(StateFilter('*'))
async def copy(msg: Message):
    user = db.get_user(msg.from_user.id)
    await try_copy(
        msg,
        conf.get_support_chat_id(),
        user.topic_id
    )
