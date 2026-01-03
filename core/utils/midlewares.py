from typing import Callable, Dict, Any, Awaitable
from time import perf_counter

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject, Message, User, KeyboardButton
from aiogram.fsm.context import FSMContext
from aiogram.dispatcher.flags import get_flag

from loguru import logger

from core.utils.operations import is_int, is_float, create_topic
from core.utils.models import Text
from core.database.database import db
from core.keyboards.keyboards import Keyboards
from core.texts.messages_texts import Texts
from core.utils.states import Other
from core.utils.message_manager import MessageManager

from config import conf


class IdentificateUser(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any]
    ) -> Any:
        tg_user: User = data["event_from_user"]
        state: FSMContext = data['state']
        state_data = await state.get_data()
        if 'msg_manager' not in state_data:
            await state.update_data(msg_manager=MessageManager())
            state_data = await state.get_data()

        if tg_user.is_bot:
            return await handler(event, data)

        user = db.get_user(data["event_from_user"].id)
        if user is None:
            if await state.get_state() == Other.init_user.state:
                return await handler(event, data)

            if event.message:
                kb = Keyboards()
                to_del = await event.message.answer(
                    'Iltimos, tilni tanlang\n\nПожалуйста, выберите язык',
                    reply_markup=kb.general.reply_markup_from_buttons(
                        *[KeyboardButton(text=i) for i in conf.get_langs().values()]
                    )
                )
                await state_data['msg_manager'].del_all()
                state_data['msg_manager'].add_to_delete_list(to_del, event.message)
                await state.set_state(Other.init_user)
                return
            if event.callback_query:
                to_del = await event.callback_query.answer('Iltimos, /start yuboring va tilni tanlang\n\nПожалуйста, отправьте /start и выберите язык', show_alert=True)
                state_data['msg_manager'].add_to_delete_list(to_del, event.callback_query)
                return

        if user.topic_id is None:
            topic_id = await create_topic(tg_user)
            db.edit_user_topic(tg_user.id, topic_id)

        result = await handler(event, data)
        return result


class SetLanguage(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any]
    ) -> Any:
        tg_user: User = data["event_from_user"]
        state: FSMContext = data['state']
        state_data = await state.get_data()
        mng = state_data['msg_manager']
        data['msg_manager'] = mng

        if tg_user.is_bot:
            result = await handler(event, data)
            await state.update_data(msg_manager=mng)
            return result

        user = db.get_user(data["event_from_user"].id)
        if user is None:
            if await state.get_state() == Other.init_user.state:
                result = await handler(event, data)
                await state.update_data(msg_manager=mng)
                return result

        lang = user.lang
        
        data['kb'] = Keyboards(lang)
        data['texts'] = Texts(lang)
        result = await handler(event, data)
        await state.update_data(msg_manager=mng)
        return result


class UpdateLogger(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any]
    ) -> Any:
        start_time = perf_counter()
        if event.message:
            msg_content_type = event.message.content_type
            event_type = f'сообщение({msg_content_type})'
            event_text = event.message.caption if msg_content_type == 'photo' else event.message.text
        elif event.callback_query:
            event_type = 'колбек'
            event_text = event.callback_query.data
        else:
            event_type = 'неизвестный'
            event_text = 'неизвестный'
        state = data['state']
        logger.info(
            f'Пришел апдейт типа {event_type} от @{data["event_from_user"].username} '
            f'с текстом {event_text}, state = {await state.get_state()}'
        )
        result = await handler(event, data)

        end_time = perf_counter()
        logger.info(f'Апдейт от @{data["event_from_user"].username} обработан за {round(end_time - start_time, 3)} секунд')
        return result


class MessageChecker(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
        msg: Message,
        data: Dict[str, Any]
    ) -> Any:
        checkers = self.get_checkers()

        for checker in checkers:
            if not await checker(self, data, msg):
                return

        return await handler(msg, data)


    def get_checkers(self):
        return [
            v for k, v in MessageChecker.__dict__.items()
            if k.startswith('check_')
        ]


    async def check_words_count(self, data: dict, msg: Message) -> bool:
        '''Проверка количества слов в сообщении'''
        text = get_flag(data, 'words_count')
        if text is not None:
            count = len(msg.text.split())
            if count != text['count']:
                to_del = await msg.answer(text=text['answer'])
                data['md'].add_msg_to_del_list(to_del)
                return False
        return True


    async def check_type_photo(self, data: dict, msg: Message) -> bool:
        '''Проверка на то, что это фото'''
        text = get_flag(data, "type_photo")
        if text is not None:
            if msg.content_type != 'photo':
                to_del = await msg.answer(text=text)
                data['md'].add_msg_to_del_list(to_del)
                return False
        return True


    async def check_type_text(self, data: dict, msg: Message) -> bool:
        '''Проверка на то, что это текст'''
        text = get_flag(data, "type_text")
        if text is not None:
            if msg.content_type != 'text':
                to_del = await msg.answer(text=text)
                data['md'].add_msg_to_del_list(to_del)
                return False
        return True


    async def check_type_contact(self, data: dict, msg: Message) -> bool:
        '''Проверка на то, что это контакт'''
        text = get_flag(data, 'type_contact')
        if text is not None:
            if msg.content_type != 'contact':
                to_del = await msg.answer(text=text)
                data['md'].add_msg_to_del_list(to_del)
                return False
        return True


    async def check_type_location(self, data: dict, msg: Message) -> bool:
        '''Проверка на то, что это локация'''
        text = get_flag(data, 'type_location')
        if text is not None:
            if msg.content_type != 'location':
                to_del = await msg.answer(text=text)
                data['md'].add_msg_to_del_list(to_del)
                return False
        return True


    async def check_int_words(self, data: dict, msg: Message) -> bool:
        '''Проверка на то, что сообщение имеет формат цифры'''
        params = get_flag(data, 'int_words')

        if params is not None:
            text_params = msg.text.split()
            passed = True

            for index in params['indexes']:
                if not is_int(text_params[index]):
                    passed = False

            if not passed:
                to_del = await msg.answer(text=params['answer'])
                data['md'].add_msg_to_del_list(to_del)

            return passed
        return True


    async def check_float_words(self, data: dict, msg: Message) -> bool:
        '''Проверка на то, что сообщение имеет формат цифры'''
        params = get_flag(data, 'float_words')
        if params is not None:
            text_params = msg.text.split()
            passed = True
            for index in params['indexes']:
                if not is_float(text_params[index]):
                    passed = False

            if not passed:
                to_del = await msg.answer(text=params['answer'])
                data['md'].add_msg_to_del_list(to_del)

            return passed
        return True
