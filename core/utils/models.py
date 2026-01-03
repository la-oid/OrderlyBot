from typing import List
from dataclasses import dataclass, fields
from inspect import getmembers


@dataclass
class Text():
    '''Класс текста для поддержки мультиязычности'''


    ru: str = 'Текст не установлен'
    uz: str = 'Matn oʻrnatilmagan'
    smile: str = ''  # Смайлик, который будет ставиться при получении значения поля


    @property  # Нужен, чтобы отобразить все имеющиеся тексты в виде списка, при добавлении новых языков изменять не требуется
    def all(self) -> List[str]:
        '''Значение текста на всех используемых языках'''
        members = getmembers(type(self))
        items = []
        for i in list(dict(members)['__dataclass_fields__'].values()):
            if i.name not in ['smile']: items.append(getattr(self, i.name))
        return items

    @classmethod  # Получить список используемых языков, при добавлении новых языков менять не нужно
    def langs(cls) -> List[str]:
        '''Список используемых языков'''
        members = fields(cls)
        items = []
        for i in members:
            if i.name not in ['smile']: items.append(str(i.name))
        return items

    def __getitem__(self, key) -> str:  # чтобы к классу можно было обращаться как к словарю
        if key not in self.langs():
            return 'Unknown language code, please, write to manager and send screenshot of this error'
        return getattr(self, key)

    def __getattribute__(cls, name: str):  # вернуть текст со смайликом
        atr = super().__getattribute__(name)
        if name == 'smile' or not isinstance(atr, str): return atr
        return cls.smile + atr


@dataclass
class UserOrderStatusesRow():
    description: str = ''
    id: str = ''
    status: str = ''
    end_date: str = ''

    def __str__(self):
        return (
            'UserOrderStatusesRow('
            f'description={self.description}, '
            f'id={self.id}, '
            f'status={self.status}, '
            f'end_date={self.end_date})'
        )


@dataclass
class ServerOrderStatusesRow():
    id: str = ''
    status: str = ''
    price: str = None
    to_pay: str = None
    payed: str = None


    def __str__(self):
        return f'ServerOrderStatusesRow(id={self.id}, status={self.status}, price={self.price}, to_pay={self.to_pay})'


    def __post_init__(self):
        self.price = self.__validate(self.price)
        self.to_pay = self.__validate(self.to_pay)
        self.payed = self.__validate(self.payed)


    def __validate(self, value: str) -> int:
        if not value or value == '':
            return None
        return value


class TextHolder():
    '''Наследуемый инит, для классов содержащих тексты'''

    def __init__(self, lang: str = 'ru') -> None:  # При инициализации класса всем текстам выбрать язык
        self.lang = lang
        for key, value in self.__class__.__dict__.items():
            if isinstance(getattr(self.__class__, key), Text):
                self.__setattr__(key, value[lang])
