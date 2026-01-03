from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext

from core.keyboards.keyboards import Keyboards
from core.texts.messages_texts import Texts
from core.texts.buttons_texts import ButtonsTexts as bt
from core.utils.filters import ChatType
from core.utils.states import CompanyInfo
from core.utils.operations import photos_on_dir_list, send_photos
from core.utils.message_manager import MessageManager
from config import conf

r = Router()
r.message.filter(ChatType('private'))


@r.message(F.text.in_(bt.user.company_info.all), StateFilter(None))
@r.message(F.text.in_(bt.general.back.all), StateFilter(CompanyInfo.info))
async def company_info(msg: Message, state: FSMContext, kb: Keyboards, texts: Texts, msg_manager: MessageManager):
    to_del = await msg.answer(
        texts.company_info.company_info,
        reply_markup=kb.user.company_info()
    )
    await msg_manager.del_all()
    msg_manager.add_to_delete_list(to_del, msg)
    await state.set_state(CompanyInfo.info)


@r.message(F.text.in_(bt.user.get_company_info_btns.our_services.all), StateFilter(CompanyInfo.info))
async def our_services(msg: Message, kb: Keyboards, texts: Texts, msg_manager: MessageManager):
    to_del = await msg.answer(
        texts.company_info.our_services,
        reply_markup=kb.user.our_servces()
    )
    await msg_manager.del_all()
    msg_manager.add_to_delete_list(to_del, msg)


@r.message(F.text.in_(bt.user.get_company_info_btns.print_3d.all), StateFilter(CompanyInfo.info))
async def print_3d(msg: Message, kb: Keyboards, texts: Texts, msg_manager: MessageManager):
    to_del = await msg.answer(
        texts.company_info.print_3d,
        reply_markup=kb.user.our_servces()
    )
    await msg_manager.del_all()
    msg_manager.add_to_delete_list(to_del, msg)


@r.message(F.text.in_(bt.user.get_company_info_btns.casting.all), StateFilter(CompanyInfo.info))
async def casting(msg: Message, kb: Keyboards, texts: Texts, msg_manager: MessageManager):
    to_del = await msg.answer(
        texts.company_info.casting,
        reply_markup=kb.user.our_servces()
    )
    await msg_manager.del_all()
    msg_manager.add_to_delete_list(to_del, msg)


@r.message(F.text.in_(bt.user.get_company_info_btns.maketing.all), StateFilter(CompanyInfo.info))
async def maketing(msg: Message, kb: Keyboards, texts: Texts, msg_manager: MessageManager):
    to_del = await msg.answer(
        texts.company_info.maketing,
        reply_markup=kb.user.our_servces()
    )
    await msg_manager.del_all()
    msg_manager.add_to_delete_list(to_del, msg)


@r.message(F.text.in_(bt.user.get_company_info_btns.modeling_3d.all), StateFilter(CompanyInfo.info))
async def modeling_3d(msg: Message, kb: Keyboards, texts: Texts, msg_manager: MessageManager):
    to_del = await msg.answer(
        texts.company_info.modeling_3d,
        reply_markup=kb.user.our_servces()
    )
    await msg_manager.del_all()
    msg_manager.add_to_delete_list(to_del, msg)


@r.message(F.text.in_(bt.user.get_company_info_btns.skaning_3d.all), StateFilter(CompanyInfo.info))
async def skaning_3d(msg: Message, kb: Keyboards, texts: Texts, msg_manager: MessageManager):
    to_del = await msg.answer(
        texts.company_info.skaning_3d,
        reply_markup=kb.user.our_servces()
    )
    await msg_manager.del_all()
    msg_manager.add_to_delete_list(to_del, msg)


@r.message(F.text.in_(bt.user.get_company_info_btns.revers_engeneering.all), StateFilter(CompanyInfo.info))
async def revers_engeneering(msg: Message, kb: Keyboards, texts: Texts, msg_manager: MessageManager):
    to_del = await msg.answer(
        texts.company_info.revers_engeneering,
        reply_markup=kb.user.our_servces()
    )
    await msg_manager.del_all()
    msg_manager.add_to_delete_list(to_del, msg)


@r.message(F.text.in_(bt.user.get_company_info_btns.geometry_control.all), StateFilter(CompanyInfo.info))
async def geometry_control(msg: Message, kb: Keyboards, texts: Texts, msg_manager: MessageManager):
    to_del = await msg.answer(
        texts.company_info.geometry_control,
        reply_markup=kb.user.our_servces()
    )
    await msg_manager.del_all()
    msg_manager.add_to_delete_list(to_del, msg)


