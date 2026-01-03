from aiogram.types import KeyboardButton
from core.texts.buttons_texts import ButtonsTexts as bt


class GeneralButtons():
    '''Общие кнопки для юзера и админа'''

    def __init__(self, lang: str = 'ru'):  # получаем язык, создаем кнопки с текстом соответствующего языка
        self.correct = KeyboardButton(text=bt.general.correct[lang])
        self.again = KeyboardButton(text=bt.general.again[lang])
        self.back = KeyboardButton(text=bt.general.back[lang])


class GetPriceButtons():
    '''Кнопки для получения цены'''

    def __init__(self, lang: str = 'ru'):  # получаем язык, создаем кнопки с текстом соответствующего языка
        self.sample = KeyboardButton(text=bt.user.get_price_btns.sample[lang])
        self.model = KeyboardButton(text=bt.user.get_price_btns.model[lang])
        self.draft = KeyboardButton(text=bt.user.get_price_btns.draft[lang])
        self.scetch = KeyboardButton(text=bt.user.get_price_btns.scetch[lang])
        self.photo = KeyboardButton(text=bt.user.get_price_btns.photo[lang])
        self.idea = KeyboardButton(text=bt.user.get_price_btns.idea[lang])

        self.without_file = KeyboardButton(text=bt.user.get_price_btns.without_file[lang])
        self.uploaded = KeyboardButton(text=bt.user.get_price_btns.uploaded[lang])

        self.prototype = KeyboardButton(text=bt.user.get_price_btns.prototype[lang])
        self.functional = KeyboardButton(text=bt.user.get_price_btns.functional[lang])
        self.decor = KeyboardButton(text=bt.user.get_price_btns.decor[lang])

        self.under_40 = KeyboardButton(text=bt.user.get_price_btns.under_40[lang])
        self.under_90 = KeyboardButton(text=bt.user.get_price_btns.under_90[lang])
        self.under_120 = KeyboardButton(text=bt.user.get_price_btns.under_120[lang])
        self.more_than_120 = KeyboardButton(text=bt.user.get_price_btns.more_than_120[lang])

        self.air = KeyboardButton(text=bt.user.get_price_btns.air[lang])
        self.water = KeyboardButton(text=bt.user.get_price_btns.water[lang])
        self.oil = KeyboardButton(text=bt.user.get_price_btns.oil[lang])
        self.other = KeyboardButton(text=bt.user.get_price_btns.other[lang])

        self.any_color = KeyboardButton(text=bt.user.get_price_btns.any_color[lang])
        self.white = KeyboardButton(text=bt.user.get_price_btns.white[lang])
        self.black = KeyboardButton(text=bt.user.get_price_btns.black[lang])
        self.colorized = KeyboardButton(text=bt.user.get_price_btns.colorized[lang])

        self.without_comm = KeyboardButton(text=bt.user.get_price_btns.without_comment[lang])


class CompanyInfoButtons():
    '''Кнопки информации о компании'''

    def __init__(self, lang: str = 'ru'):  # получаем язык, создаем кнопки с текстом соответствующего языка
        self.our_services = KeyboardButton(text=bt.user.get_company_info_btns.our_services[lang])
        self.contacts = KeyboardButton(text=bt.user.get_company_info_btns.contacts[lang])
        self.work_mode = KeyboardButton(text=bt.user.get_company_info_btns.work_mode[lang])
        self.our_works = KeyboardButton(text=bt.user.get_company_info_btns.our_works[lang])
        self.delivery = KeyboardButton(text=bt.user.get_company_info_btns.delivery[lang])
        self.prices = KeyboardButton(text=bt.user.get_company_info_btns.prices[lang])
        self.payment = KeyboardButton(text=bt.user.get_company_info_btns.payment[lang])

        self.print_3d = KeyboardButton(text=bt.user.get_company_info_btns.print_3d[lang])
        self.modeling_3d = KeyboardButton(text=bt.user.get_company_info_btns.modeling_3d[lang])
        self.skaning_3d = KeyboardButton(text=bt.user.get_company_info_btns.skaning_3d[lang])
        self.revers_engeneering = KeyboardButton(text=bt.user.get_company_info_btns.revers_engeneering[lang])
        self.geometry_control = KeyboardButton(text=bt.user.get_company_info_btns.geometry_control[lang])
        self.casting = KeyboardButton(text=bt.user.get_company_info_btns.casting[lang])
        self.silicone_forms = KeyboardButton(text=bt.user.get_company_info_btns.silicone_forms[lang])
        self.maketing = KeyboardButton(text=bt.user.get_company_info_btns.maketing[lang])
        self.prototiping = KeyboardButton(text=bt.user.get_company_info_btns.prototiping[lang])
        self.serial_production = KeyboardButton(text=bt.user.get_company_info_btns.serial_production[lang])

        self.call = KeyboardButton(text=bt.user.get_company_info_btns.call[lang])
        self.adres = KeyboardButton(text=bt.user.get_company_info_btns.adres[lang])
        self.social_media = KeyboardButton(text=bt.user.get_company_info_btns.social_media[lang])

        self.functional = KeyboardButton(text=bt.user.get_company_info_btns.functional[lang])
        self.prototips = KeyboardButton(text=bt.user.get_company_info_btns.prototips[lang])
        self.souvenirs = KeyboardButton(text=bt.user.get_company_info_btns.souvenirs[lang])
        self.decor = KeyboardButton(text=bt.user.get_company_info_btns.decor[lang])
        self.toys = KeyboardButton(text=bt.user.get_company_info_btns.toys[lang])
        self.makets = KeyboardButton(text=bt.user.get_company_info_btns.makets[lang])
        self.figurines = KeyboardButton(text=bt.user.get_company_info_btns.figurines[lang])
        self.medicine = KeyboardButton(text=bt.user.get_company_info_btns.medicine[lang])


class UserButtons():
    '''Кнопки пользователей'''

    def __init__(self, lang: str = 'ru'):  # получаем язык, создаем кнопки с текстом соответствующего языка
        self.get_price_btns = GetPriceButtons(lang)
        self.get_company_info_btns = CompanyInfoButtons(lang)
        self.menu = KeyboardButton(text=bt.user.menu[lang])

        self.write_to_manager = KeyboardButton(text=bt.user.write_to_manager[lang])
        self.get_price = KeyboardButton(text=bt.user.get_price[lang])
        self.company_info = KeyboardButton(text=bt.user.company_info[lang])
        self.order_status = KeyboardButton(text=bt.user.order_status[lang])
        self.language = KeyboardButton(text=bt.user.language[lang])


class AdminButtons():
    '''Кнопки админов'''

    def __init__(self, lang: str = 'ru'):  # получаем язык, создаем кнопки с текстом соответствующего языка
        pass


class Buttons():
    '''Все кнопки бота'''

    def __init__(self, lang: str = 'ru'):  # получаем язык, создаем кнопки с текстом соответствующего языка
        self.user = UserButtons(lang)
        self.admin = AdminButtons(lang)
        self.general = GeneralButtons(lang)
