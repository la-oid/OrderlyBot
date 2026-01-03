from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

from core.keyboards.buttons import Buttons


class BaseKeyboard():
    '''Базовые клавиатуры'''

    def __init__(self, lang: str = 'ru'):  # получаем язык, создаем кнопки с текстом соответствующего языка
        self.btn = Buttons(lang)


    def reply_markup_from_buttons(self, *btns: KeyboardButton, adjust: int = 1) -> ReplyKeyboardMarkup | None:
        '''Клава из реплай кнопок, если они есть'''
        if len(btns) == 0:
            return

        builder = ReplyKeyboardBuilder()
        builder.add(*btns)
        builder.adjust(adjust)
        return builder.as_markup(resize_keyboard=True)


    def inline_markup_from_buttons(self, *btns: InlineKeyboardButton, adjust: int = 1) -> InlineKeyboardMarkup | None:
        '''Клава из инлайн кнопок, если они есть'''
        if len(btns) == 0:
            return

        builder = InlineKeyboardBuilder()
        builder.add(*btns)
        builder.adjust(adjust)
        return builder.as_markup()


class GeneralKeyboards(BaseKeyboard):
    '''Общие клавы'''

    def __init__(self, lang: str = 'ru'):  # получаем язык, создаем кнопки с текстом соответствующего языка
        self.btn = Buttons(lang)


    def check(self) -> ReplyKeyboardMarkup:
        '''Клава проверка правильности'''
        return self.reply_markup_from_buttons(
            self.btn.general.correct,
            self.btn.general.again,
            self.btn.user.menu
        )


