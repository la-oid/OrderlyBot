import os
from typing import List
import traceback

from aiogram.types import Message, User, InputMediaPhoto
from aiogram.utils.media_group import MediaGroupBuilder
from aiogram.types.input_file import FSInputFile
from aiogram.utils.chat_action import ChatActionSender
from aiogram.exceptions import TelegramForbiddenError

from loguru import logger

from core.database.database import db
from config import conf
from helper import bot


def photos_on_dir_list(path: str) -> list[str]:
    '''Получить список файлов в папке'''
    files = os.listdir(path)
    to_return = []
    for i in files:
        if i.endswith(('.jpg', '.jpeg', '.png')):
            to_return.append(path + '/' + i)
    return to_return


async def send_photos(user_id, photos):
    to_return = []
    # Разбиваем список фотографий на группы по 10
    for i in range(0, len(photos), 10):
        media_group = []
        for path in photos[i:i + 10]:
            media_group.append(InputMediaPhoto(media=FSInputFile(path)))
        # Отправляем группу фотографий
        async with ChatActionSender(
                action='upload_photo',
                chat_id=user_id,
                bot=bot,
        ):
            to_return.append(await bot.send_media_group(chat_id=user_id, media=media_group))
    return to_return


async def try_delete(
    msg: List[Message] | Message
):
    '''Пытается удалить сообщение'''
    if isinstance(msg, list):
        for i in msg:
            await try_delete(i)
        return
    try:
        await msg.delete()
    except Exception as e:
        logger.warning(f'Сообщение от пользователя не было удалено по причине {e}')


def is_int(string: str | List[str]) -> bool:
    '''
    Проверяет, является ли строка числом

    :param string: Проверяемая строка или список проверяемых строк
    '''
    try:
        if isinstance(string, list):
            for i in string:
                num = int(i)
        else:
            num = int(string)
            num += 1
        return True
    except Exception:
        return False


def is_float(string: str | List[str]) -> bool:
    '''
    Проверяет, является ли строка числом

    :param string: Проверяемая строка или список проверяемых строк
    '''
    try:
        if isinstance(string, list):
            for i in string:
                num = float(i)
        else:
            num = float(string)
            num += 1
        return True
    except Exception:
        return False


def set_loggers():
    logger.add(
        'logs/{time}.log',
        level='INFO',
        backtrace=True,
        diagnose=True,
        rotation='00:00',
        retention='1 week',
        catch=True
    )
    logger.add(
        'errors/{time}.log',
        level='ERROR',
        backtrace=True,
        diagnose=True,
        rotation='00:00',
        retention='1 week',
        catch=True
    )


async def create_topic(user: User) -> int:
    '''
    Создает топик с пользователем, вернет айди топика

    :param user: обьект пользователя telegram
    '''
    lastname = str(user.last_name) if user.last_name else ''
    firstname = str(user.first_name) if user.first_name else ''

    topic_name = firstname + ' ' + lastname
    topic = await bot.create_forum_topic(conf.get_support_chat_id(), name=topic_name)
    username = f'@{user.username}' if user.username else ''

    text = (
        f'{firstname} {lastname} - {username}\n'
        f'{user.id}\n'
        f'{user.language_code}'
    )
    await try_send_message(
        chat_id=conf.get_support_chat_id(),
        topic_id=topic.message_thread_id,
        text=text
    )
    await try_send_message(
        chat_id=conf.get_support_chat_id(),
        topic_id=topic.message_thread_id,
        text=(
            'Список команд:\n\n'
            '/info - информация о заказах пользователя\n'
            '/set_id <id заказа> - начать отслеживание заказа, скобки писать не нужно\n'
            '/unset_id <id заказа> - перестать отслеживать заказ, скобки писать не нужно\n'
        )
    )
    db.edit_user_topic(user.id, topic.message_thread_id)
    return topic.message_thread_id


async def try_send_to_topic(user: User, text: str, topic_id: int) -> None:
    '''Пытается отправить в топик'''
    try:
        if not await active_topic(topic_id):
            topic_id = await create_topic(user)
        await bot.send_message(
            chat_id=conf.get_support_chat_id(),
            text=text,
            message_thread_id=topic_id,
            parse_mode='html'
        )
    except Exception as e:
        text = f'Сообщение не отправлено в топик с именем "{user.username} {user.last_name}" по причине {e}\nСтек:\n\n'
        text += traceback.format_exc()
        logger.warning(text)
        return text


async def try_copy_to_topic(msg: Message, copy_msg_id: int) -> None:
    '''Пытается скопировать сообщение в топик'''
    try:
        topic_id = db.get_user(msg.from_user.id).topic_id
        if not await active_topic(topic_id):
            topic_id = await create_topic(msg.from_user)

        await bot.copy_message(
            conf.get_support_chat_id(),
            msg.chat.id,
            copy_msg_id,
            topic_id
        )
    except Exception as e:
        text = (
            f'Сообщение не скопировано в топик с именем "{msg.from_user.username} '
            f'{msg.from_user.last_name}" по причине {e}\nстек:\n\n'
        )

        text += traceback.format_exc()
        logger.warning(text)
        return text


