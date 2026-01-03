from aiogram import Router, F
from aiogram.filters import StateFilter
from aiogram.types import Message, ContentType
from aiogram.fsm.context import FSMContext

# from loguru import logger

from core.keyboards.keyboards import Keyboards
from core.utils.filters import ChatType
from core.utils.states import GetPrice
from core.utils.operations import try_send_files_pack, try_send_to_topic
from core.texts.buttons_texts import ButtonsTexts as bt
from core.texts.messages_texts import Texts
from core.database.database import db
from core.utils.message_manager import MessageManager

from config import conf

r = Router()
r.message.filter(ChatType('private'))


@r.message(F.text.in_(bt.user.get_price.all))
@r.message(F.text.in_(bt.general.again.all), StateFilter(GetPrice.check))
async def get_price(msg: Message, state: FSMContext, kb: Keyboards, texts: Texts, msg_manager: MessageManager):
    to_del = await msg.answer(texts.get_price.start_data, reply_markup=kb.user.start_data())
    await msg_manager.del_all()
    msg_manager.add_to_delete_list(to_del, msg)
    await state.set_state(GetPrice.get_start_data)


@r.message(F.text, StateFilter(GetPrice.get_start_data))
async def get_start_data(msg: Message, state: FSMContext, kb: Keyboards, texts: Texts, msg_manager: MessageManager):
    if msg.content_type != ContentType.TEXT:
        to_del = await msg.answer(texts.errors.not_text, reply_markup=kb.user.start_data())
        await msg_manager.del_all()
        msg_manager.add_to_delete_list(to_del, msg)
        return

    if msg.text not in (
        bt.user.get_price_btns.sample.all +
        bt.user.get_price_btns.model.all +
        bt.user.get_price_btns.draft.all +
        bt.user.get_price_btns.scetch.all +
        bt.user.get_price_btns.photo.all +
        bt.user.get_price_btns.idea.all
    ):
        to_del = await msg.answer(texts.errors.not_in, reply_markup=kb.user.start_data())
        msg_manager.add_to_delete_list(to_del, msg)
        return

    to_del = await msg.answer(texts.get_price.get_start_data, reply_markup=kb.user.upload_files())
    await msg_manager.del_all()
    msg_manager.add_to_delete_list(to_del, msg)
    await state.update_data(start_data=msg.text.lower())
    await state.set_state(GetPrice.get_file)


@r.message(StateFilter(GetPrice.get_file))
async def get_file(msg: Message, state: FSMContext, kb: Keyboards, texts: Texts, msg_manager: MessageManager):
    data = await state.get_data()
    if 'files' not in data:
        data['files'] = []

    if msg.content_type != ContentType.TEXT:
        data['files'].append(msg)
        await state.set_data(data)
        return

    if msg.text in bt.user.get_price_btns.uploaded.all:
        data = await state.get_data()
        if 'files' not in data or len(data['files']) == 0:
            to_del = await msg.answer(texts.errors.no_files, reply_markup=kb.user.upload_files())
            await msg_manager.del_all()
            msg_manager.add_to_delete_list(to_del, msg)
            return

    elif msg.text in bt.user.get_price_btns.without_file.all:
        await state.update_data(files=[])

    else:
        to_del = await msg.answer(texts.errors.not_in, reply_markup=kb.user.upload_files())
        await msg_manager.del_all()
        msg_manager.add_to_delete_list(to_del, msg)
        return

    to_del = await msg.answer(texts.get_price.size, reply_markup=kb.user.to_menu())
    await msg_manager.del_all()
    msg_manager.add_to_delete_list(to_del, msg)
    await state.set_state(GetPrice.get_size)


@r.message(StateFilter(GetPrice.get_size))
async def get_size(msg: Message, state: FSMContext, kb: Keyboards, texts: Texts, msg_manager: MessageManager):
    if msg.content_type != ContentType.TEXT:
        to_del = await msg.answer(texts.errors.not_text, reply_markup=kb.user.to_menu())
        await msg_manager.del_all()
        msg_manager.add_to_delete_list(to_del, msg)
        return

    await state.update_data(size=msg.text)
    to_del = await msg.answer(texts.get_price.usage, reply_markup=kb.user.usage())
    await msg_manager.del_all()
    msg_manager.add_to_delete_list(to_del, msg)
    await state.set_state(GetPrice.get_usage)


@r.message(StateFilter(GetPrice.get_usage))
async def get_usage(msg: Message, state: FSMContext, kb: Keyboards, texts: Texts, msg_manager: MessageManager):
    if msg.content_type != ContentType.TEXT:
        to_del = await msg.answer(texts.errors.not_text, reply_markup=kb.user.usage())
        await msg_manager.del_all()
        msg_manager.add_to_delete_list(to_del, msg)
        return

    if msg.text not in (
        bt.user.get_price_btns.prototype.all +
        bt.user.get_price_btns.functional.all +
        bt.user.get_price_btns.decor.all
    ):
        to_del = await msg.answer(texts.errors.not_in, reply_markup=kb.user.usage())
        await msg_manager.del_all()
        msg_manager.add_to_delete_list(to_del, msg)
        return

    to_del = await msg.answer(texts.get_price.temperature, reply_markup=kb.user.temperature())
    await msg_manager.del_all()
    msg_manager.add_to_delete_list(to_del, msg)
    await state.update_data(usage=msg.text.lower())
    await state.set_state(GetPrice.get_temperature)