@r.message(F.text.in_(bt.user.get_company_info_btns.silicone_forms.all), StateFilter(CompanyInfo.info))
async def silicone_forms(msg: Message, kb: Keyboards, texts: Texts, msg_manager: MessageManager):
    to_del = await msg.answer(
        texts.company_info.silicone_forms,
        reply_markup=kb.user.our_servces()
    )
    await msg_manager.del_all()
    msg_manager.add_to_delete_list(to_del, msg)


@r.message(F.text.in_(bt.user.get_company_info_btns.prototiping.all), StateFilter(CompanyInfo.info))
async def prototiping(msg: Message, kb: Keyboards, texts: Texts, msg_manager: MessageManager):
    to_del = await msg.answer(
        texts.company_info.prototiping,
        reply_markup=kb.user.our_servces()
    )
    await msg_manager.del_all()
    msg_manager.add_to_delete_list(to_del, msg)


@r.message(F.text.in_(bt.user.get_company_info_btns.serial_production.all), StateFilter(CompanyInfo.info))
async def serial_production(msg: Message, kb: Keyboards, texts: Texts, msg_manager: MessageManager):
    to_del = await msg.answer(
        texts.company_info.serial_production,
        reply_markup=kb.user.our_servces()
    )
    await msg_manager.del_all()
    msg_manager.add_to_delete_list(to_del, msg)


@r.message(F.text.in_(bt.user.get_company_info_btns.contacts.all), StateFilter(CompanyInfo.info))
async def contacts(msg: Message, kb: Keyboards, texts: Texts, msg_manager: MessageManager):
    to_del = await msg.answer(
        texts.company_info.contacts,
        reply_markup=kb.user.contacts()
    )
    await msg_manager.del_all()
    msg_manager.add_to_delete_list(to_del, msg)


@r.message(F.text.in_(bt.user.get_company_info_btns.call.all), StateFilter(CompanyInfo.info))
async def call(msg: Message, kb: Keyboards, texts: Texts, msg_manager: MessageManager):
    to_del = await msg.answer(
        texts.company_info.call,
        reply_markup=kb.user.contacts()
    )
    await msg_manager.del_all()
    msg_manager.add_to_delete_list(to_del, msg)


@r.message(F.text.in_(bt.user.get_company_info_btns.adres.all), StateFilter(CompanyInfo.info))
async def adres(msg: Message, kb: Keyboards, texts: Texts, msg_manager: MessageManager):
    to_del = await msg.answer(
        texts.company_info.adres,
        reply_markup=kb.user.contacts()
    )
    to_del2 = await msg.answer_location(41.3170105, 69.3399196)
    await msg_manager.del_all()
    msg_manager.add_to_delete_list(to_del, msg, to_del2)


# при нажатии сразу из меню
@r.message(F.text.in_(bt.user.get_company_info_btns.adres.all))
async def adres_from_menu(msg: Message, kb: Keyboards, texts: Texts, msg_manager: MessageManager):
    to_del = await msg.answer(
        texts.company_info.adres,
        reply_markup=kb.user.menu()
    )
    to_del2 = await msg.answer_location(41.3170105, 69.3399196)
    await msg_manager.del_all()
    msg_manager.add_to_delete_list(to_del, msg, to_del2)


@r.message(F.text.in_(bt.user.get_company_info_btns.social_media.all), StateFilter(CompanyInfo.info))
async def social_media(msg: Message, kb: Keyboards, texts: Texts, msg_manager: MessageManager):
    to_del = await msg.answer(
        texts.company_info.social_media,
        reply_markup=kb.user.contacts()
    )
    await msg_manager.del_all()
    msg_manager.add_to_delete_list(to_del, msg)


@r.message(F.text.in_(bt.user.get_company_info_btns.work_mode.all), StateFilter(CompanyInfo.info))
async def work_mode(msg: Message, kb: Keyboards, texts: Texts, msg_manager: MessageManager):
    to_del = await msg.answer(
        texts.company_info.work_mode,
        reply_markup=kb.user.company_info()
    )
    await msg_manager.del_all()
    msg_manager.add_to_delete_list(to_del, msg)


@r.message(F.text.in_(bt.user.get_company_info_btns.our_works.all), StateFilter(CompanyInfo.info))
async def our_works(msg: Message, kb: Keyboards, texts: Texts, msg_manager: MessageManager):
    to_del = await msg.answer(
        texts.company_info.our_works,
        reply_markup=kb.user.our_works()
    )
    await msg_manager.del_all()
    msg_manager.add_to_delete_list(to_del, msg)


@r.message(F.text.in_(bt.user.get_company_info_btns.functional.all), StateFilter(CompanyInfo.info))
async def functional(msg: Message, kb: Keyboards, msg_manager: MessageManager):
    path = conf.photos_dir() + '/Функциональные'
    photos = photos_on_dir_list(path)
    to_del = await send_photos(msg.from_user.id, photos)
    for i in to_del:
        for j in i:
            msg_manager.add_to_delete_list(j, msg)



