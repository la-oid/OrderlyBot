import os

from dotenv import load_dotenv

from core.utils.models import Text


class Config():
    '''Настройки бота'''

    def __init__(self) -> None:
        load_dotenv()


    def get_token(self) -> str:
        '''Токен бота'''
        return os.getenv('TOKEN')


    def get_admin_id(self) -> int:
        '''Айди владельца бота'''
        return int(os.getenv('ADMIN_ID'))


    def get_support_chat_id(self) -> int:
        '''Чат подержки, куда кидать обращения'''
        return int(os.getenv('SUPPORT_CHAT_ID'))


    def datetime_format(self) -> str:
        '''Формат даты и времени'''
        return '%d.%m.%Y %H:%M:%S'


    def get_db_conneciton(self) -> str:
        '''Строка подключения к бд'''
        return 'sqlite:///core/database/Xakum.db'


    def get_langs(self) -> dict[str]:
        '''языки'''
        return {
            'ru': 'русский',
            'uz': "o'zbek"
        }

    def photos_dir(self) -> str:
        '''директория с папками фоток'''
        return 'core/source/photo'


    def status_asociate(self) -> dict:
        '''словарь асоциаций для статусов'''
        return {
            'в ожидании': Text(ru='в ожидании', uz='kutmoqda'),
            'в процессе моделирования': Text(ru='в процессе моделирования', uz='modellashtirish jarayonida'),
            'в процессе производства': Text(ru='в процессе производства', uz='ishlab chiqarish jarayonida'),
            'готов': Text(ru='готов', uz='tayyor'),
            'выполнен': Text(ru='выполнен', uz='bajarildi'),
        }


    def folder_id(self) -> str:
        '''id папки'''
        return '1-0dv5liHbKm41q8IsR139Ds8NNz80Js6'



conf = Config()
