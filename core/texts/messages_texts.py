from core.utils.models import Text, TextHolder
from core.texts.company_info import CompanyInfoTexts


class GetPriceTexts(TextHolder):
    '''Тексты меню'''
    start_data = Text(
        ru='Какие исходные данные у вас есть?',
        uz="Qanday dastlabki ma'lumotlaringiz bor?",
    )
    get_start_data = Text(
        ru='Загрузите исходные данные',
        uz="Dastlabki ma'lumotlarni yuklang",
    )
    size = Text(
        ru='Какие примерные размеры изделия в мм?',
        uz="Mahsulotning taxminiy o'lchamlari millimetrda qancha?",
    )
    usage = Text(
        ru='Как будет использоваться изделие?',
        uz='Mahsulot qanday ishlatiladi?',
    )
    temperature = Text(
        ru='При какой температуре будет использоваться изделие?',
        uz='Mahsulot qanday haroratda ishlatiladi?',
    )
    environment = Text(
        ru='В какой среде будет использоваться изделие?',
        uz='Mahsulot qaysi muhitda ishlatiladi?',
    )
    color = Text(
        ru='Какой цвет изделия требуется?',
        uz="Mahsulotning rangi qanday bo'lishi kerak?",
    )
    count = Text(
        ru='Какое количество изделий необходимо?',
        uz="Mahsulotlarning qancha miqdori kerak bo'ladi?",
    )
    comment = Text(
        ru='Если требуется, напишите комментарий',
        uz="Agar kerak bo'lsa, qo'shimcha ma'lumot yozing"
    )
    check_correct = Text(
        ru='Проверьте правильность ввода данных:\n\n',
        uz="Kiritilgan ma'lumotlarning to'g'riligini tekshiring:\n\n",
    )
    info_sended = Text(
        ru='Информация для расчёта стоимости отправлена! В ближайшее время менеджер свяжется с вами',
        uz="Narxlarni hisoblash uchun ma'lumot yuborildi! Menejer tez orada siz bilan bog'lanadi",
    )
    generated_text = Text(
        ru=(
            'Исходные данные: {start_data}\n'
            'Примерные размеры изделия: {size}\n'
            'Использование: {usage}\n'
            'Максимальная температура: {temperature}\n'
            'Среда: {environment}\n'
            'Цвет: {color}\n'
            'Количество: {count}\n\n'
            '{comment}'
        ),
        uz=(
            "Dastlabki ma'lumotlar: {start_data}\n"
            "Taxminiy o'lchamlari: {size}\n"
            "Qanday ishlatiladi: {usage}\n"
            "Maksimal harorat: {temperature}\n"
            "Muhit: {environment}\n"
            "Rang: {color}\n"
            "Miqdori: {count}\n\n"
            "{comment}"
        ),
    )


class MenuTexts(TextHolder):
    '''Тексты меню'''

    write_to_manager_deactivate = Text(
        ru='Режим прямого общения с менеджером деактивирован',
        uz="Menejer bilan to'g'ridan-to'g'ri muloqot rejimi o'chirilgan",
    )
    start = Text(
        ru=(
            'Здравствуйте!👋 \n\nМы занимаемся профессиональным изготовлением изделий из пластика с помощью 3D-принтеров.\nВот небольшая навигация:\n\n'
            '💬Написать менеджеру — свяжитесь напрямую со специалистом для любых вопросов.\n'
            '📝Получить расчет стоимости — отправьте информацию о вашем заказе и узнайте стоимость услуги.\n'
            'ℹ️О компании — познакомьтесь с нашей командой и услугами.\n'
            '📍Адрес — локация и адрес нашего офиса.\n'
            '📦Статус заказа — узнайте, на каком этапе производства находится ваш заказ.'
        ),
        uz=(
            "Assalomu aleykum!👋 \n\nBiz 3D printerlar yordamida plastik mahsulotlarni professional darajada ishlab chiqarish "
            "bilan shug'ullanamiz.\nMana kichik navigatsiya:\n\n"
            "💬Menejerga yozish — har qanday savollar bo‘yicha mutaxassis bilan bevosita bog‘laning.\n"
            "📝Narxni hisoblash — buyurtmangiz haqidagi ma’lumotni yuboring va xizmat narxini bilib oling.\n"
            "ℹ️Kompaniya haqida — jamoamiz va xizmatlarimiz bilan tanishing.\n"
            "📍Manzil — ofisimizning joylashuvi va manzili.\n"
            "📦Buyurtma holati — buyurtmangiz qaysi ishlab chiqarish bosqichida ekanligini bilib oling."
        ),
    )
    to_menu = Text(
        ru='Выберите необходимый раздел меню',
        uz="Kerakli menyu bo'limini tanlang",
    )
    write_to_manager = Text(
        ru=(
            'Задайте вопрос и специалист ответит вам в ближайшее время.\n'
        ),
        uz=(
            'Savolni yozing va mutaxassis sizga yaqin vaqtda javob beradi.\n'
        ),
    )
    order_status = Text(
        ru='Отправьте номер вашего заказа',
        uz='Buyurtma raqamini yuboring',
    )
    order = Text(
        ru='Заказ',
        uz='Buyurtma',
    )
    processing = Text(
        ru='Обрабатываю...',
        uz='Ishlanmoqda...'
    )