@r.message(StateFilter(GetPrice.get_temperature))
async def get_temperature(msg: Message, state: FSMContext, kb: Keyboards, texts: Texts, msg_manager: MessageManager):
    if msg.content_type != ContentType.TEXT:
        to_del = await msg.answer(texts.errors.not_text, reply_markup=kb.user.temperature())
        await msg_manager.del_all()
        msg_manager.add_to_delete_list(to_del, msg)
        return

    if msg.text not in (
        bt.user.get_price_btns.under_40.all +
        bt.user.get_price_btns.under_90.all +
        bt.user.get_price_btns.under_120.all +
        bt.user.get_price_btns.more_than_120.all
    ):
        to_del = await msg.answer(texts.errors.not_in, reply_markup=kb.user.temperature())
        await msg_manager.del_all()
        msg_manager.add_to_delete_list(to_del, msg)
        return

    to_del = await msg.answer(texts.get_price.environment, reply_markup=kb.user.environment())
    await msg_manager.del_all()
    msg_manager.add_to_delete_list(to_del, msg)
    await state.update_data(temperature=msg.text.lower())
    await state.set_state(GetPrice.get_environment)


@r.message(StateFilter(GetPrice.get_environment))
async def get_environment(msg: Message, state: FSMContext, kb: Keyboards, texts: Texts, msg_manager: MessageManager):
    if msg.content_type != ContentType.TEXT:
        to_del = await msg.answer(texts.errors.not_text, reply_markup=kb.user.environment())
        await msg_manager.del_all()
        msg_manager.add_to_delete_list(to_del, msg)
        return

    if msg.text not in (
        bt.user.get_price_btns.air.all +
        bt.user.get_price_btns.water.all +
        bt.user.get_price_btns.oil.all +
        bt.user.get_price_btns.other.all
    ):
        to_del = await msg.answer(texts.errors.not_in, reply_markup=kb.user.environment())
        await msg_manager.del_all()
        msg_manager.add_to_delete_list(to_del, msg)
        return

    to_del = await msg.answer(texts.get_price.color, reply_markup=kb.user.color())
    await msg_manager.del_all()
    msg_manager.add_to_delete_list(to_del, msg)
    await state.update_data(environment=msg.text.lower())
    await state.set_state(GetPrice.get_color)


@r.message(StateFilter(GetPrice.get_color))
async def get_color(msg: Message, state: FSMContext, kb: Keyboards, texts: Texts, msg_manager: MessageManager):
    if msg.content_type != ContentType.TEXT:
        to_del = await msg.answer(texts.errors.not_text, reply_markup=kb.user.color())
        await msg_manager.del_all()
        msg_manager.add_to_delete_list(to_del, msg)
        return

    if msg.text not in (
        bt.user.get_price_btns.any_color.all +
        bt.user.get_price_btns.black.all +
        bt.user.get_price_btns.white.all +
        bt.user.get_price_btns.colorized.all
    ):
        to_del = await msg.answer(texts.errors.not_in, reply_markup=kb.user.color())
        await msg_manager.del_all()
        msg_manager.add_to_delete_list(to_del, msg)
        return

    to_del = await msg.answer(texts.get_price.count, reply_markup=kb.user.to_menu())
    await msg_manager.del_all()
    msg_manager.add_to_delete_list(to_del, msg)
    await state.update_data(color=msg.text.lower())
    await state.set_state(GetPrice.get_count)


@r.message(StateFilter(GetPrice.get_count))
async def get_count(msg: Message, state: FSMContext, kb: Keyboards, texts: Texts, msg_manager: MessageManager):
    if msg.content_type != ContentType.TEXT:
        to_del = await msg.answer(texts.errors.not_text)
        await msg_manager.del_all()
        msg_manager.add_to_delete_list(to_del, msg)
        return

    await state.update_data(count=msg.text.lower())
    to_del = await msg.answer(
        texts.get_price.comment,
        reply_markup=kb.general.reply_markup_from_buttons(kb.btn.user.get_price_btns.without_comm)
    )
    await msg_manager.del_all()
    msg_manager.add_to_delete_list(to_del, msg)
    await state.set_state(GetPrice.get_comment)


@r.message(StateFilter(GetPrice.get_comment))
async def get_comment(msg: Message, state: FSMContext, kb: Keyboards, texts: Texts, msg_manager: MessageManager):
    await state.update_data(comment=msg.html_text)
    data = await state.get_data()
    to_del = await msg.answer(
        texts.get_price.check_correct + texts.get_price.generated_text.format(**data),
        reply_markup=kb.general.check()
    )
    await msg_manager.del_all()
    msg_manager.add_to_delete_list(to_del, msg)
    await state.set_state(GetPrice.check)


@r.message(F.text.in_(bt.general.correct.all), StateFilter(GetPrice.check))
async def all_correct(msg: Message, state: FSMContext, kb: Keyboards, texts: Texts, msg_manager: MessageManager):

    data = await state.get_data()
    text = texts.get_price.generated_text.format(**data)
    user = db.get_user(msg.from_user.id)
    topic_id = user.topic_id

    await try_send_to_topic(msg.from_user, text, topic_id)
    if len(data['files']) > 0:
        await try_send_files_pack(data['files'], conf.get_support_chat_id(), topic_id)

    to_del = await msg.answer(
        texts.get_price.info_sended,
        reply_markup=kb.user.menu()
    )
    await msg_manager.del_all()
    msg_manager.add_to_delete_list(to_del, msg)
    await state.set_state(None)
    await state.set_data({})