async def try_send_files_pack(files: list[Message], chat_id: int, thread_id: int = None):
    '''Пытается отправить файлы паком в чат'''
    try:
        if thread_id:
            if not await active_topic(thread_id):
                thread_id = await create_topic(files[0].from_user)

        sending_group = MediaGroupBuilder()
        sorted_files = {}
        for msg in files:
            if msg.content_type not in sorted_files.keys():
                sorted_files[msg.content_type] = []

            if msg.content_type == 'photo':
                file_id = msg.photo[-1].file_id
            elif msg.content_type == 'video':
                file_id = msg.video.file_id
            elif msg.content_type == 'document':
                file_id = msg.document.file_id
            else:
                file_id = None

            if file_id:
                sorted_files[msg.content_type].append(file_id)

        for content_type in sorted_files:
            count = 0
            for file_id in sorted_files[content_type]:
                sending_group.add(type=content_type, media=file_id)
                count += 1
                if count % 10 == 0 or count == len(sorted_files[content_type]):
                    await bot.send_media_group(
                        chat_id=chat_id,
                        media=sending_group.build(),
                        message_thread_id=thread_id
                    )
                    sending_group = MediaGroupBuilder()

    except Exception as e:
        text = (
            f'Не удалось отправить файлы в чат {chat_id} '
            f'{f"в топик {thread_id}" if thread_id else ""} '
            f'по причине {e}, список файлов: {files}\n'
            f'Стек:\n\n'
        )
        text += traceback.format_exc()
        logger.warning(text)
        return text


async def try_send_message(
        chat_id: int, text: str, topic_id: int = None, parse_mode: str = None, reply_markup=None
) -> None | str:
    '''Пытается отправить сообщение в чат'''
    try:
        return await bot.send_message(
            chat_id=chat_id,
            text=text,
            message_thread_id=topic_id,
            parse_mode=parse_mode,
            reply_markup=reply_markup,
        )
    except TelegramForbiddenError as e:
        user = db.get_user(chat_id)
        if user:
            db.edit_user_banned(user.id)
        text = (
            f'Не удалось отправить сообщение с тектом {text} в чат {chat_id} топик {topic_id} '
            f'по причине {e}\nСтек:\n\n'
            f'{traceback.format_exc()}'
        )
        logger.warning(text)
        return text
    except Exception as e:
        text = (
            f'Не удалось отправить сообщение с тектом {text} в чат {chat_id} топик {topic_id} '
            f'по причине {e}\nСтек:\n\n'
            f'{traceback.format_exc()}'
        )
        logger.warning(text)
        return text


async def try_copy(msg: Message, chat_id: int, thread_id=None):
    '''Пытается скопировать сообщение'''
    try:
        if thread_id:
            if not await active_topic(thread_id):
                thread_id = await create_topic(msg.from_user)

        await bot.copy_message(
            chat_id=chat_id,
            from_chat_id=msg.chat.id,
            message_id=msg.message_id,
            message_thread_id=thread_id
        )
    except Exception as e:
        text = (
            f'Не удалось скопировать сообщение от '
            f'{msg.from_user.username}({msg.from_user.id}) в чат {chat_id} по причине {e}\n'
            f'\nСтек:\n\n{traceback.format_exc()}'
        )
        logger.warning(text)
        return text


async def active_topic(thread_id: int) -> bool:
    '''Проверка топика, true, если работает, false, если не работает'''
    try:
        msg = await bot.send_message(
            chat_id=conf.get_support_chat_id(),
            message_thread_id=thread_id,
            text='Проверка топика'
        )
        await msg.delete()
        return True
    except Exception as e:
        logger.error(
            f'Не удалось прочекать топик {thread_id} по причине {e}\nСтек\n\n'
            f'{traceback.format_exc()}'
        )
        return False


async def try_send_photo(chat_id: int, photo_path: str, topic_id: int = None, caption: str = None):
    '''Пытается отправить фото в чат'''
    try:
        async with ChatActionSender(
                action='upload_photo',
                chat_id=chat_id,
                message_thread_id=topic_id,
                bot=bot,
        ):
            await bot.send_photo(
                chat_id=chat_id,
                message_thread_id=topic_id,
                photo=FSInputFile(photo_path),
                caption=caption
            )

    except Exception as e:
        text = (
            f'Не удалось отправить фото {photo_path} в чат {chat_id} по причине {e}\nСтек\n'
            f'{traceback.format_exc()}'
        )
        logger.error(text)
        return text
