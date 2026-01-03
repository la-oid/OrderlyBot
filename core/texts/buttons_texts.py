from core.utils.models import Text


class General():
    '''Общие кнопки для юзера и админа'''
    correct = Text(ru='Все верно', uz="Hammasi to'g'ri", smile='✅')
    again = Text(ru='Ввести заново', uz='Qayta kiritish', smile='🔄')
    back = Text(ru='Назад', uz='Orqaga', smile='⬅️')


class GetPrice():
    '''Кнопки для получения цены'''
    sample = Text(ru='Образец', uz='Namuna', smile='📄')
    model = Text(ru='Компьютерная модель', uz='Kompyuter modeli', smile='💻')
    draft = Text(ru='Чертеж', uz='Chizma', smile='📐')
    scetch = Text(ru='Эскиз', uz='Eskiz', smile='✏️')
    photo = Text(ru='Фото', uz='Rasm', smile='📸')
    idea = Text(ru='Идея', uz="G'oya", smile='💡')

    without_file = Text(ru='Без файла', uz="Fayl yo'q", smile='📂')
    uploaded = Text(ru='Загружено', uz='Yuklandi', smile='✅')

    prototype = Text(ru='Прототип', uz='Prototip', smile='🧩')
    functional = Text(ru='Функциональное', uz='Funktsional', smile='⚙️')
    decor = Text(ru='Декор', uz='Dekor', smile='🎨')

    under_40 = Text(ru='Не более +40°С', uz='+40°S dan yuqori emas', smile='🔥')
    under_90 = Text(ru='Не более +90°С', uz='+90°S dan yuqori emas', smile='🔥🔥')
    under_120 = Text(ru='Не более +120°С', uz='+120°S dan yuqori emas', smile='🔥🔥🔥')
    more_than_120 = Text(ru='Более +120°С', uz='+120°S dan yuqori', smile='🔥🔥🔥🔥')

    air = Text(ru='Воздух', uz='Havo', smile='🌬️')
    water = Text(ru='Вода', uz='Suv', smile='💧')
    oil = Text(ru='Масло', uz='Moy', smile='🛢️')
    other = Text(ru='Другое', uz='Boshqa', smile='❓')

    any_color = Text(ru='Любой', uz='Har qanday', smile='🌈')
    white = Text(ru='Белый', uz='Oq', smile='⚪')
    black = Text(ru='Черный', uz='Qora', smile='⚫')
    colorized = Text(ru='Цветной', uz='Rangli', smile='🖌️')

    without_comment = Text(ru='Без комментария', uz="Qo'shimcha ma'lumot yo'q", smile='🤐')


class CompanyInfo():
    '''Кнопки информации о компании'''
    our_services = Text(ru='Услуги', uz='Xizmatlar', smile='🛠️')
    contacts = Text(ru='Контакты', uz='Kontaktlar', smile='📞')
    work_mode = Text(ru='Режим работы', uz='Ish vaqti', smile='⏰')
    our_works = Text(ru='Наши работы', uz='Bizning ishlarimiz', smile='🖼️')
    delivery = Text(ru='Доставка', uz='Yetkazib berish', smile='🚚')
    prices = Text(ru='Цены', uz='Narxlar', smile='💰')
    payment = Text(ru='Оплата', uz="To'lov", smile='💳')

    print_3d = Text(ru='3D-печать', uz='3D-print', smile='⚙️')
    modeling_3d = Text(ru='3D-моделирование', uz='3D-modellashtirish', smile='💻')
    skaning_3d = Text(ru='3D-сканирование', uz='3D-skanerlash', smile='📡')
    revers_engeneering = Text(ru='Реверс-инжиниринг', uz='Revers-injiniring', smile='🔧')
    geometry_control = Text(ru='3D-контроль геометрии', uz='3D Geometriya nazorati', smile='📏')
    casting = Text(ru='Литье пластмасс', uz='Plastmassa quyish', smile='🧪')
    silicone_forms = Text(ru='Силиконовые формы', uz='Silikon qoliplar', smile='🧼')
    maketing = Text(ru='Макетирование', uz='Maketlashtirish', smile='🏗️')
    prototiping = Text(ru='Прототипирование', uz='Prototiplash', smile='🛠️')
    serial_production = Text(ru='Производство серии изделий', uz='Mahsulotlar seriyasini ishlab chiqarish', smile='🏭')

    call = Text(ru='Позвонить', uz="Qo'ng'iroq", smile='📞')
    adres = Text(ru='Адрес', uz='Manzil', smile='📍')
    social_media = Text(ru='Соцсети', uz='Ijtimoiy tarmoqlar', smile='🌐')

    functional = Text(ru='Функциональные', uz='Funktsional', smile='⚙️')
    prototips = Text(ru='Прототипы', uz='Prototiplar', smile='🧩')
    souvenirs = Text(ru='Сувениры', uz='Suvenirlar', smile='🎁')
    decor = Text(ru='Декор', uz='Dekor', smile='🎨')
    toys = Text(ru='Игрушки', uz="O'yinchoqlar", smile='🧸')
    makets = Text(ru='Макеты', uz='Maketlar', smile='🏗️')
    figurines = Text(ru='Статуэтки', uz='Statuetkalar', smile='🗿')
    medicine = Text(ru='Медицина', uz='Tibbiyot', smile='⚕️')


class User():
    '''Кнопки пользователей'''
    get_price_btns = GetPrice()
    get_company_info_btns = CompanyInfo()

    menu = Text(ru='В меню', uz='Menyuga', smile='📋')

    write_to_manager = Text(ru='Написать менеджеру', uz='Menejerga yozish', smile='💬 ')
    get_price = Text(ru='Получить расчет стоимости', uz='Narxni hisoblash', smile='📝')
    company_info = Text(ru='О компании', uz='Kompaniya haqida', smile='ℹ️')
    order_status = Text(ru='Статус заказа', uz='Buyurtma holati', smile='📦')
    rate = Text(ru='Оценить', uz='Baholash', smile='⭐️')
    language = Text(ru="Tilni o'zgartirish", uz='Поменять язык', smile='🌍')


class Admin():
    '''Кнопки админа'''


class ButtonsTexts():
    '''В целом по кнопкам'''
    user = User()
    admin = Admin()
    general = General()