class MiscTexts(TextHolder):
    '''Тексты меню'''
    all_other = Text(
        ru='Ваше сообщение не отправлено менеджеру, необходимо выбрать Написать менеджеру',
        uz='Xabaringiz menejyerga yuborilmadi, “Menejerga yozish” tugmasini tanlash kerak',
    )
    rate_rank = Text(
        ru='Довольны ли вы заказом {order_id}? Очень доволен — 10. Совсем не доволен — 1',
        uz='{order_id} raqamli buyurtma sizni qoniqtirdimi? Juda qoniqtirdi — 10; umuman qoniqtirmadi — 1',
    )
    thx_for_rate = Text(
        ru='Спасибо за вашу оценку!',
        uz='Baholaganingiz uchun rahmat!',
    )
    choose_language = Text(
        ru='Tilni tanlang',
        uz='Выберите язык',
    )
    lang_edited = Text(
        ru='Язык изменен!',
        uz="Til o'zgartirildi!",
    )
    ask_rate = Text(
        ru='Здравствуйте. Недавно мы выполнили заказ {order_id}. Оцените пожалуйста нашу работу от 1 до 10',
        uz='Assalomu alaykum. Biz yaqinda {order_id} raqamli buyurtmani bajardik. Iltimos, ishimizni 1 dan 10 gacha baholang',
    )
    order_ready = Text(
        ru=(
            'Здравствуйте.\n'
            'Заказ {order_id} готов.'
        ),
        uz=(
            "Assalomu alaykum.\n"
            "Buyurtma {order_id} tayyor."
        )
    )
    order_price = Text(
        ru='Стоимость заказа {price} сум.',
        uz="Buyurtma narxi {price} so'm."
    )
    order_to_pay = Text(
        ru='Сумма к оплате {to_pay} сум',
        uz="To'lanadigan summa {to_pay} so'm"
    )
    order_payed = Text(
        ru='Оплачено {payed} сум.',
        uz="{payed} so'm to'landi."
    )
    order_end_date = Text(
        ru='Плановая дата выполнения заказа {end_date}.',
        uz="Buyurtmani bajarishning taxminiy sanasi {end_date}."
    )
    order_number = Text(
        ru='Номер вашего заказа {order_id}.',
        uz="Buyurtma raqami {order_id}."
    )


class ErrorsTexts(TextHolder):
    '''Тексты ошибок'''
    unknown_order = Text(
        ru='Неизвестный номер заказа, убедитесь в правильности написания',
        uz="Noma'lum buyurtma raqami, uning to'g'ri yozilganligiga ishonch hosil qiling",
    )
    not_text = Text(
        ru='Я принимаю только текстовое сообщение',
        uz='Men faqat matnli xabarlarni qabul qilaman',
    )
    not_in = Text(
        ru='Неправильное сообщение, ожидался один из предложенных вариантов',
        uz="Xabar noto'g'ri, taklif qilingan variantlardan biri kutilmoqda",
    )
    not_int = Text(
        ru='Неправильное сообщение, ожидалось целое числовое значение',
        uz="Xabar noto'g'ri, kutilgan tamsayı qiymati",
    )
    no_files = Text(
        ru='Вы не добавили ни одного файла',
        uz="Siz hech qanday fayl qo'shmagansiz",
    )
    unknown_order_for_user = Text(
        ru='Странно... Этого заказа нет в базе данных, пожалуйста, напишите об этой проблеме менеджеру',
        uz="G'alati... Bu buyurtma ma'lumotlar bazasida yo'q, iltimos, ushbu muammo haqida menejerga yozing",
    )
    rate_not_in_range = Text(
        ru='Оценка должна быть в пределах от 1 до 10',
        uz="Baho 1 dan 10 gacha bo'lishi kerak",
    )


class Texts(TextHolder):
    '''Все тексты'''

    def __init__(self, lang: str = 'ru'):
        super().__init__(lang)
        self.menu = MenuTexts(lang)
        self.errors = ErrorsTexts(lang)
        self.misc = MiscTexts(lang)
        self.get_price = GetPriceTexts(lang)
        self.company_info = CompanyInfoTexts(lang)
