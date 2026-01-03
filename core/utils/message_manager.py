from typing import List

from aiogram.types import Message

from core.utils.operations import try_delete


class MessageManager():
    '''Класс для управления отправкой и удалением сообщений'''


    def __init__(self):
        self.messages: List[Message] = []


    def add_to_delete_list(self, *msgs: Message):
        '''Добавить сообщение в список сообщений для удаления'''
        for msg in msgs:
            if msg not in self.messages:
                self.messages.append(msg)


    async def del_all(self):
        '''Удалить все сообщения в списке'''
        await try_delete(self.messages)
        self.messages.clear()
