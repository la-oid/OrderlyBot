from core.utils.models import Text, TextHolder


class CompanyInfoTexts(TextHolder):
    '''Тексты инфо о компании'''
    company_info = Text(
        ru=(
            'Наша компания — это команда людей, которые стремятся сделать технологии доступными и понятными для '
            'бизнеса. Мы занимаемся разработкой и производством решений в области 3D-печати с 2016 года. Основной '
            'фокус — создание прототипов и малых серий, что дает нашим клиентам гибкость и возможность быстро '
            'адаптироваться на всех этапах разработки.\n\n'

            'Мы работаем с самыми современными технологиями, чтобы помочь вам превращать идеи в реальность. С '
            'нашим оборудованием (парк из 40 3D-принтеров) и профессионалами (в команде 15 человек) вы получите '
            'точность и качество, которые необходимы для успешного производства. Мы понимаем, как важны детали, '
            'и наши решения всегда направлены на то, чтобы максимально эффективно решить вашу задачу.\n\n'

            'Для нас каждый проект — это не просто выполнение заказа, а возможность помочь вам достичь целей. '
            'Будь то создание прототипа, доработка изделия или производство серийных деталей — мы подходим к '
            'каждому запросу индивидуально. Мы всегда готовы предложить оптимальные решения, которые идеально '
            'подходят именно для вашего бизнеса.\n\n'

            'Вместе с вами мы создаем будущее, где инновации служат вашему успеху.'
        ),
        uz=(
            "Bizning kompaniyamiz texnologiyalarni biznes uchun tushunarli va qulay qilishga intiladigan jamoa. "
            "Biz 2016 yildan buyon 3D-print sohasida yechimlar ishlab chiqish va ishlab chiqarish bilan shug'ullanamiz. "
            "Asosiy yo'nalishimiz – prototiplar va kichik seriyalar yaratish bo'lib, bu mijozlarimizga moslashuvchanlik va "
            "barcha ishlab chiqarish bosqichlarida tez moslashish imkoniyatini beradi.\n\n"

            "Biz eng zamonaviy texnologiyalar bilan ishlaymiz va g'oyalarni haqiqatga aylantirishga yordam beramiz. "
            "Bizning uskunamiz (40 ta 3D-printer parki) va mutaxassislarimiz (15 kishilik jamoa) bilan siz muvaffaqiyatli "
            "ishlab chiqarish uchun zarur bo'lgan aniqlik va sifatni olasiz. Biz detallarning naqadar muhimligini "
            "tushunamiz va bizning yechimlarimiz har doim sizning vazifangizni maksimal samarali hal qilishga qaratilgan.\n\n"

            "Biz uchun har bir loyiha shunchaki buyurtmani bajarish emas, balki sizga maqsadlaringizga erishishda "
            "yordam berish imkoniyatidir. Prototip yaratish, mahsulotni takomillashtirish yoki seriyali qismlar ishlab "
            "chiqarish bo'lsa ham. Har bir so'rovga individual yondashamiz. Biz har doim sizning biznesingiz uchun "
            "mukammal yechimlarni taklif qilishga tayyormiz.\n\n"

            "Biz siz bilan birgalikda innovatsiyalar muvaffaqiyatingizga xizmat qiladigan kelajakni yaratamiz."
        ),
    )

    our_services = Text(
        ru='Выберите интересующий вас раздел:',
        uz="Sizni qiziqtirgan bo'limni tanlang:",
    )

    print_3d = Text(
        ru=(
            'Мы используем самые современные методы 3D-печати, чтобы создавать детали с максимальной точностью, '
            'экономя ваше время и деньги. Наши принтеры работают с разрешением до 50 микрон, что позволяет печатать '
            'даже самые сложные формы с мельчайшими деталями. Мы используем разные материалы, такие как ABS, ABS-GF, '
            'PA, PA-CF, TPU, TPU-GF, PLA, PETG, фотополимерная смола, чтобы подбирать оптимальные решения для любых нужд '
            '— от стандартных деталей до уникальных компонентов для специфических задач.\n\n'

            '3D-печать идеально подходит для быстрого прототипирования. Она помогает значительно снизить затраты на '
            'разработку и ускорить тестирование новых продуктов. Особенно эта технология полезна для малых партий или '
            'когда нужно создать уникальные детали, которые нецелесообразно производить традиционными методами.\n\n'

            'С помощью 3D-печати можно легко создать изделия с внутренними каналами, сложными геометрическими формами, '
            'или даже такие, для которых не нужно создавать дорогостоящие формы. Это не только экономит деньги, но и '
            'сокращает время на производство, уменьшая вероятность ошибок и необходимость в переделках.\n\n'

            'Кроме того, мы интегрируем 3D-печать в ваши процессы разработки, будь то создание рабочих прототипов '
            'или изготовление ограниченных серий продукции. Мы поможем адаптировать эту технологию под ваши конкретные '
            'задачи, обеспечивая максимальную гибкость и эффективность на каждом этапе.'
        ),
        uz=(
            "Biz eng zamonaviy 3D-print usullaridan foydalanamiz, bu bizga detalni maksimal aniqlikda yaratishga imkon beradi," 
            "vaqtingiz va pulingizni tejashga yordam beradi. Bizning printernlarimiz 50 mikronga qadar rezolyutsiya bilan ishlaydi, "
            "bu esa eng murakkab shakllarni eng kichik detallar bilan chop etishga imkon beradi. Biz ABS, ABS-GF, PA, PA-CF, TPU, TPU-GF, "
            "PLA, PETG, fotopolimer qatron kabi turli materiallardan foydalanamiz, bu esa har qanday ehtiyojlar uchun optimal "
            "yechimlarni tanlash imkonini beradi — standart detaldan tortib, maxsus vazifalar uchun noyob komponentlargacha.\n\n"

            "3D-print tezkor prototiplash uchun mukammal mos keladi. Bu ishlab chiqish xarajatlarini sezilarli darajada kamaytirishga "
            "va yangi mahsulotlarni sinovdan o'tkazishni tezlashtirishga yordam beradi. Ayniqsa, bu texnologiya kichik partiyalar yoki "
            "an'anaviy usullar bilan ishlab chiqarish noqulay bo'lgan noyob detallarni yaratish zarurati bo'lgan hollarda foydalidir.\n\n"

            "3D-print yordamida ichki kanallari, murakkab geometrik shakllari yoki hatto qimmatbaho shablonlarni yaratishni talab qilmaydigan "
            "mahsulotlarni osongina yaratish mumkin. Bu nafaqat pulni tejashga, balki ishlab chiqarish vaqtini qisqartirishga, xatoliklarni "
            "kamaytirishga va qayta ishlash zaruratini yo'qotishga yordam beradi.\n\n"

            "Bundan tashqari, biz 3D-printni sizning ishlab chiqarish jarayonlaringizga integratsiya qilamiz, hoh bu ishchi prototiplarni "
            "yaratish yoki cheklangan seriyali mahsulotlarni ishlab chiqarish bo'lsin. Biz ushbu texnologiyani sizning aniq vazifalaringizga "
            "moslashtirishda yordam beramiz, har bir bosqichda maksimal moslashuvchanlik va samaradorlikni ta'minlaymiz."
        ),
    )

    casting = Text(
        ru=(
            'Литье пластмасс в силиконовые формы — это идеальный способ создавать детали с высокой точностью и '
            'долговечностью, при этом сохраняя минимальные затраты. Мы используем лучшие материалы, которые идеально '
            'подходят как для прототипов, так и для серийного производства. Этот процесс позволяет добиться точности '
            'до 0,2 мм и отлично передает все детали, что особенно важно для сложных компонентов.\n\n'

            'Кроме того, мы постоянно работаем над тем, чтобы оптимизировать сам процесс литья, снижая затраты и '
            'ускоряя сроки выполнения заказов. Мы умеем работать как с малыми, так и со средними сериями, что позволяет '
            'нашим клиентам получать качественные изделия с минимальными затратами.\n\n'

            'Наши специалисты всегда готовы помочь на этапе проектирования форм для литья, что помогает избежать дефектов '
            'и улучшить качество продукции. Мы гарантируем, что каждая деталь будет соответствовать всем необходимым '
            'стандартам качества и функциональности.'
        ),
        uz=(
            "Silikon qoliplarga plastmassa quyish — bu yuqori aniqlik va uzoq muddatga samarali detalni yaratishning "
            "mukammal usuli bo'lib, shu bilan birga minimal xarajatlarni saqlab qoladi. Biz eng yaxshi materiallardan "
            "foydalanamiz, ular prototiplar uchun ham, seriyali ishlab chiqarish uchun ham ideal mos keladi. Ushbu "
            "jarayon 0,2 mm gacha aniqlikni ta'minlaydi va barcha detallarning aniq ifodalanishini ta'minlaydi, bu "
            "murakkab komponentlar uchun ayniqsa muhimdir.\n\n"

            "Bundan tashqari, biz quyish jarayonini optimallashtirish, xarajatlarni kamaytirish va buyurtmalarni bajarish "
            "muddatlarini tezlashtirish ustida doimiy ishlaymiz. Biz kichik va o'rta seriyalarda ishlashni bilamiz, bu esa "
            "mijozlarimizga minimal xarajatlar bilan sifatli mahsulotlar olish imkonini beradi.\n\n"

            "Mutaxassislarimiz quyish qoliplarini loyihalash bosqichida ham yordam berishga tayyor, bu esa nuqsonlarni "
            "oldini olish va mahsulot sifatini yaxshilashga yordam beradi. Biz har bir detalning barcha zarur sifat va "
            "funksionallik standartlariga mos kelishini kafolatlaymiz."
        ),
    )

    maketing = Text(
        ru=(
            'Макетирование играет ключевую роль в демонстрации концепций на выставках и презентациях. Мы создаем макеты '
            'в масштабе для оборудования, сооружений и объектов сложной формы, чтобы они максимально точно отражали размеры, '
            'детали и функциональные особенности оригинала. Это не просто уменьшенные копии. Они тщательно прорабатываются с '
            'учетом всех технических и эстетических деталей, чтобы быть максимально близкими к реальному объекту. Будь то '
            'промышленное оборудование, архитектурные сооружения или транспортные средства, мы создаем высококачественные '
            'прототипы, которые могут быть использованы на крупных выставках и форумах.\n\n'

            'С помощью таких макетов можно наглядно продемонстрировать функциональность, дизайн и технические характеристики '
            'продукции. Они дают возможность потенциальным клиентам, партнерам и инвесторам увидеть продукт в действии и лучше '
            'понять его особенности до начала массового производства. Такой подход способствует не только более точной '
            'презентации идей, но и эффективной обратной связи, которая помогает улучшить продукт и скорректировать проект на '
            'ранних стадиях.\n\n'

            'Когда вы работаете с нами, вы получаете высокотехнологичный инструмент для демонстрации и проверки концепций, '
            'который позволяет выделиться на выставках и показать ваш продукт в лучшем свете.'
        ),
        uz=(
            "Maketlash ko'rgazmalar va taqdimotlarda kontseptsiyalarni namoyish qilishda muhim rol o'ynaydi. Biz jihozlar, inshootlar "
            "va murakkab shakldagi obyektlar uchun maketlar yaratamiz, shunda ular o'zgarishsiz ravishda asl nusxaning o'lchamlari, "
            "detallar va funktsional xususiyatlarini aks ettiradi. Bu faqat kichraytirilgan nusxalar emas. Ular barcha texnik va estetik "
            "detallarga e'tibor berilgan holda ishlab chiqiladi, shunda ular haqiqiy obyektga eng yaqin bo'lishi ta'minlanadi. Bu sanoat "
            "uskunalari, arxitektura inshootlari yoki transport vositalari bo'lsin, biz yirik ko'rgazmalar va forumlarda foydalanish uchun "
            "yuqori sifatli prototiplar yaratamiz.\n\n"

            "Bunday maketlar yordamida mahsulotning funktsional imkoniyatlari, dizayni va texnik xususiyatlarini aniq namoyish etish mumkin. "
            "Ular potensial mijozlarga, hamkorlarga va investorlar uchun mahsulotni harakatda ko'rish va uning xususiyatlarini ommaviy ishlab "
            "chiqarish boshlanishidan oldin yaxshiroq tushunish imkonini beradi. Bunday yondashuv nafaqat g'oyalarni aniqroq taqdim etishga, "
            "balki samarali qayta aloqa olishga ham yordam beradi, bu esa mahsulotni yaxshilash va loyiha dastlabki bosqichlarida tuzatishlar "
            "kiritishga yordam beradi.\n\n"

            "Biz bilan ishlaganda siz yuqori texnologiyali vositani olasiz, bu esa kontseptsiyalarni namoyish qilish va sinovdan o'tkazish uchun "
            "mo'ljallangan bo'lib, ko'rgazmalarda ajralib turishga va mahsulotingizni eng yaxshi tomondan ko'rsatishga yordam beradi."
        ),
    )

    modeling_3d = Text(
        ru=(
            '3D-моделирование — это то, с чего начинается практически каждое наше решение. Мы создаем цифровые модели, которые '
            'точно отражают ваш замысел и позволяют протестировать его ещё до начала производства. С помощью различных программ '
            'мы проектируем даже самые сложные формы и конструкции, которые идеально подходят для 3D-печати, литья или '
            'других производственных процессов.\n\n'

            'Мы работаем с разными типами объектов — от простых деталей до сложных многослойных систем с множеством '
            'функциональных элементов. Когда мы проектируем, учитываем всё — от механической прочности до тепловых '
            'характеристик, чтобы убедиться, что готовая продукция будет работать так, как нужно. Это позволяет вам сэкономить '
            'время и деньги на тестах и предотвратить проблемы на самых ранних стадиях.\n\n'

            'Наши инженеры и дизайнеры проходят все этапы: от подготовки чертежей до финальной оптимизации модели под конкретный '
            'способ производства. Так мы не только ускоряем процесс, но и сводим к минимуму вероятность ошибок, которые могут '
            'возникнуть в дальнейшем. Моделирование помогает избежать лишних затрат на физические прототипы и даёт возможность '
            'протестировать и улучшить модель до начала производства, что значительно снижает риски.'
        ),
        uz=(
            "3D-modellashtirish — bu deyarli har bir yechimimizning boshlanishi. Biz raqamli modellardan foydalanib, sizning rejangizni "
            "aniq aks ettiramiz va uni ishlab chiqarish boshlanmasdan oldin sinab ko'rishga imkon beradi. Turli dasturlar yordamida biz "
            "eng murakkab shakllar va tuzilmalarni loyihalashni amalga oshiramiz, ular 3D-print, quyish yoki boshqa ishlab chiqarish "
            "jarayonlari uchun mukammal mos keladi.\n\n"

            "Biz turli xil obyektlar bilan ishlaymiz — oddiy detaldardan tortib, ko'p qatlamli tizimlar va ko'plab funktsional elementlarga "
            "ega murakkab tizimlargacha. Loyihalashda biz hamma narsani hisobga olamiz — mexanik kuchdan tortib issiqlik xususiyatlarigacha, "
            "va shu orqali tayyor mahsulot kerakli tarzda ishlashini ta'minlaymiz. Bu sizga testlarga sarflanadigan vaqt va mablag'ni tejashga "
            "va eng dastlabki bosqichlarda muammolarni oldini olishga yordam beradi.\n\n"

            "Bizning muhandislarimiz va dizaynerlarimiz barcha bosqichlarni o'z ichiga oladi: chizmalarni tayyorlashdan tortib, modelni aniq "
            "ishlab chiqarish usuliga moslashtirishgacha. Shunday qilib, biz jarayonni tezlashtiramiz va keyinchalik yuzaga kelishi mumkin bo'lgan "
            "xatoliklarni minimallashtiramiz. Modellash jarayoni jismoniy prototiplarga sarflanadigan ortiqcha xarajatlarni oldini olishga yordam "
            "beradi va ishlab chiqarish boshlanishidan oldin modelni sinab ko'rish va yaxshilash imkonini beradi, bu esa xavflarni sezilarli darajada kamaytiradi."
        ),
    )

    skaning_3d = Text(
        ru=(
            'С помощью 3D-сканирования мы можем восстановить любые объекты, включая те, которые повреждены, устарели или больше '
            'не производятся. Используя лазерные сканеры с точностью до 0,04 мм, мы получаем детализированные и точные модели, '
            'которые идеально подходят для анализа, доработки или улучшения конструкции.\n\n'

            'Таким образом мы можем захватывать форму и размеры объекта без его повреждения, например, с целью восстановления '
            'старых машин, оборудования или для создания уникальных деталей, которые больше не выпускаются. Также '
            '3D-сканирование помогает легко создавать запасные части, копии уникальных компонентов и точно подгонять '
            'конструкции, чтобы избежать ошибок на этапе прототипирования.\n\n'

            'Мы предоставляем вам полную цифровую реконструкцию изделия, что даёт возможность модернизировать старые детали или '
            'разрабатывать новые, сохраняя все их оригинальные характеристики. После сканирования вы получаете точные модели, '
            'которые можно использовать для 3D-печати или других методов производства.'
        ),
        uz=(
            "3D-skanerlash yordamida biz har qanday obyektlarni tiklay olishimiz mumkin, shu jumladan zarar ko'rgan, eskirgan yoki "
            "ishlab chiqarishdan to’xtaganlarini ham. 0,04 mm gacha aniqlik bilan lazerli skanerlar yordamida biz batafsil va aniq "
            "modellarga ega bo'lamiz, ular tahlil qilish, takomillashtirish yoki konstruktsiyani yaxshilash uchun mukammal mos keladi.\n\n"

            "Shu tarzda biz obyektning shaklini va o'lchamlarini uning shikastlanmasdan ushlashimiz mumkin, masalan, eski mashinalar, "
            "jihozlar tiklanishi yoki ishlab chiqarishdan to’xtagan noyob detallarni yaratish maqsadida. Shuningdek, 3D-skanerlash yordamida "
            "ehtiyot qismlar yaratish, noyob komponentlarning nusxalarini ko'paytirish va konstruktsiyalarni aniq moslashtirish, prototiplash "
            "bosqichida xatoliklardan qochish osonlashadi.\n\n"

            "Biz sizga mahsulotning to'liq raqamli rekonstruksiyasini taqdim etamiz, bu esa eski detallarni modernizatsiya qilish yoki yangi "
            "detallarni ishlab chiqishda, ularning barcha original xususiyatlarini saqlab qolish imkonini beradi. Skanerlashdan so'ng siz aniq "
            "modellarga ega bo'lasiz, ularni 3D-print yoki boshqa ishlab chiqarish usullarida ishlatishingiz mumkin."
        ),
    )

    revers_engeneering = Text(
        ru=(
            'Реверс-инжиниринг — это отличный способ вернуть жизнь старым изделиям и деталям, которые уже не производятся или '
            'не соответствуют современным стандартам. Мы используем 3D-сканирование с точностью до 0,04 мм, чтобы точно создать '
            'цифровые копии существующих объектов. Затем мы проводим подробный анализ, чтобы понять, где и как можно улучшить '
            'эти детали.\n\n'

            'Наши специалисты не просто восстанавливают старые детали, а перерабатывают их конструкцию, улучшая прочность, вес '
            'или функциональность. Это может включать выбор новых материалов, изменение геометрии, улучшение характеристик '
            'работы деталей или создание новых прототипов с улучшенными параметрами. Реверс-инжиниринг также идеально подходит '
            'для продления срока службы старого оборудования и машин, что позволяет значительно сократить затраты на '
            'производство новых деталей.\n\n'

            'Мы уверены, что каждая восстановленная деталь будет полностью соответствовать современным стандартам качества и '
            'безопасности. Это дает нашим клиентам уверенность в надежности и долговечности конечных изделий.'
        ),
        uz=(
            "Revers-injiniring - bu eskirgan yoki zamonaviy standartlarga mos kelmaydigan mahsulotlar va detallarni hayotga "
            "qaytarishning ajoyib usuli. Biz mavjud ob'ektlarning aniq raqamli nusxalarini yaratish uchun 0,04 mm gacha aniqlikdagi "
            "3D-skanerlashdan foydalanamiz. Keyin, ushbu detallarni qayerda va qanday qilib yaxshilash mumkinligini tushunish uchun "
            "batafsil tahlil o'tkazamiz.\n\n"

            "Mutaxassislarimiz faqatgina eski detallarning nusxalarini yaratib qolmay, balki ularning konstruksiyasini qayta ishlab, "
            "mustahkamlik, og'irlik yoki funksionallikni yaxshilaydilar. Bu yangi materiallarni tanlash, geometriyani o'zgartirish, "
            "detal ishlash xarakteristikalarini yaxshilash yoki yangi prototiplarni yaxshilangan parametrlar bilan yaratishni o'z ichiga "
            "olishi mumkin. Revers injiniring shuningdek eski uskunalar va mashinalar xizmat muddatini uzaytirish uchun juda mos keladi, "
            "bu yangi detallarning ishlab chiqarish xarajatlarini sezilarli darajada kamaytiradi.\n\n"

            "Biz har bir qayta tiklangan detal zamonaviy sifat va xavfsizlik standartlariga to'liq mos kelishiga ishonamiz. Bu mijozlarimizga "
            "yakuniy mahsulotlarning ishonchliligi va uzoq umr ko'rishida ishonch beradi."
        ),
    )

    geometry_control = Text(
        ru=(
            '3D-контроль геометрии — это ключевой этап в производственном процессе, который помогает удостовериться, '
            'что каждое изделие точно соответствует проекту и техническим требованиям. Для этого мы используем лазерные '
            '3D-сканеры с точностью до 0,04 мм. Это позволяет нам выявлять даже самые небольшие отклонения от нужных '
            'параметров.\n\n'

            'Процесс контроля заключается в сравнении данных, полученных с помощью сканирования, с оригинальными 3D-моделями '
            'или чертежами. Это дает возможность обнаружить любые отклонения и внести необходимые корректировки в '
            'производственный процесс. Такой подход особенно важен в таких сферах, как автомобильная, энергетическая, '
            'металлообрабатывающая или медицинская промышленность, где даже малейшие погрешности могут оказать серьезное '
            'влияние на работу.\n\n'

            'После проверки мы предоставляем полные отчеты о проведенных измерениях. Это помогает не только повысить '
            'качество, но и существенно сократить время, которое ушло бы на исправление ошибок на более поздних стадиях.'
        ),
        uz=(
            "Geometrik 3D-nazorat — bu ishlab chiqarish jarayonida har bir mahsulotning loyihaga va texnik talablarga to'liq "
            "mos kelishini tasdiqlash uchun muhim bosqichdir. Buning uchun biz aniqligi 0,04 mm gacha bo'lgan lazerli "
            "3D-skanerlardan foydalanamiz, bu esa kerakli parametrlar bo'yicha hatto eng kichik og'ishlarni ham aniqlash imkonini beradi.\n\n"

            "Nazorat jarayoni skanerlash yordamida olingan ma'lumotlarni original 3D-modellar yoki chizmalar bilan taqqoslashdan iborat. "
            "Bu har qanday og'ishlarni aniqlash va ishlab chiqarish jarayoniga kerakli tuzatishlarni kiritish imkonini beradi. Bunday "
            "yondashuv ayniqsa avtomobilsozlik, energetika, metall ishlov berish yoki tibbiyot sanoati kabi sohalarda muhimdir, chunki "
            "hatto eng kichik xatolar ham ishga jiddiy ta'sir ko'rsatishi mumkin.\n\n"

            "Tekshirishdan so'ng biz olingan o'lchovlar bo'yicha to'liq hisobotlarni taqdim etamiz. Bu nafaqat mahsulot sifatini oshirishga, "
            "balki kechikishlardagi xatolarni tuzatish uchun sarflanadigan vaqtni sezilarli darajada kamaytirishga yordam beradi."
        ),
    )

    silicone_forms = Text(
        ru=(
            'Силиконовые формы — это отличный способ производить пластиковые детали с высокой точностью, при этом можно '
            'использовать одну и ту же форму много раз. Мы работаем только с высококачественным силиконовым материалом, '
            'который идеально передает все мельчайшие детали и позволяет создавать даже самые сложные и уникальные изделия. '
            'Такие формы отлично подходят как для мелкосерийного производства, так и для создания кастомизированных '
            'деталей в ограниченных тиражах.\n\n'

            'Кроме того, силиконовые формы помогают быстро и эффективно производить изделия с минимальными затратами. Мы часто '
            'используем этот метод для создания прототипов, тестирования новых идей или просто для того, чтобы снизить расходы '
            'на массовое производство. Если нужно создать детали с высокой точностью и возможностью многократного '
            'воспроизведения, силиконовые формы — это, без сомнения, подходящее решение.\n\n'

            'Этот метод отлично работает в самых разных отраслях — от автомобильной и авиационной до медицинской и '
            'косметической, где важна каждая деталь и качество продукции.'
        ),
        uz=(
            "Silikon qoliplar — bu plastik detallarning yuqori aniqlikda ishlab chiqarilishi uchun ajoyib usul bo'lib, bir xil "
            "qolipdan bir necha marotaba foydalanish imkonini beradi. Biz faqat yuqori sifatli silikon materiallar bilan ishlaymiz, "
            "ular eng nozik detallarning aniq ifodalanishini ta'minlaydi va eng murakkab va noyob mahsulotlarni yaratishga imkon beradi. "
            "Bunday qoliplar kichik seriyali ishlab chiqarish uchun ham, cheklangan miqdorda maxsuslashtirilgan mahsulotlar yaratish "
            "uchun ham juda mos keladi.\n\n"

            "Bundan tashqari, silikon qoliplar mahsulotlarni tez va samarali ishlab chiqarish, xarajatlarni minimal darajada saqlash "
            "imkonini beradi. Biz bu usuldan prototiplarni yaratish, yangi g'oyalarni sinab ko'rish yoki ommaviy ishlab chiqarish "
            "xarajatlarini kamaytirish uchun tez-tez foydalanamiz. Agar yuqori aniqlik va ko'p martalik detallarni yaratish kerak bo'lsa, "
            "silikon qoliplar, shubhasiz, mos yechimdir.\n\n"

            "Ushbu usul avtomobilsozlik va aviatsiya sanoatidan tortib, tibbiyot va kosmetika sohalariga qadar keng ko'lamli tarmoqlarda "
            "mukammal ishlaydi, bu erda har bir detal va mahsulot sifati juda muhimdir."
        ),
    )

    prototiping = Text(
        ru=(
            'Прототипирование — это тот самый момент, когда ваши идеи начинают превращаться в реальные объекты, которые можно '
            'потрогать, протестировать и оценить. Мы предлагаем полный спектр услуг по созданию прототипов с использованием '
            'таких технологий, как 3D-печать, литье и другие современные методы. Это позволяет нам создавать прототипы быстро, '
            'без ущерба для качества.\n\n'

            'Наши прототипы точно передают не только внешний вид, но и внутренние элементы изделия, что дает возможность '
            'провести полное тестирование, выявить возможные недостатки и внести коррективы на самых первых этапах разработки. '
            'Это особенно важно для тех клиентов, которым нужно проверить, как их идея будет работать на практике.\n\n'

            'Но мы не просто создаем прототипы. Мы также помогаем улучшать их, учитывая требования, которые появятся на стадии '
            'серийного производства. Это позволяет оптимизировать конструкцию изделия еще до массового выпуска, чтобы оно '
            'соответствовало всем техническим и функциональным стандартам, а также было готово к большому тиражу.'
        ),
        uz=(
            "Prototiplash — bu sizning g'oyangiz haqiqiy obyektlarga aylanishni boshlagan vaqt, ularni qo'lingiz bilan ushlab ko'rish, "
            "sinovdan o'tkazish va baholash mumkin bo'ladi. Biz 3D print, quyish va boshqa zamonaviy usullarni qo'llagan holda "
            "prototiplar yaratish bo'yicha to'liq xizmatlar taklif qilamiz. Bu bizga prototiplarni tezda va sifatni yo'qotmasdan "
            "yaratish imkonini beradi.\n\n"

            "Bizning prototiplarimiz faqat tashqi ko'rinishni emas, balki mahsulotning ichki elementlarini ham aniq aks ettiradi, "
            "bu esa to'liq sinovdan o'tkazish, mumkin bo'lgan kamchiliklarni aniqlash va loyihaning dastlabki bosqichlarida o'zgartirishlar "
            "kiritish imkonini beradi. Bu, ayniqsa, o'z g'oyasining amaliyotda qanday ishlashini tekshirishni xohlaydigan mijozlar uchun juda muhim.\n\n"

            "Lekin biz faqat prototiplar yaratish bilan cheklanmaymiz. Biz ularni yaxshilashga ham yordam beramiz va seriyali ishlab "
            "chiqarish bosqichida paydo bo'ladigan talablarni ham hisobga olamiz. Bu, mahsulotni ommaviy chiqarilishdan oldin uning "
            "konstruktsiyasini optimallashtirishga imkon beradi, shunda u barcha texnik va funksional standartlarga mos keladi va katta "
            "miqdorda ishlab chiqarishga tayyor bo'ladi."
        ),
    )

    serial_production = Text(
        ru=(
            'Если вам нужно запустить небольшую или среднюю партию изделий — будь то для тестирования на рынке, создания '
            'ограниченных серий или подготовки к массовому производству — мы готовы помочь. Мы знаем, как важно сбалансировать '
            'качество и стоимость, и именно для этого мы предлагаем идеальные решения. С помощью наших технологий, таких как '
            'литье, 3D-печать и других современных методов, мы можем производить каждую единицу с высокой точностью, при этом '
            'минимизируя затраты.\n\n'

            'Наша команда опытных специалистов всегда рядом, чтобы помочь вам на каждом этапе — от разработки и оптимизации '
            'продукта до его производства. Мы используем только проверенные методы, чтобы каждая партия была сделана в '
            'соответствии с проектными требованиями и стандартами качества. Мы также учитываем все нюансы по срокам и бюджету, '
            'чтобы производство было не только качественным, но и экономически выгодным.\n\n'

            'Мы работаем с различными материалами и подберем наилучший вариант, подходящий именно для вашего продукта. Благодаря '
            'этому мы можем точно воспроизводить изделия, снижая риски и улучшая производственные процессы.'
        ),
        uz=(
            "Agar sizga kichik va oʻrta oʻlchamdagi mahsulotlar partiyasini ishga tushirish kerak boʻlsa – bozor sinovlari, cheklangan "
            "nashrlar yoki oldindan ishlab chiqarish uchun – biz yordam berish uchun shu yerdamiz. Biz sifat va narxni muvozanatlash "
            "qanchalik muhimligini bilamiz va shuning uchun biz mukammal yechimlarni taklif qilamiz. Quyma, 3D-print va boshqa ilg'or "
            "usullar kabi texnologiyalarimizdan foydalanib, biz har bir birlikni yuqori aniqlik bilan ishlab chiqarishimiz mumkin, shu "
            "bilan birga xarajatlarni minimallashtiramiz.\n\n"

            "Tajribali mutaxassislardan iborat jamoamiz sizga mahsulotni ishlab chiqish va optimallashtirishdan tortib ishlab "
            "chiqarishgacha bo‘lgan har qadamda yordam berish uchun shu yerda. Biz har bir partiyaning dizayn spetsifikatsiyalari "
            "va sifat standartlariga mos kelishini ta'minlash uchun faqat tasdiqlangan usullardan foydalanamiz. Shuningdek, ishlab "
            "chiqarish nafaqat yuqori sifatli, balki iqtisodiy jihatdan foydali bo'lishi uchun biz vaqt va byudjetning barcha "
            "nyuanslarini hisobga olamiz.\n\n"

            "Biz turli xil materiallar bilan ishlaymiz va mahsulotingizga mos keladigan eng yaxshi variantni tanlaymiz. Bu bizga "
            "mahsulotlarni aniq qayta ishlab chiqarish, xavflarni kamaytirish va ishlab chiqarish jarayonlarini takomillashtirish imkonini beradi."
        ),
    )

    contacts = Text(
        ru='Выберите интересующий вас раздел:',
        uz="Sizni qiziqtirgan bo'limni tanlang:",
    )
    call = Text(
        ru='+998781133882',
        uz='+998781133882',
    )
    adres = Text(
        ru="📍Адрес: г.Ташкент, Мирзо-Улугбекский р-н, ул.Ломоносова, 50. \n\n🔹Ориентир: ул.Циолковского, кафе Oltintepa jo'ja",
        uz="📍Manzil: Toshkent sh., Mirzo-Ulug‘bek tumani, Lomonosov ko‘chasi, 50-uy. \n\n🔹Mo'ljal: Tsiolkovskiy ko'chasi, kafe Oltintepa jo'ja",
    )
    social_media = Text(
        ru=(
            '🔹TELEGRAM\n'
            't.me/at3dprint\n\n'
            '🔹FACEBOOK\n'
            'facebook.com/3dprint.atech/\n\n'
            '🔹INSTAGRAM\n'
            'instagram.com/3dprint.atech/\n\n'
            '🔹САЙТ\n'
            'additiv.uz'
        ),
        uz=(
            '🔹TELEGRAM\n'
            't.me/at3dprint\n\n'
            '🔹FACEBOOK\n'
            'facebook.com/3dprint.atech/\n\n'
            '🔹INSTAGRAM\n'
            'instagram.com/3dprint.atech/\n\n'
            '🔹SAYT\n'
            'additiv.uz'
        ),
    )

    work_mode = Text(
        ru=(
            '⏰Мы работаем без перерыва на обед с понедельника по пятницу с 9:00 до 19:00, \nв '
            'субботу с 9:00 до 15:00, \nв воскресенье - выходной.\n\n'
        ),
        uz=(
            "⏰Biz tushliksiz ishlaymiz: dushanbadan jumagacha soat 9:00 dan 19:00 gacha, \nshanba kuni "
            "soat 9:00 dan 15:00 gacha, \nyakshanba - dam olish kuni.\n\n"
        ),
    )

    our_works = Text(
        ru='Выберите интересующий вас раздел:',
        uz="Sizni qiziqtirgan bo'limni tanlang:",
    )

    there_will_be_photos = Text(
        ru='Здесь будут фотографии',
        uz='Здесь будут фотографии',
    )

    delivery = Text(
        ru=(
            'Готовый заказ можно забрать в нашем офисе в рабочие часы. Для вашего удобства мы также предлагаем отправку '
            'заказов с помощью различных служб доставки. В Ташкенте вы можете получить товар через ЯндексGo или Uklon, '
            'а по Узбекистану — через почтовые службы BTS и Emu Express.\n\n'

            'Мы заботимся о вашем удобстве и предлагаем гибкие варианты доставки, чтобы вы могли получить заказ в удобное '
            'для вас время. Стоимость доставки рассчитывается в соответствии с тарифами выбранной транспортной компании '
            'и оплачивается отдельно.\n\n'

            'Для уточнения сроков и стоимости доставки, пожалуйста, свяжитесь с нами перед оформлением заказа, '
            'и мы подберем оптимальный вариант для вас.'
        ),
        uz=(
            "Tayyor buyurtmani ish vaqtida ofisimizdan olib ketishingiz mumkin. Qulayligingiz uchun biz turli yetkazib berish "
            "xizmatlari orqali buyurtmalarni yuborishni ham taklif etamiz. Toshkentda YandexGo yoki Uklon orqali, O'zbekiston "
            "bo'ylab esa BTS va Emu Express pochta xizmatlari orqali mahsulotingizni olishingiz mumkin.\n\n"

            "Biz sizning qulayligingizni o'ylaymiz va buyurtmani qulay vaqtda olishingiz uchun yetkazib berish variantlarini "
            "taklif etamiz. Yetkazib berish narxi tanlangan transport kompaniyasining tariflariga muvofiq hisoblanadi va alohida to'lanadi.\n\n"

            "Yetkazib berish muddati va narxini aniqlashtirish uchun, iltimos, buyurtma berishdan oldin biz bilan bog'laning "
            "va biz siz uchun optimal variantni tanlaymiz."
        ),
    )

    prices = Text(
        ru=(
            'Стоимость наших услуг зависит от нескольких факторов, включая наличие готовой 3D-модели для печати, '
            'объем заказа, тип и количество требуемого материала, а также требуемое качество поверхности и точность '
            'изготовления. Мы учитываем все эти параметры, чтобы предоставить клиенту наиболее оптимальное решение '
            'по цене и качеству.\n\n'

            'Минимальная стоимость одного заказа составляет 300 000 сум. Однако для точного расчета стоимости заказа '
            'важно предоставить как можно больше информации о требуемом изделии: размеры, материалы, особенности '
            'конструкции и любые другие пожелания, которые могут повлиять на цену.\n\n'

            'Мы ориентированы на прозрачность в расчетах и предлагаем конкурентоспособные цены на рынке 3D-печати '
            'и сопутствующих услуг. Наша цель — сделать процесс заказа и производства максимально удобным, '
            'понятным и доступным для клиентов.\n\n'

            'Чтобы получить точный расчет стоимости для вашего заказа, просто оставьте заявку. Наша команда быстро '
            'выполнит расчет и предоставит вам подробное предложение. Для этого нажмите кнопку “Получить расчет стоимости” '
            'и заполните форму.'
        ),
        uz=(
            "Bizning xizmatlarimizning narxi bir necha omillarga bog'liq, jumladan tayyor 3D-modelning mavjudligi, buyurtmaning "
            "hajmi, kerakli material turi va miqdori, shuningdek, sirt sifatiga va tayyorlash aniqligiga qo'yiladigan talablar. "
            "Biz ushbu parametrlarning barchasini hisobga olamiz va mijozga eng ma’qul yechimni taqdim etamiz.\n\n"

            "Bir buyurtmaning minimal narxi 300 000 so‘mni tashkil etadi. Ammo buyurtmaning aniq narxini hisoblash uchun kerakli "
            "mahsulot haqida iloji boricha ko'proq ma'lumot berish muhim: o'lchamlari, materiallar, konstruktsiya xususiyatlari "
            "va narxga ta'sir qiluvchi boshqa talablar.\n\n"

            "Biz hisob-kitoblarda shaffoflikka intilamiz va 3D-print bozorida raqobatbardosh narxlarni taklif etamiz. Bizning "
            "maqsadimiz buyurtma berish va ishlab chiqarish jarayonini mijozlar uchun maksimal darajada qulay, tushunarli va mavjud qilishdir.\n\n"

            "Buyurtmangiz uchun aniq narxni olishga, shunchaki so’rov qoldiring. Bizning jamoamiz tezda hisob-kitobni amalga oshiradi va sizga "
            "batafsil taklifni taqdim etadi. Buning uchun “Narxni hisoblash“ tugmasini bosing va shaklni to'ldiring."
        ),
    )

    payment = Text(
        ru=(
            'Мы предлагаем различные удобные способы оплаты для ваших заказов. Вы можете выбрать наиболее подходящий '
            'для вас вариант из следующего списка:\n\n '
            '- Наличные;\n\n '
            '- Пластиковая карта физического лица; \n\n '
            '- Корпоративная пластиковая карта; \n\n '
            '- Через систему Click \nhttp://indoor.click.uz/pay?id=042310&t=0; \n\n '
            '- Через систему Payme \nhttps://transfer.paycom.uz/64227f52fc0dc40f82606ea9; \n\n '
            '- Через систему Uzumbank \nhttps://www.apelsin.uz/open-service?serviceId=498609564; \n\n '
            '- Перечисление на расчетный счет по договору'
        ),
        uz=(
            "Buyurtmalaringiz uchun turli qulay to'lov usullarini taklif etamiz. Quyidagi ro'yxatdan sizga eng mos variantni tanlashingiz mumkin\n\n"
            '- Naqd pul;\n\n '
            '- Jismoniy shaxsning plastik kartasi; \n\n '
            '- Korporativ plastik karta; \n\n ' 
            '- Click tizimi orqali \nhttp://indoor.click.uz/pay?id=042310&t=0; \n\n '
            '- Payme tizimi orqali \nhttps://transfer.paycom.uz/64227f52fc0dc40f82606ea9; \n\n '
            '- Uzumbank tizimi orqali \nhttps://www.apelsin.uz/open-service?serviceId=498609564; \n\n '
            "- Shartnoma bo'yicha hisob raqamiga o'tkazish"
        ),
    )