class UserKeyboards(BaseKeyboard):
    '''Клавиатуры пользователей'''

    def __init__(self, lang: str = 'ru'):  # получаем язык, создаем кнопки с текстом соответствующего языка
        self.btn = Buttons(lang)


    def start_data(self) -> ReplyKeyboardMarkup:
        '''Клава исходных данных получения цены'''
        return self.reply_markup_from_buttons(
            self.btn.user.get_price_btns.sample,
            self.btn.user.get_price_btns.model,
            self.btn.user.get_price_btns.draft,
            self.btn.user.get_price_btns.scetch,
            self.btn.user.get_price_btns.photo,
            self.btn.user.get_price_btns.idea,
            self.btn.user.menu
        )


    def upload_files(self) -> ReplyKeyboardMarkup:
        '''загрузка файлов'''
        return self.reply_markup_from_buttons(
            self.btn.user.get_price_btns.without_file,
            self.btn.user.get_price_btns.uploaded,
            self.btn.user.menu
        )


    def usage(self) -> ReplyKeyboardMarkup:
        '''Клава выбора использования'''
        return self.reply_markup_from_buttons(
            self.btn.user.get_price_btns.prototype,
            self.btn.user.get_price_btns.functional,
            self.btn.user.get_price_btns.decor,
            self.btn.user.menu
        )


    def temperature(self) -> ReplyKeyboardMarkup:
        '''Температура, при которой используется изделие'''
        return self.reply_markup_from_buttons(
            self.btn.user.get_price_btns.under_40,
            self.btn.user.get_price_btns.under_90,
            self.btn.user.get_price_btns.under_120,
            self.btn.user.get_price_btns.more_than_120,
            self.btn.user.menu
        )


    def environment(self) -> ReplyKeyboardMarkup:
        '''Среда, в которой используется изделие'''
        return self.reply_markup_from_buttons(
            self.btn.user.get_price_btns.air,
            self.btn.user.get_price_btns.water,
            self.btn.user.get_price_btns.oil,
            self.btn.user.get_price_btns.other,
            self.btn.user.menu
        )


    def color(self) -> ReplyKeyboardMarkup:
        '''Цвет'''
        return self.reply_markup_from_buttons(
            self.btn.user.get_price_btns.any_color,
            self.btn.user.get_price_btns.black,
            self.btn.user.get_price_btns.white,
            self.btn.user.get_price_btns.colorized,
            self.btn.user.menu
        )


    def company_info(self) -> ReplyKeyboardMarkup:
        '''Клава раздела "О компании"'''
        return self.reply_markup_from_buttons(
            self.btn.user.get_company_info_btns.our_services,
            self.btn.user.get_company_info_btns.contacts,
            self.btn.user.get_company_info_btns.work_mode,
            self.btn.user.get_company_info_btns.our_works,
            self.btn.user.get_company_info_btns.delivery,
            self.btn.user.get_company_info_btns.prices,
            self.btn.user.get_company_info_btns.payment,
            self.btn.user.menu
        )


    def our_servces(self) -> ReplyKeyboardMarkup:
        '''Клава раздела услуг'''
        return self.reply_markup_from_buttons(
            self.btn.user.get_company_info_btns.print_3d,
            self.btn.user.get_company_info_btns.modeling_3d,
            self.btn.user.get_company_info_btns.skaning_3d,
            self.btn.user.get_company_info_btns.revers_engeneering,
            self.btn.user.get_company_info_btns.geometry_control,
            self.btn.user.get_company_info_btns.casting,
            self.btn.user.get_company_info_btns.silicone_forms,
            self.btn.user.get_company_info_btns.maketing,
            self.btn.user.get_company_info_btns.prototiping,
            self.btn.user.get_company_info_btns.serial_production,
            self.btn.general.back,
            self.btn.user.menu,
        )


    def contacts(self) -> ReplyKeyboardMarkup:
        '''Клава контактов'''
        return self.reply_markup_from_buttons(
            self.btn.user.get_company_info_btns.call,
            self.btn.user.get_company_info_btns.adres,
            self.btn.user.get_company_info_btns.social_media,
            self.btn.user.write_to_manager,
            self.btn.general.back,
            self.btn.user.menu,
        )


    def our_works(self) -> ReplyKeyboardMarkup:
        '''Клава наших работ'''
        return self.reply_markup_from_buttons(
            self.btn.user.get_company_info_btns.functional,
            self.btn.user.get_company_info_btns.prototips,
            self.btn.user.get_company_info_btns.souvenirs,
            self.btn.user.get_company_info_btns.decor,
            self.btn.user.get_company_info_btns.toys,
            self.btn.user.get_company_info_btns.makets,
            self.btn.user.get_company_info_btns.figurines,
            self.btn.user.get_company_info_btns.medicine,
            self.btn.general.back,
            self.btn.user.menu
        )


    def menu(self) -> ReplyKeyboardMarkup:
        '''Клава меню пользователя'''
        return self.reply_markup_from_buttons(
            self.btn.user.write_to_manager,
            self.btn.user.get_price,
            self.btn.user.company_info,
            self.btn.user.get_company_info_btns.adres,
            self.btn.user.order_status,
            self.btn.user.language
        )


    def to_menu(self) -> ReplyKeyboardMarkup:
        '''Клава в меню'''
        return self.reply_markup_from_buttons(
            self.btn.user.menu
        )


    def write_to_manager(self) -> ReplyKeyboardMarkup:
        '''Написать менеджеру'''
        return self.reply_markup_from_buttons(
            self.btn.user.write_to_manager,
            self.btn.user.menu
        )


class AdminKeyboards(BaseKeyboard):
    '''Клавиатуры админов'''

    def __init__(self, lang: str = 'ru'):  # получаем язык, создаем кнопки с текстом соответствующего языка
        self.btn = Buttons(lang)


    def stop_tracking(self, order_id: str) -> InlineKeyboardMarkup:
        '''Клава с кнопкой перестать отслеживать заказ'''
        return self.inline_markup_from_buttons(
            InlineKeyboardButton(text='Отменить', callback_data=f'untrack_{order_id}')
        )


    def check(self) -> ReplyKeyboardMarkup:
        '''Клава проверки'''
        return self.reply_markup_from_buttons(
            self.btn.general.correct,
            self.btn.general.again
        )



class Keyboards():
    '''Все клавиатуры бота'''

    def __init__(self, lang: str = 'ru'):  # получаем язык, создаем кнопки с текстом соответствующего языка
        self.btn = Buttons(lang)
        self.user = UserKeyboards(lang)
        self.admin = AdminKeyboards(lang)
        self.general = GeneralKeyboards(lang)
