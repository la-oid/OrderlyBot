from asyncio import sleep
from datetime import datetime, timedelta

from aiogram import Router, F
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext

from core.database.database import db
from core.keyboards.keyboards import Keyboards
from core.texts.buttons_texts import ButtonsTexts as bt
from core.utils.filters import GreatAdmin
from core.utils.states import Mail
from core.utils.operations import try_copy

from helper import bot

r = Router()
r.message.filter(
    GreatAdmin()
)


@r.message(F.text, Command('delme'))
async def delme(msg: Message):
    db.delete_user(msg.from_user.id)
    await msg.answer('Вы удалены')



@r.message(F.text, Command('help'))
async def help(msg: Message):
    await msg.reply(
        'Список команд:\n\n'
        '/stat - статистика пользователей\n'
        '/mail - сделать рассылку'
    )


@r.message(F.text, Command('stat'))
async def set_id(msg: Message):
    users = db.get_all_users()

    banned_bot = []
    dont_baned = []

    for user in users:
        if user.banned_bot: banned_bot.append(user)
        else: dont_baned.append(user)

    await msg.answer(
        f'Забанили: {len(banned_bot)}\n'
        f'Не забанили: {len(dont_baned)}\n'
        f'Всего: {len(users)}'
    )


@r.message(F.text.in_(bt.general.again.all), StateFilter(Mail.check))
@r.message(F.text, Command('mail'))
async def mail(msg: Message, state: FSMContext):
    await msg.answer('Отправьте мне сообщение, которое надо разослать')
    await state.set_state(Mail.get_msg)


@r.message(StateFilter(Mail.get_msg))
async def get_msg(msg: Message, state: FSMContext):
    await state.update_data(to_copy=msg)
    kb = Keyboards()
    await bot.copy_message(
        msg.chat.id,
        msg.chat.id,
        msg.message_id,
        reply_markup=kb.admin.check()
    )
    await state.set_state(Mail.check)


@r.message(F.text.in_(bt.general.correct.all), StateFilter(Mail.check))
async def correct(msg: Message, state: FSMContext):
    data = await state.get_data()
    to_copy = data['to_copy']
    users = db.get_users_for_mail()

    await msg.answer(
        f'Получено пользователей из бд: {len(users)}\n'
        f'Начинаю рассылку...'
    )

    start_time = datetime.now()
    errors = {}
    sended = 0
    for user in users:
        error = await try_copy(to_copy, user.id)
        if error:
            if error not in errors: errors[error] = 1
            else: errors[error] += 1
        else: sended += 1
        await sleep(1)

    end_time = datetime.now()
    elapsed_time = end_time - start_time  # timedelta

    # Форматируем результат в часы, минуты и секунды
    formatted_time = str(timedelta(seconds=elapsed_time.total_seconds()))
    text = (
        f'Рассылка завершена за {formatted_time}\n'
        f'Отправлено {sended} людям\n'
        f'Ошибка при отправке: {len(errors)} раз\n'
        f'Ошибки:\n\n'
    )

    for error, count in errors.items():
        text += f'{count} раза - {error}\n\n'

    await msg.answer(text, reply_markup=ReplyKeyboardRemove())