@r.message(F.text.in_(bt.user.get_company_info_btns.prototips.all), StateFilter(CompanyInfo.info))
async def prototips(msg: Message, kb: Keyboards, msg_manager: MessageManager):
    path = conf.photos_dir() + '/Прототипы'
    photos = photos_on_dir_list(path)
    to_del = await send_photos(msg.from_user.id, photos)
    for i in to_del:
        for j in i:
            msg_manager.add_to_delete_list(j, msg)



@r.message(F.text.in_(bt.user.get_company_info_btns.souvenirs.all), StateFilter(CompanyInfo.info))
async def souvenirs(msg: Message, kb: Keyboards, msg_manager: MessageManager):
    path = conf.photos_dir() + '/Сувениры'
    photos = photos_on_dir_list(path)
    to_del = await send_photos(msg.from_user.id, photos)
    for i in to_del:
        for j in i:
            msg_manager.add_to_delete_list(j, msg)



@r.message(F.text.in_(bt.user.get_company_info_btns.decor.all), StateFilter(CompanyInfo.info))
async def decor(msg: Message, kb: Keyboards, msg_manager: MessageManager):
    path = conf.photos_dir() + '/Декор'
    photos = photos_on_dir_list(path)
    to_del = await send_photos(msg.from_user.id, photos)
    for i in to_del:
        for j in i:
            msg_manager.add_to_delete_list(j, msg)



@r.message(F.text.in_(bt.user.get_company_info_btns.toys.all), StateFilter(CompanyInfo.info))
async def toys(msg: Message, kb: Keyboards, msg_manager: MessageManager):
    path = conf.photos_dir() + '/Игрушки'
    photos = photos_on_dir_list(path)
    to_del = await send_photos(msg.from_user.id, photos)
    for i in to_del:
        for j in i:
            msg_manager.add_to_delete_list(j, msg)



@r.message(F.text.in_(bt.user.get_company_info_btns.makets.all), StateFilter(CompanyInfo.info))
async def makets(msg: Message, kb: Keyboards, msg_manager: MessageManager):
    path = conf.photos_dir() + '/Макеты'
    photos = photos_on_dir_list(path)
    to_del = await send_photos(msg.from_user.id, photos)
    for i in to_del:
        for j in i:
            msg_manager.add_to_delete_list(j, msg)



@r.message(F.text.in_(bt.user.get_company_info_btns.figurines.all), StateFilter(CompanyInfo.info))
async def figurines(msg: Message, kb: Keyboards, msg_manager: MessageManager):
    path = conf.photos_dir() + '/Статуэтки'
    photos = photos_on_dir_list(path)
    to_del = await send_photos(msg.from_user.id, photos)
    for i in to_del:
        for j in i:
            msg_manager.add_to_delete_list(j, msg)



@r.message(F.text.in_(bt.user.get_company_info_btns.medicine.all), StateFilter(CompanyInfo.info))
async def medicine(msg: Message, kb: Keyboards, msg_manager: MessageManager):
    path = conf.photos_dir() + '/Медицина'
    photos = photos_on_dir_list(path)
    to_del = await send_photos(msg.from_user.id, photos)
    for i in to_del:
        for j in i:
            msg_manager.add_to_delete_list(j, msg)



@r.message(F.text.in_(bt.user.get_company_info_btns.delivery.all), StateFilter(CompanyInfo.info))
async def delivery(msg: Message, kb: Keyboards, texts: Texts, msg_manager: MessageManager):
    to_del = await msg.answer(
        texts.company_info.delivery,
        reply_markup=kb.user.company_info()
    )
    await msg_manager.del_all()
    msg_manager.add_to_delete_list(to_del, msg)


@r.message(F.text.in_(bt.user.get_company_info_btns.prices.all), StateFilter(CompanyInfo.info))
async def prices(msg: Message, kb: Keyboards, texts: Texts, msg_manager: MessageManager):
    to_del = await msg.answer(
        texts.company_info.prices,
        reply_markup=kb.user.company_info()
    )
    await msg_manager.del_all()
    msg_manager.add_to_delete_list(to_del, msg)


@r.message(F.text.in_(bt.user.get_company_info_btns.payment.all), StateFilter(CompanyInfo.info))
async def payment(msg: Message, kb: Keyboards, texts: Texts, msg_manager: MessageManager):
    to_del = await msg.answer(
        texts.company_info.payment,
        reply_markup=kb.user.company_info()
    )
    await msg_manager.del_all()
    msg_manager.add_to_delete_list(to_del, msg)
