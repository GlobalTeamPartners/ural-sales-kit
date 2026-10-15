# -*- coding: utf-8 -*-
"""
Полноценный генератор всех страниц Sales Kit для Дмитрия с глубокой интеграцией шаблонов Global Plus.
"""
import os
import json
import sys
import markdown

if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

WORKSPACE = r"c:\Users\Vlaslav\Downloads\Дима Верхняя Синичиха Алапаевск"

with open(os.path.join(WORKSPACE, "companies_database.json"), "r", encoding="utf-8") as f:
    COMPANIES = json.load(f)

# Шаблоны Global Plus
# Шаблоны Global Plus (100% RU оригинал из globalplus.tech / globalteamgroup.github.io & локальные демо)
TEMPLATES_CATALOG = [
    {
        "id": "tpl-wood",
        "title": "УралЛесПром | Оптовый B2B-Портал Древесины & Фанеры",
        "category": "Лесопромышленность & Деревообработка",
        "badge": "Калькулятор партий ГОСТ • Вагонные нормы • 1С",
        "url": "demos/wood-industry-demo/index.html",
        "video": "assets/videos/wood.mp4",
        "demo_type": "B2B-портал оптовых поставок фанеры и леса",
        "desc": "Интерактивный калькулятор кубатуры, веса и оптовой стоимости партий березовой фанеры (ФК/ФСФ) и пиломатериалов по ГОСТ с проверкой остатков на складах Верхней Синячихи.",
        "features": [
            "Калькулятор вагонных и фурных партий по ГОСТ 3916.1-96",
            "Автоматический пересчет веса, кубатуры и стоимости с НДС",
            "Моментальная выписка спецификации со счетом для строительных трестов",
            "Прямой трекинг железнодорожных накладных РЖД"
        ],
        "target_leads": "НАО «СВЕЗА Верхняя Синячиха», ООО «Лестех», Верхнесинячихинский лесохим, ООО «Алапаевский ДОЗ» (АДОЗ), Алапаевский лесопромышленный холдинг (АЛХ), ООО «Синячиха-Лес»",
        "pitch_talk": "«Снабженец из Тюмени или ХМАО хочет заказать 3 фуры фанеры 18 мм в субботу вечером. Вместо ожидания понедельника он вводит объем, видит точный вес партии и получает счет за 10 секунд. Сделка закрыта!»"
    },
    {
        "id": "tpl-zksk",
        "title": "Завод Металлоконструкций ЗКСК (Промышленность & Металлообработка)",
        "category": "Машиностроение & Металл",
        "badge": "3D-Каркасы • Расчет металлоемкости • 500K м²",
        "url": "https://globalteamgroup.github.io/zksk-sample/",
        "video": "assets/videos/machinery.mp4",
        "demo_type": "Кинематографичный портал завода металлоконструкций",
        "desc": "Полнофункциональный портал завода быстровозводимых зданий, промышленных каркасов, ангаров и металлоконструкций полного цикла с инженерным калькулятором.",
        "features": [
            "Интерактивное 3D-моделирование промышленных каркасов и пролетов",
            "Расчет металлоемкости и сметной стоимости за тонну металлопроката",
            "Портфолио реализованных объектов на 500 000+ м² с фильтрами по отраслям",
            "Презентация сертифицированной лаборатории неразрушающего контроля и сварки"
        ],
        "target_leads": "ВСЗ (Верхнесинячихинский завод), АО «Стройдормаш», ООО «ЗИСТ», ООО «Бурмаш», ПАО «Уралмашзавод», ВИЗ-Сталь, Синара ТМК, Пневмостроймашина, Котельный завод",
        "pitch_talk": "«Главный инженер и генподрядчик выбирают завод не по буклетам. Мы показываем им цифровой завод: интерактивные каркасы, допуски, реальные цеха и моментальный расчет металлоемкости партии»."
    },
    {
        "id": "tpl-machinery",
        "title": "B2B-Конфигуратор Буровых Машин & Спецтехники",
        "category": "Машиностроение & Металл",
        "badge": "3D-Селектор бурилок • Подбор шнеков • Выгрузка КП",
        "url": "demos/machinery-demo/index.html",
        "video": "assets/videos/machinery.mp4",
        "demo_type": "B2B-конфигуратор промышленного оборудования",
        "desc": "Интерактивный селектор бурильно-крановых машин, подбор бурового инструмента по категориям грунта, кросс-подбор гидромоторов PSM-Hydraulics.",
        "features": [
            "Интерактивный 3D-подбор машин под глубину бурения и тип грунта",
            "Кросс-подбор отечественных аналогов импортной гидравлики",
            "Моментальная генерация заказной спецификации и ТЗ за 15 секунд",
            "Прямая интеграция заявок с отделом сбыта завода и 1С"
        ],
        "target_leads": "АО «Стройдормаш», ООО «ЗИСТ», ООО «Бурмаш», ПАО «Уралмашзавод», УЗГА, Синара СТМ, PSM-Hydraulics, Уральский турбинный завод, СТЗ/ТМК, ВИЗ-Сталь",
        "pitch_talk": "«Главный конструктор и отдел сбыта тратят недели на согласование опросных листов. В нашей системе энергетик или строитель выбирает категорию грунта, а система сама подбирает бурилку и выкатывает готовое КП»."
    },
    {
        "id": "tpl-stroyka",
        "title": "Инженерно-Строительный Холдинг «Стройка-Про»",
        "category": "Девелопмент & Недвижимость",
        "badge": "Допуски СРО • Парк техники • Сметный калькулятор",
        "url": "https://globalteamgroup.github.io/stroyka-pro/",
        "video": "assets/videos/stroyka.mp4",
        "demo_type": "Премиальный портал генерального подрядчика",
        "desc": "Цифровой портал крупной строительной компании: каталог генподрядных проектов, лицензии СРО, презентация парка собственной спецтехники и калькулятор этапов СМР.",
        "features": [
            "Интерактивная карта сданных промышленных и жилых объектов",
            "Витрина парка тяжелой строительной техники с характеристиками",
            "Сметный калькулятор строительства объектов с разбивкой по этапам",
            "Раздел для субподрядчиков и тендерная площадка закупок"
        ],
        "target_leads": "Алапаевск-Строй, Уралстройкомплекс, Атомстройкомплекс, Брусника, ЛСР. Урал, Синара-Девелопмент, Forum Group",
        "pitch_talk": "«Заказчики уровня Газпрома или области требуют подтверждения надежности генподрядчика. Наш портал демонстрирует допуски, парк техники и видеоконтроль площадок в реальном времени»."
    },
    {
        "id": "tpl-estate",
        "title": "Девелопмент Клубных Кварталов «Luxury Estate»",
        "category": "Девелопмент & Недвижимость",
        "badge": "Интерактивный генплан • 3D-Виллы • Чат инвесторов",
        "url": "https://globalteamgroup.github.io/luxury-estate-sample/",
        "video": "assets/videos/estate.mp4",
        "demo_type": "Кинематографичный портал элитного девелопмента",
        "desc": "Сайт клубной загородной и городской недвижимости: интерактивный выбор участков на генплане, 3D-архитектурные резиденции, видовые панорамы и закрытый брокерский чат.",
        "features": [
            "Интерактивный генплан поселка со статусами участков в реальном времени",
            "3D-визуализация резиденций с возможностью кастомизации отделки",
            "Ипотечный калькулятор с расчетом премиальных кредитных программ",
            "Приватный Telegram-чат для инвесторов и закрытые презентации"
        ],
        "target_leads": "Брусника, Атомстройкомплекс, УГМК-Застройщик (Макаровский, Исеть), Forum Group (Тихвинъ), PRINZIP (Мельница), КОРТРОС Академический, Синара-Девелопмент",
        "pitch_talk": "«Покупатели элитного жилья не смотрят сухие планировки. Наш портал за 3 секунды влюбляет в объект: кинематографичные ракурсы, 3D-вид из будущего окна и моментальный выбор резиденции»."
    },
    {
        "id": "tpl-clinic",
        "title": "Многопрофильный Медицинский Центр «Клиника Европа»",
        "category": "Медицина & Эстетика",
        "badge": "Видеоряд клиники • Онлайн-запись • AI-Триаж симптомов",
        "url": "https://globalteamgroup.github.io/europa-clinic/",
        "video": "assets/videos/clinic.mp4",
        "demo_type": "Кинематографичный портал многопрофильной клиники",
        "desc": "Премиальный медицинский портал: видеоэкскурсия по отделениям, защищенная запись на приём к врачам высшей категории, каталог МРТ/КТ диагностики и личный кабинет.",
        "features": [
            "Кинематографичный видеофон операционных и стационара",
            "Интерактивная запись к докторам с синхронизацией врачебного графика",
            "Умный опросник симптомов и маршрутизация к нужному специалисту",
            "Прейскурант услуг и калькулятор комплексных диагностических чекапов"
        ],
        "target_leads": "УГМК-Здоровье, Центр косметологии им. Нудельмана, Здоровье 365, Линлайн, Парацельс, Клиника «Здоровье» (Алапаевск)",
        "pitch_talk": "«Пациент выбирает клинику по уровню доверия. В нашем решении он видит современное оборудование, квалификацию врачей и записывается со смартфона без очередей в регистратуре»."
    },
    {
        "id": "tpl-lumiere",
        "title": "Клиника Эстетической Стоматологии & Косметологии «Люмьер»",
        "category": "Медицина & Эстетика",
        "badge": "3D-Улыбка • Имплантация All-on-4 • План лечения",
        "url": "https://globalteamgroup.github.io/lumiere-clinic-sample/",
        "video": "assets/videos/dental.mp4",
        "demo_type": "Интерактивный портал эстетической стоматологии",
        "desc": "Презентация премиальной стоматологии и косметологии: 3D-моделирование улыбки, фотопротоколы До/После, протоколы имплантации All-on-4/6 и запись на консультацию.",
        "features": [
            "Интерактивный слайдер До / После реставрации и имплантации",
            "3D-визуализация протоколов дентальной имплантации ведущих брендов",
            "Калькулятор комплексного плана лечения под ключ",
            "Прямая запись на консультацию главного врача через Telegram"
        ],
        "target_leads": "Мегадента Клиник, Центр косметологии им. Нудельмана, Стоматология «Дента-Люкс» (Алапаевск), Линлайн, эстетические центры Екатеринбурга",
        "pitch_talk": "«Пациент на имплантацию на 500 000 рублей должен увидеть результат еще до кресла. Наш портал показывает реальные кейсы с макро-фотографиями и снимает все сомнения»."
    },
    {
        "id": "tpl-detailing",
        "title": "Центр Премиального Автоухода «Elite Detailing»",
        "category": "Авто & Детейлинг",
        "badge": "60fps Скролл авто • Калькулятор бронепленки • Керамика 9H",
        "url": "https://globalteamgroup.github.io/elite-detailing/",
        "video": "assets/videos/auto.mp4",
        "demo_type": "Покадровый интерактивный скролл автокомплекса",
        "desc": "Покадровая 60fps анимация премиального автомобиля с интерактивным выбором зон оклейки антигравийной полиуретановой пленкой, керамикой и записью в бокс.",
        "features": [
            "Плавный скролл автомобиля с подсветкой защитных элементов кузова",
            "Калькулятор оклейки: Зоны риска, Полная защита кузова, Полировка + Керамика 9H",
            "Онлайн-бронирование даты заезда в детейлинг-бокс",
            "Галерея макро-съемки качества подворотов пленки и реставрации кожи"
        ],
        "target_leads": "Detailing Alarm Ekb, Restyle, Порше Центр Екатеринбург, ГК «Автобан», Планета Авто, АвтоЛидер (Алапаевск)",
        "pitch_talk": "«Владельцы статусных авто выбирают глазами. Когда клиент видит на экране интерактивное преображение кузова — он не торгуется, а сразу бронирует бокс на комплексную защиту»."
    },
    {
        "id": "tpl-service",
        "title": "Сервисный Центр Спецтехники & Автоколонн",
        "category": "Авто & Детейлинг",
        "badge": "Парк спецтехники • Заказ запчастей • Выездные бригады",
        "url": "demos/service-demo/index.html",
        "video": "assets/videos/auto.mp4",
        "demo_type": "B2B-портал сервисного обслуживания спецтехники",
        "desc": "Специализированная B2B-система технического обслуживания лесовозов, тягачей, кранов и строительной техники: вызов дежурного механика и заказ запчастей.",
        "features": [
            "Интерактивный каталог услуг ТО и капитального ремонта узлов",
            "Форма вызова мобильной ремонтной бригады на делянку или карьер",
            "Каталог запчастей и гидравлических компонентов с наличием",
            "Калькулятор сервисного контракта для автопарков и лесозаготовителей"
        ],
        "target_leads": "СТО и сервис спецтехники (Верхняя Синячиха), Автобазы Алапаевска, автоколонны лесовозов Свеза и Лестех, транспортные предприятия области",
        "pitch_talk": "«Каждый день простоя лесовоза или бурилки — это сотни тысяч убытка. Наш портал позволяет механику на делянке вызвать бригаду или заказать гидронасос за 2 клика со смартфона»."
    },
    {
        "id": "tpl-horeca",
        "title": "Загородный Курорт & Спа-Отель «HoReCa Grand»",
        "category": "HoReCa & Отели",
        "badge": "Видеоряд курорта • Бронь номеров & коттеджей • Спа-клуб",
        "url": "https://globalteamgroup.github.io/horeca-grand-sample/",
        "video": "assets/videos/horeca.mp4",
        "demo_type": "Кинематографичный портал загородного курорта",
        "desc": "Атмосферный кинематографичный портал: бронирование номеров и коттеджей напрямую без комиссии агрегаторов, банный комплекс, ресторан и банкетные залы.",
        "features": [
            "Панорамный видеоряд территории курорта, спа и номеров",
            "Интерактивный модуль прямого бронирования проживания без комиссии",
            "Бронирование спа-процедур, банных ритуалов и аренда квадроциклов",
            "Презентация банкетных возможностей для корпоративов и свадеб"
        ],
        "target_leads": "Отель & Ресторан «Эрмитаж» (Алапаевск), Гостиница «Металлург», База отдыха «Чистые пруды», Загородный клуб «Белый Парус», Отель «Hyatt Regency Ekaterinburg», Небоскреб «Высоцкий»",
        "pitch_talk": "«Отели отдают агрегаторам до 20% комиссии с каждого гостя. Наш портал делает прямые продажи: гость влюбляется в видеоряд загородного отдыха и оплачивает коттедж прямо на сайте»."
    },
    {
        "id": "tpl-restaurant",
        "title": "Ресторан Авторской Кухни & Банкетный Комплекс",
        "category": "HoReCa & Отели",
        "badge": "Панорамный вид • Банкетный калькулятор • Депозиты",
        "url": "demos/horeca-demo/index.html",
        "video": "assets/videos/horeca.mp4",
        "demo_type": "Премиальный ресторанный портал",
        "desc": "Интерактивный портал ресторанной группы: выбор панорамных столиков на схеме зала, банкетный калькулятор меню и внесение депозита онлайн.",
        "features": [
            "Интерактивная карта залов с бронированием конкретного столика",
            "Банкетный калькулятор с расчетом меню и винной карты на персону",
            "Модуль приема депозитов (снижение неявок гостей до 0%)",
            "Красочное меню авторских блюд с качественными фото и составом"
        ],
        "target_leads": "Ресторан «Троекуровъ», Kitchen (панорамный), Сойка, Гастроли, Momo Pan Asian Kitchen, ресторан отеля Эрмитаж",
        "pitch_talk": "«В пятничный вечер хостес теряет звонки, а гости не приходят. В нашей системе гость выбирает столик с панорамой заката, вносит депозит за 1 минуту и получает персональное приглашение»."
    },
    {
        "id": "tpl-geotochka",
        "title": "Геоточка — Сеть Складов & Точек на Яндекс Картах",
        "category": "Пищепром & Агро",
        "badge": "Локальное SEO • Яндекс Карты • Сеть баз",
        "url": "https://globalteampartners.github.io/geotochka/",
        "video": "assets/videos/agro.mp4",
        "demo_type": "Геолокационная платформа сети",
        "desc": "Сайт-система управления и продвижения точек присутствия, складов, фирменных магазинов и сервисных центров по всей территории России.",
        "features": [
            "Интерактивная карта присутствия с автоопределением геопозиции",
            "Модуль захвата трафика из Яндекс Карт, 2ГИС и поисковиков",
            "Интеграция с локальными акциями и каталогом свежей продукции",
            "Автоматический маршрутизатор оптовиков к ближайшему складу"
        ],
        "target_leads": "Талицкое молоко (карта «Где купить свежее сегодня»), Черкашин и Партнеры, СМАК, Алапаевский молочный комбинат (АМК), сеть складов СВЕЗА и Лестех",
        "pitch_talk": "«Покупатели в Екатеринбурге и области ищут вашу свежую продукцию в шаговой доступности. Наша система показывает ближайшие магазины с наличием и приводит покупателей прямо к прилавку»."
    },
    {
        "id": "tpl-tentorium",
        "title": "Тенториум: Презентация Производства & B2B Сеть",
        "category": "Пищепром & Агро",
        "badge": "3D-Производство • Личный кабинет B2B • Франшиза",
        "url": "https://globalteampartners.github.io/tentorium-presentation/",
        "video": "assets/videos/agro.mp4",
        "demo_type": "Презентация фабрики и партнерской сети",
        "desc": "Интерактивная 3D-демонстрация чистоты промышленного производства, экологических лабораторий, условий открытия франшизы и дистрибьюторских оптовых цен.",
        "features": [
            "3D-тур по производственным линиям и лабораториям завода",
            "Презентация условий B2B-дистрибуции и маржинальности для дилеров",
            "Калькулятор окупаемости франшизы / оптового склада",
            "Личный кабинет партнера с автоматическим формированием заказа"
        ],
        "target_leads": "Птицефабрика Свердловская, АМК Алапаевск, Alma Ceramica (плитка), АДОЗ (спецтара), АЛХ (шпалы), Лестех, Верхнесинячихинский лесохим",
        "pitch_talk": "«Когда крупный федеральный закупщик выбирает поставщика, ему мало прайса в Excel. Мы показываем ему цифровой интерактивный завод: мощности, контроль качества и форму заказа партии за 3 клика»."
    },
    {
        "id": "tpl-tourism",
        "title": "Туристический Портал & Заповедники Урала",
        "category": "Туризм, Спорт & Услуги",
        "badge": "АУЖД туры • Музей Нижней Синячихи • Бронирование онлайн",
        "url": "https://globalteamgroup.github.io/tourism-sample/",
        "video": "assets/videos/tourism.mp4",
        "demo_type": "Туристический региональный портал",
        "desc": "Цифровая платформа бронирования путешествий по историческим местам Свердловской области: поездки по Алапаевской узкоколейке, Музей в Нижней Синячихе, спорткомплекс Орион и самоцветные копи.",
        "features": [
            "Интерактивная карта туристических достопримечательностей с аудиогидами",
            "Бронирование билетов на поезд АУЖД и групповых экскурсий онлайн",
            "Календарь народных праздников и фестивалей в Нижней Синячихе",
            "Готовые пакетные туры выходного дня из Екатеринбурга"
        ],
        "target_leads": "Алапаевская узкоколейная ж/д (АУЖД туризм), Музей деревянного зодчества (Нижняя Синячиха), ФОК «Орион», Центр развития туризма Свердловской области",
        "pitch_talk": "«Туристы из Москвы и Питера хотят приехать на АУЖД и в Синячиху, но не могут купить билет и заказать гида в интернете. Наша система дает им европейский сервис бронирования»."
    },
    {
        "id": "tpl-globalplus",
        "title": "Global Plus | Премиальные Веб-Решения для Бизнеса",
        "category": "Шоурил Global Plus",
        "badge": "Cinematic Scroll • Разработка за 48 часов • B2B-Лидогенерация",
        "url": "https://globalteamgroup.github.io/global-plus/",
        "video": "assets/videos/machinery.mp4",
        "demo_type": "Официальный презентационный портал агентства",
        "desc": "Официальный сайт агентства Global Plus: демонстрация возможностей кинематографичного дизайна, архитектура быстрой разработки за 48 часов, кейсы роста конверсий и контакты.",
        "features": [
            "Кинематографичный скролл мирового уровня для B2B-сегмента",
            "Презентация бизнес-результатов: рост конверсий из холодного трафика до 14%",
            "Интерактивная карта компетенций и стек технологий Global Plus",
            "Прямой контакт с основателями агентства для персонального разбора"
        ],
        "target_leads": "Визитная карточка Дмитрия для демонстрации масштаба и технологий Global Plus на любых переговорах",
        "pitch_talk": "«Мы не продаем шаблоны с конструкторов. Мы создаем цифровые системы мирового уровня, которые переводят ваш уральский бизнес в высшую лигу федеральных контрактов»."
    }
]

print("Генерация страниц началась...")

# ------------------------------------------------------------------------------
# 1. ГЕНЕРАЦИЯ Templates_Catalog.html (Витрина Шаблонов Сайтов Global Plus)
# ------------------------------------------------------------------------------
template_cards_html = []
for t in TEMPLATES_CATALOG:
    feats = "".join([f"<li>✓ {f}</li>" for f in t["features"]])
    card = f"""
    <div class="case-card" data-category="{t['category']}">
        <div class="case-video-wrap">
            <video src="{t['video']}" muted loop playsinline preload="metadata"></video>
            <div class="video-overlay"></div>
            <div class="case-category">{t['category']}</div>
            <div class="case-type-badge">{t['demo_type']}</div>
        </div>
        <div class="case-info">
            <div class="template-header">
                <div>
                    <h3 class="tpl-title">{t['title']}</h3>
                    <span class="tpl-badge">{t['badge']}</span>
                </div>
                <a href="{t['url']}" target="_blank" class="btn-open-live">Открыть во весь экран ↗</a>
            </div>
            <p class="tpl-desc">{t['desc']}</p>
            
            <div class="tpl-body-grid">
                <div class="tpl-features">
                    <h4>⚡ Ключевые возможности решения:</h4>
                    <ul>{feats}</ul>
                </div>
                <div class="tpl-targets">
                    <h4>🎯 Кому предлагать на Урале:</h4>
                    <p class="targets-text">{t['target_leads']}</p>
                </div>
            </div>

            <div class="pitch-quote">
                <div class="quote-label">🐺 Что Диме говорить директору при показе на планшете:</div>
                <p>{t['pitch_talk']}</p>
            </div>

            <div class="card-footer-actions">
                <a href="{t['url']}" target="_blank" class="btn-tpl-action btn-live">🌐 Протестировать Live-Сайт</a>
                <a href="Leads_List.html" class="btn-tpl-action btn-leads">📋 Показать клиентов в базе</a>
                <button class="btn-tpl-action btn-copy" onclick="copyLink('{t['url']}', this)">🔗 Скопировать ссылку для WhatsApp</button>
            </div>
        </div>
    </div>
    """
    template_cards_html.append(card)

templates_page_html = f"""<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Каталог Шаблонов Сайтов & Кейсов | Global Plus</title>
    <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;700&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
    <style>
        :root {{
            --bg-base: #0B0E14;
            --bg-surface: #121721;
            --bg-card: #18202E;
            --gold: #C5A059;
            --gold-light: #E0C07A;
            --red: #D32F2F;
            --green: #10B981;
            --blue: #2563EB;
            --white: #F8FAFC;
            --text-dim: #94A3B8;
            --border: rgba(197, 160, 89, 0.2);
            --border-card: rgba(255, 255, 255, 0.08);
        }}
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{
            background-color: var(--bg-base);
            color: var(--white);
            font-family: 'Inter', sans-serif;
            padding: 30px 20px 80px;
            line-height: 1.6;
        }}
        .top-nav {{
            max-width: 1200px;
            margin: 0 auto 30px;
            display: flex;
            align-items: center;
            justify-content: space-between;
        }}
        .btn-back {{
            display: inline-flex;
            align-items: center;
            gap: 8px;
            background: rgba(255, 255, 255, 0.05);
            border: 1px solid var(--border-card);
            color: var(--gold);
            padding: 8px 18px;
            border-radius: 6px;
            text-decoration: none;
            font-weight: 600;
            font-size: 0.9rem;
            transition: all 0.2s;
        }}
        .btn-back:hover {{
            background: var(--gold);
            color: #000;
        }}
        .container {{
            max-width: 1200px;
            margin: 0 auto;
        }}
        .hero-banner {{
            background: linear-gradient(135deg, rgba(197,160,89,0.12) 0%, rgba(18,23,33,0.8) 100%);
            border: 1px solid var(--gold);
            border-radius: 16px;
            padding: 35px 40px;
            margin-bottom: 35px;
        }}
        .brand-badge {{
            display: inline-block;
            color: var(--gold);
            font-size: 0.8rem;
            letter-spacing: 2px;
            text-transform: uppercase;
            font-weight: 700;
            margin-bottom: 10px;
        }}
        h1 {{
            font-family: 'Playfair Display', serif;
            color: var(--gold-light);
            font-size: clamp(2rem, 3.5vw, 2.8rem);
            margin-bottom: 12px;
        }}
        .subtitle {{
            color: var(--text-dim);
            font-size: 1.05rem;
            max-width: 850px;
        }}
        .filter-panel {{
            display: flex;
            gap: 10px;
            flex-wrap: wrap;
            margin-bottom: 35px;
            background: var(--bg-surface);
            padding: 16px;
            border-radius: 12px;
            border: 1px solid var(--border-card);
        }}
        .filter-btn {{
            background: rgba(255, 255, 255, 0.05);
            border: 1px solid var(--border-card);
            color: var(--text-dim);
            padding: 8px 16px;
            border-radius: 20px;
            font-size: 0.85rem;
            cursor: pointer;
            transition: all 0.2s;
        }}
        .filter-btn:hover, .filter-btn.active {{
            background: var(--gold);
            color: #000;
            border-color: var(--gold);
            font-weight: 600;
        }}
        .templates-grid {{
            display: flex;
            flex-direction: column;
            gap: 35px;
        }}
        .case-card {{
            background: rgba(18, 23, 33, 0.85);
            backdrop-filter: blur(16px);
            -webkit-backdrop-filter: blur(16px);
            border: 1px solid var(--border-card);
            border-radius: 18px;
            overflow: hidden;
            transition: all 0.35s cubic-bezier(0.16, 1, 0.3, 1);
            box-shadow: 0 10px 30px rgba(0,0,0,0.4);
        }}
        .case-card:hover {{
            border-color: var(--gold);
            box-shadow: 0 20px 40px rgba(197, 160, 89, 0.2), 0 0 30px rgba(0,0,0,0.7);
            transform: translateY(-4px);
        }}
        .case-video-wrap {{
            position: relative;
            width: 100%;
            height: 260px;
            background: #000;
            overflow: hidden;
        }}
        .case-video-wrap video {{
            width: 100%;
            height: 100%;
            object-fit: cover;
            display: block;
            filter: brightness(0.85);
            transition: transform 0.6s cubic-bezier(0.16, 1, 0.3, 1), filter 0.6s ease;
        }}
        .case-card:hover .case-video-wrap video {{
            transform: scale(1.05);
            filter: brightness(1.05);
        }}
        .video-overlay {{
            position: absolute;
            inset: 0;
            background: linear-gradient(180deg, rgba(0,0,0,0.2) 0%, rgba(18, 23, 33, 0.95) 100%);
            pointer-events: none;
        }}
        .case-category {{
            position: absolute;
            top: 18px;
            left: 20px;
            background: rgba(11, 14, 20, 0.85);
            backdrop-filter: blur(10px);
            border: 1px solid var(--gold);
            color: var(--gold-light);
            font-size: 0.75rem;
            font-weight: 700;
            letter-spacing: 1.5px;
            text-transform: uppercase;
            padding: 6px 14px;
            border-radius: 20px;
            z-index: 2;
            text-shadow: 0 2px 4px rgba(0,0,0,0.9);
        }}
        .case-type-badge {{
            position: absolute;
            bottom: 18px;
            right: 20px;
            background: rgba(0, 0, 0, 0.7);
            backdrop-filter: blur(8px);
            border: 1px solid rgba(255, 255, 255, 0.15);
            color: #E2E8F0;
            font-size: 0.8rem;
            font-weight: 500;
            padding: 5px 12px;
            border-radius: 6px;
            z-index: 2;
        }}
        .case-info {{
            padding: 28px 32px 32px;
        }}
        .template-header {{
            display: flex;
            justify-content: space-between;
            align-items: flex-start;
            flex-wrap: wrap;
            gap: 16px;
            margin-bottom: 16px;
            border-bottom: 1px solid var(--border-card);
            padding-bottom: 18px;
        }}
        .tpl-category {{
            font-size: 0.8rem;
            text-transform: uppercase;
            letter-spacing: 1px;
            color: var(--gold);
            font-weight: 700;
            display: block;
            margin-bottom: 6px;
        }}
        .tpl-title {{
            font-family: 'Playfair Display', serif;
            font-size: 1.6rem;
            color: var(--white);
            margin-bottom: 6px;
        }}
        .tpl-badge {{
            display: inline-block;
            background: rgba(16, 185, 129, 0.15);
            border: 1px solid rgba(16, 185, 129, 0.4);
            color: #6EE7B7;
            padding: 4px 12px;
            border-radius: 20px;
            font-size: 0.75rem;
            font-weight: 600;
        }}
        .btn-open-live {{
            background: var(--gold);
            color: #000;
            padding: 10px 22px;
            border-radius: 8px;
            text-decoration: none;
            font-weight: 700;
            font-size: 0.9rem;
            transition: all 0.2s;
        }}
        .btn-open-live:hover {{
            background: var(--gold-light);
            transform: translateY(-2px);
        }}
        .tpl-desc {{
            color: #CBD5E1;
            font-size: 1rem;
            margin-bottom: 24px;
            line-height: 1.7;
        }}
        .tpl-body-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
            gap: 24px;
            margin-bottom: 24px;
        }}
        .tpl-features, .tpl-targets {{
            background: rgba(0, 0, 0, 0.25);
            border: 1px solid var(--border-card);
            border-radius: 10px;
            padding: 20px;
        }}
        .tpl-features h4, .tpl-targets h4 {{
            font-size: 0.95rem;
            color: var(--gold-light);
            margin-bottom: 12px;
        }}
        .tpl-features ul {{
            list-style: none;
            font-size: 0.9rem;
            color: #94A3B8;
        }}
        .tpl-features li {{
            margin-bottom: 6px;
        }}
        .targets-text {{
            font-size: 0.9rem;
            color: #E2E8F0;
            line-height: 1.6;
        }}
        .pitch-quote {{
            background: rgba(197, 160, 89, 0.08);
            border-left: 4px solid var(--gold);
            border-radius: 0 8px 8px 0;
            padding: 16px 20px;
            margin-bottom: 24px;
        }}
        .quote-label {{
            font-size: 0.8rem;
            color: var(--gold);
            text-transform: uppercase;
            font-weight: 700;
            letter-spacing: 1px;
            margin-bottom: 6px;
        }}
        .pitch-quote p {{
            color: #F1F5F9;
            font-style: italic;
            font-size: 0.95rem;
        }}
        .card-footer-actions {{
            display: flex;
            gap: 12px;
            flex-wrap: wrap;
        }}
        .btn-tpl-action {{
            padding: 10px 18px;
            border-radius: 6px;
            text-decoration: none;
            font-size: 0.85rem;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.2s;
            border: none;
        }}
        .btn-live {{
            background: rgba(16, 185, 129, 0.2);
            color: #6EE7B7;
            border: 1px solid rgba(16, 185, 129, 0.4);
        }}
        .btn-live:hover {{
            background: var(--green);
            color: #000;
        }}
        .btn-leads {{
            background: rgba(37, 99, 235, 0.2);
            color: #93C5FD;
            border: 1px solid rgba(37, 99, 235, 0.4);
        }}
        .btn-leads:hover {{
            background: var(--blue);
            color: #fff;
        }}
        .btn-copy {{
            background: rgba(255, 255, 255, 0.08);
            color: #fff;
            border: 1px solid var(--border-card);
        }}
        .btn-copy:hover {{
            background: #fff;
            color: #000;
        }}
    </style>
</head>
<body>

<!-- КИНЕМАТОГРАФИЧЕСКИЙ ФОН GLOBAL PLUS -->
<div class="cinematic-bg-wrap">
    <video class="cinematic-video" autoplay muted loop playsinline src="assets/videos/machinery.mp4"></video>
    <div class="cinematic-overlay"></div>
    <div class="grain-overlay"></div>
</div>

<div class="top-nav">
    <a href="index.html" class="btn-back">&larr; Вернуться в Центр Продаж</a>
    <div style="color: var(--gold); font-size: 0.85rem; font-weight: 600;">Global Plus &times; GlobalTeamPartners</div>
</div>

<div class="container">
    <div class="hero-banner">
        <span class="brand-badge">ОФИЦИАЛЬНЫЙ ПУЛ ШАБЛОНОВ GLOBALPLUS.TECH</span>
        <h1>🔥 Каталог Боевых Шаблонов Сайтов & Кейсов</h1>
        <p class="subtitle">Кинематографичные сайты с видеофоном, 60fps-скроллом и ИИ-модулями, разработанные студией Global Plus. Открывай прямо на планшете перед уральскими директорами или отправляй ссылку в WhatsApp.</p>
    </div>

        <!-- ФИЛЬТРЫ ПО ЦЕЛЕВЫМ ОТРАСЛЯМ УРАЛА -->
    <div class="filter-panel">
        <button class="filter-btn active" data-filter="all">Все шаблоны ({len(TEMPLATES_CATALOG)})</button>
        <button class="filter-btn" data-filter="Лесопромышленность & Деревообработка">🌲 Лес & Фанера</button>
        <button class="filter-btn" data-filter="Машиностроение & Металл">⚙️ Машиностроение & Заводы</button>
        <button class="filter-btn" data-filter="Девелопмент & Недвижимость">🏙️ Девелопмент & Генподряд</button>
        <button class="filter-btn" data-filter="Медицина & Эстетика">💉 Медицина & Эстетика</button>
        <button class="filter-btn" data-filter="Авто & Детейлинг">🏎️ Авто & Детейлинг</button>
        <button class="filter-btn" data-filter="HoReCa & Отели">🏨 HoReCa & Отели</button>
        <button class="filter-btn" data-filter="Пищепром & Агро">🥛 Пищепром & Агро</button>
        <button class="filter-btn" data-filter="Туризм, Спорт & Услуги">🚂 Туризм, Спорт & Услуги</button>
        <button class="filter-btn" data-filter="Шоурил Global Plus">🌐 Шоурил Global Plus</button>
    </div>

    <!-- СЕТКА КАРТОЧЕК ШАБЛОНОВ -->
    <div class="templates-grid" id="templatesGrid">
        {''.join(template_cards_html)}
    </div>
</div>

<script>
    function copyLink(url, btn) {{
        navigator.clipboard.writeText(url).then(() => {{
            const orig = btn.innerText;
            btn.innerText = "✓ Ссылка скопирована!";
            btn.style.background = "#10B981";
            btn.style.color = "#000";
            setTimeout(() => {{
                btn.innerText = orig;
                btn.style.background = "";
                btn.style.color = "";
            }}, 2000);
        }}).catch(err => {{
            alert("Ссылка: " + url);
        }});
    }}

    document.querySelectorAll('.filter-btn').forEach(btn => {{
        btn.addEventListener('click', () => {{
            document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
            btn.classList.add('active');
            const cat = btn.getAttribute('data-filter');
            document.querySelectorAll('.case-card').forEach(card => {{
                if (cat === 'all' || card.getAttribute('data-category') === cat) {{
                    card.style.display = 'block';
                }} else {{
                    card.style.display = 'none';
                }}
            }});
        }});
    }});

    // Автовоспроизведение превью-видео при появлении в зоне видимости или наведении
    const cardVideos = document.querySelectorAll('.case-video-wrap video');
    if ('IntersectionObserver' in window) {{
        const observer = new IntersectionObserver((entries) => {{
            entries.forEach(entry => {{
                const vid = entry.target;
                if (entry.isIntersecting) {{
                    vid.muted = true;
                    vid.defaultMuted = true;
                    vid.play().catch(() => {{}});
                }} else {{
                    vid.pause();
                }}
            }});
        }}, {{ threshold: 0.2 }});
        cardVideos.forEach(v => observer.observe(v));
    }} else {{
        cardVideos.forEach(v => {{
            v.muted = true;
            v.defaultMuted = true;
            v.play().catch(() => {{}});
        }});
    }}
</script>

</body>
</html>
"""

with open(os.path.join(WORKSPACE, "Templates_Catalog.html"), "w", encoding="utf-8") as f:
    f.write(templates_page_html)
print("Templates_Catalog.html успешно сгенерирован!")

# ------------------------------------------------------------------------------
# 2. ГЕНЕРАЦИЯ index.html (Главный Хаб с новой карточкой шаблонов и витриной)
# ------------------------------------------------------------------------------
index_html = f"""<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Глобал Плюс × Global Team Partners | Центр Продаж: Урал</title>
    <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,600;0,700;1,400&family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <style>
        :root {{
            --bg-base: #0B0E14;
            --bg-surface: #121721;
            --bg-card: #18202E;
            --gold: #C5A059;
            --gold-light: #E0C07A;
            --red: #D32F2F;
            --green: #10B981;
            --blue: #2563EB;
            --purple: #8B5CF6;
            --white: #F8FAFC;
            --text-dim: #94A3B8;
            --border: rgba(197, 160, 89, 0.2);
            --border-card: rgba(255, 255, 255, 0.08);
        }}
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{
            background-color: var(--bg-base);
            color: var(--white);
            font-family: 'Inter', -apple-system, sans-serif;
            line-height: 1.6;
            overflow-x: hidden;
        }}
        header {{
            background: linear-gradient(180deg, #10141D 0%, #0B0E14 100%);
            border-bottom: 2px solid var(--border);
            padding: 60px 20px 45px;
            text-align: center;
            position: relative;
        }}
        header::after {{
            content: '';
            position: absolute;
            bottom: -2px;
            left: 50%;
            transform: translateX(-50%);
            width: 240px;
            height: 3px;
            background: linear-gradient(90deg, transparent, var(--gold), transparent);
        }}
        .brand-pill {{
            display: inline-flex;
            align-items: center;
            gap: 8px;
            background: rgba(197, 160, 89, 0.12);
            border: 1px solid var(--gold);
            color: var(--gold-light);
            padding: 6px 18px;
            border-radius: 30px;
            font-size: 11px;
            letter-spacing: 2.5px;
            text-transform: uppercase;
            font-weight: 700;
            margin-bottom: 20px;
        }}
        h1 {{
            font-family: 'Playfair Display', serif;
            font-size: clamp(2rem, 4vw, 3.2rem);
            font-weight: 700;
            color: var(--white);
            margin-bottom: 12px;
            letter-spacing: -0.5px;
        }}
        h1 span.cross {{
            color: var(--gold);
            font-weight: 400;
            padding: 0 8px;
        }}
        h1 span.highlight {{
            color: var(--gold-light);
        }}
        .subtitle {{
            font-size: clamp(1rem, 1.8vw, 1.25rem);
            color: var(--text-dim);
            max-width: 850px;
            margin: 0 auto 15px;
        }}
        .partner-badge {{
            display: inline-block;
            background: rgba(211, 47, 47, 0.15);
            border: 1px solid rgba(211, 47, 47, 0.4);
            color: #FF8A80;
            font-size: 0.85rem;
            padding: 5px 16px;
            border-radius: 20px;
            font-weight: 600;
        }}
        .container {{
            max-width: 1240px;
            margin: 40px auto 80px;
            padding: 0 24px;
        }}
        .stats-bar {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
            gap: 16px;
            margin-bottom: 40px;
        }}
        .stat-card {{
            background: var(--bg-surface);
            border: 1px solid var(--border-card);
            border-radius: 12px;
            padding: 20px 24px;
            text-align: center;
        }}
        .stat-num {{
            font-family: 'Playfair Display', serif;
            font-size: 2.2rem;
            font-weight: 700;
            color: var(--gold);
        }}
        .stat-label {{
            font-size: 0.8rem;
            color: var(--text-dim);
            text-transform: uppercase;
            letter-spacing: 1px;
            margin-top: 4px;
        }}
        .section-heading {{
            font-family: 'Playfair Display', serif;
            font-size: 1.8rem;
            margin-bottom: 24px;
            color: var(--white);
            display: flex;
            align-items: center;
            gap: 12px;
        }}
        .section-heading::after {{
            content: '';
            flex: 1;
            height: 1px;
            background: var(--border-card);
        }}
        .grid-core {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(340px, 1fr));
            gap: 24px;
            margin-bottom: 60px;
        }}
        .hub-card {{
            background: var(--bg-surface);
            border: 1px solid var(--border-card);
            border-radius: 16px;
            padding: 32px;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
            position: relative;
            overflow: hidden;
        }}
        .hub-card::before {{
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 4px;
            background: var(--card-accent, var(--gold));
            opacity: 0;
            transition: opacity 0.3s;
        }}
        .hub-card:hover {{
            transform: translateY(-6px);
            border-color: rgba(197, 160, 89, 0.5);
            box-shadow: 0 16px 36px rgba(0, 0, 0, 0.4);
        }}
        .hub-card:hover::before {{
            opacity: 1;
        }}
        .hub-card.lead-database {{ --card-accent: var(--gold); }}
        .hub-card.strategy {{ --card-accent: var(--red); }}
        .hub-card.templates {{ --card-accent: #EAB308; }}
        .hub-card.scripts {{ --card-accent: var(--green); }}
        .hub-card.pitches {{ --card-accent: var(--purple); }}
        .hub-card.brand {{ --card-accent: linear-gradient(90deg, var(--gold), var(--red)); }}
        .hub-card.intel {{ --card-accent: var(--blue); }}
        
        .card-icon {{
            font-size: 2.4rem;
            margin-bottom: 16px;
            display: inline-block;
        }}
        .card-title {{
            font-family: 'Playfair Display', serif;
            font-size: 1.45rem;
            color: var(--white);
            margin-bottom: 12px;
        }}
        .card-desc {{
            color: var(--text-dim);
            font-size: 0.95rem;
            line-height: 1.6;
            margin-bottom: 24px;
            flex-grow: 1;
        }}
        .btn-card {{
            display: inline-flex;
            align-items: center;
            justify-content: space-between;
            background: rgba(255, 255, 255, 0.05);
            border: 1px solid var(--border-card);
            color: var(--white);
            padding: 12px 20px;
            border-radius: 8px;
            text-decoration: none;
            font-weight: 600;
            font-size: 0.9rem;
            transition: all 0.2s;
        }}
        .btn-card:hover {{
            background: var(--gold);
            border-color: var(--gold);
            color: #000;
        }}
        .badge-hot {{
            background: var(--red);
            color: #fff;
            padding: 2px 8px;
            border-radius: 12px;
            font-size: 0.7rem;
            font-weight: 700;
            margin-left: 8px;
            letter-spacing: 1px;
        }}

        /* ДЕМО СЕКЦИЯ */
        .demo-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 20px;
            margin-bottom: 60px;
        }}
        .demo-card {{
            background: rgba(18, 23, 33, 0.85);
            backdrop-filter: blur(12px);
            border: 1px solid var(--border-card);
            border-radius: 14px;
            overflow: hidden;
            display: flex;
            flex-direction: column;
            transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
        }}
        .demo-card:hover {{
            border-color: var(--gold);
            transform: translateY(-4px);
            box-shadow: 0 12px 30px rgba(0,0,0,0.5);
        }}
        .demo-thumb {{
            position: relative;
            width: 100%;
            height: 140px;
            background: #000;
            overflow: hidden;
        }}
        .demo-thumb video {{
            width: 100%;
            height: 100%;
            object-fit: cover;
            display: block;
            filter: brightness(0.8);
            transition: transform 0.5s ease;
        }}
        .demo-card:hover .demo-thumb video {{
            transform: scale(1.06);
            filter: brightness(1.0);
        }}
        .demo-thumb-overlay {{
            position: absolute;
            inset: 0;
            background: linear-gradient(180deg, rgba(0,0,0,0.1) 0%, rgba(18, 23, 33, 0.9) 100%);
            pointer-events: none;
        }}
        .demo-content {{
            padding: 18px 20px 20px;
            display: flex;
            flex-direction: column;
            flex-grow: 1;
            justify-content: space-between;
        }}
        .demo-title {{
            font-size: 1.15rem;
            font-weight: 600;
            color: var(--white);
            margin-bottom: 8px;
            display: flex;
            align-items: center;
            gap: 8px;
        }}
        .demo-subtitle {{
            font-size: 0.85rem;
            color: var(--text-dim);
            margin-bottom: 16px;
        }}
        .demo-link {{
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 10px 14px;
            background: rgba(16, 185, 129, 0.1);
            border: 1px solid rgba(16, 185, 129, 0.3);
            border-radius: 6px;
            color: #6EE7B7;
            text-decoration: none;
            font-size: 0.85rem;
            font-weight: 600;
            transition: all 0.2s;
        }}
        .demo-link:hover {{
            background: var(--green);
            color: #000;
        }}

        footer {{
            text-align: center;
            padding: 50px 20px;
            border-top: 1px solid var(--border-card);
            color: var(--text-dim);
            font-size: 0.85rem;
        }}
    </style>
</head>
<body>

<!-- КИНЕМАТОГРАФИЧЕСКИЙ ФОН GLOBAL PLUS -->
<div class="cinematic-bg-wrap">
    <video class="cinematic-video" autoplay muted loop playsinline src="assets/videos/machinery.mp4"></video>
    <div class="cinematic-overlay"></div>
    <div class="grain-overlay"></div>
</div>

<header>
    <div class="brand-pill">GLOBAL PLUS &times; GLOBAL TEAM PARTNERS</div>
    <h1>Уральский Центр Продаж <span class="cross">&times;</span> <span class="highlight">Штаб Димы</span></h1>
    <p class="subtitle">Интегрированная система экспансии, коммерческих предложений и готовых сайтов: Верхняя Синячиха &bull; Алапаевск &bull; Екатеринбург</p>
    <div class="partner-badge">🎯 Региональный партнер: Дмитрий | Свердловская область</div>
</header>

<div class="container">

    <!-- СТАТИСТИЧЕСКАЯ ПАНЕЛЬ -->
    <div class="stats-bar">
        <div class="stat-card">
            <div class="stat-num">62</div>
            <div class="stat-label">Отобранных предприятия</div>
        </div>
        <div class="stat-card">
            <div class="stat-num">15</div>
            <div class="stat-label">Шаблонов сайтов Global Plus</div>
        </div>
        <div class="stat-card">
            <div class="stat-num">3</div>
            <div class="stat-label">Географических пояса</div>
        </div>
        <div class="stat-card">
            <div class="stat-num">48 ч</div>
            <div class="stat-label">Запуск прототипа</div>
        </div>
    </div>

    <!-- КЛЮЧЕВЫЕ МОДУЛИ ШТАБА -->
    <h2 class="section-heading">⚡ Стратегические Инструменты Партнера</h2>

    <div class="grid-core">

        <!-- КАРТОЧКА 1: БАЗА ЛИДОВ -->
        <div class="hub-card lead-database">
            <div>
                <span class="card-icon">📋</span>
                <h3 class="card-title">Единая База 62 Предприятий</h3>
                <p class="card-desc">Полный реестр целевых заводов, комбинатов, девелоперов, клиник и ресторанов Синячихи, Алапаевска и Екатеринбурга. Точные ЛПР, выявленные боли, готовые питчи и прикрепленные шаблоны сайтов.</p>
            </div>
            <a href="Leads_List.html" class="btn-card">
                <span>Открыть Базу Лидов (62 компании)</span>
                <span>&rarr;</span>
            </a>
        </div>

        <!-- КАРТОЧКА 2: ШАБЛОНЫ САЙТОВ GLOBAL PLUS -->
        <div class="hub-card templates">
            <div>
                <span class="card-icon">🔥</span>
                <h3 class="card-title">Каталог Шаблонов Global Plus <span class="badge-hot">15 РЕШЕНИЙ</span></h3>
                <p class="card-desc">Реальные кинематографичные сайты с видеофоном, скроллом и формами по отраслям (Медицина, Детейлинг, Девелопмент, HoReCa, Гео-карты, Заводы). Открывай на планшете перед директорами.</p>
            </div>
            <a href="Templates_Catalog.html" class="btn-card">
                <span>Смотреть 15 Шаблонов Сайтов</span>
                <span>&rarr;</span>
            </a>
        </div>

        <!-- КАРТОЧКА: ИНТЕРАКТИВНАЯ ПРЕЗЕНТАЦИЯ (PITCH DECK) -->
        <div class="hub-card deck-card" style="--card-accent: #C5A059;">
            <div>
                <span class="card-icon">📊</span>
                <h3 class="card-title">Интерактивный Pitch Deck <span class="badge-hot">ДЛЯ IPAD</span></h3>
                <p class="card-desc">Динамическая презентация со скроллом, анимацией и видеофоном под любую компанию из 62 в базе. Полноэкранный показ 4 ключевых слайдов на встречах с уральскими директорами.</p>
            </div>
            <a href="Dynamic_Pitch_Deck.html?id=sveza-vs" class="btn-card">
                <span>Запустить Интерактивные Слайды</span>
                <span>&rarr;</span>
            </a>
        </div>

        <!-- КАРТОЧКА: ДИНАМИЧЕСКИЙ 1-PAGER (КП ДЛЯ ПЕЧАТИ) -->
        <div class="hub-card pager-card" style="--card-accent: #10B981;">
            <div>
                <span class="card-icon">📄</span>
                <h3 class="card-title">Динамический 1-Pager (А4) <span class="badge-hot">В РУКИ</span></h3>
                <p class="card-desc">Готовый стратегический меморандум под каждую компанию: боли, решение за 48 часов, 3 фазы цен и расчет ROI. Готов к распечатке на А4 или отправке в PDF директору в руки.</p>
            </div>
            <a href="Dynamic_One_Pager.html?id=sveza-vs" class="btn-card">
                <span>Открыть Одностраничник А4</span>
                <span>&rarr;</span>
            </a>
        </div>

        <!-- КАРТОЧКА 3: ПЛЕЙБУК ДИМЫ -->
        <div class="hub-card strategy">
            <div>
                <span class="card-icon">🐺</span>
                <h3 class="card-title">Плейбук Димы: Стратегия На Земле <span class="badge-hot">ОСНОВА</span></h3>
                <p class="card-desc">Пошаговое руководство регионального представителя Global Plus. Позиционирование, 3-шаговая модель захода к уральским директорам, работа с планшетом на встречах, регламент 4-недельного спринта.</p>
            </div>
            <a href="Solo_Executive_Strategy.html" class="btn-card">
                <span>Изучить Плейбук Партнера</span>
                <span>&rarr;</span>
            </a>
        </div>

        <!-- КАРТОЧКА 4: БЫСТРЫЕ СКРИПТЫ -->
        <div class="hub-card scripts">
            <div>
                <span class="card-icon">🚀</span>
                <h3 class="card-title">Быстрые Скрипты &amp; Заходы</h3>
                <p class="card-desc">Боевые скрипты звонков директорам, шаблоны WhatsApp/Telegram, обход секретарей заводов, сценарий 30-секундного показа на iPad, закрытие 10 ключевых возражений уральского бизнеса.</p>
            </div>
            <a href="Fast_Collab_Pitches.html" class="btn-card">
                <span>Открыть Скрипты и Питчи</span>
                <span>&rarr;</span>
            </a>
        </div>

        <!-- КАРТОЧКА 5: 62 ПИТЧА И ЦЕНЫ -->
        <div class="hub-card pitches">
            <div>
                <span class="card-icon">🔍</span>
                <h3 class="card-title">Каталог 62 КП и Расценки</h3>
                <p class="card-desc">Детальный каталог коммерческих предложений с прайс-листами внедрения, ежемесячной абонентской платой (Retainer) и обоснованием окупаемости (ROI) под каждую сферу деятельности.</p>
            </div>
            <a href="Comprehensive_Pitches.html" class="btn-card">
                <span>Смотреть Все 62 Оффера</span>
                <span>&rarr;</span>
            </a>
        </div>

        <!-- КАРТОЧКА 6: СТРАТЕГИЯ БРЕНДОВ -->
        <div class="hub-card brand">
            <div>
                <span class="card-icon">👑</span>
                <h3 class="card-title">Синергия Двойного Бренда</h3>
                <p class="card-desc">Как Диме использовать мощь связки «Глобал Плюс» (надежный уральский интегратор на месте) и «GlobalTeamPartners» (международные IT-стандарты и передовые нейросети).</p>
            </div>
            <a href="Exclusive_Strategy.html" class="btn-card">
                <span>Стратегия Позиционирования</span>
                <span>&rarr;</span>
            </a>
        </div>

        <!-- КАРТОЧКА 7: АНАЛИЗ РЫНКА -->
        <div class="hub-card intel">
            <div>
                <span class="card-icon">🧠</span>
                <h3 class="card-title">Разведка Рынка Урала</h3>
                <p class="card-desc">Глубокий анализ бизнес-ландшафта Свердловской области: лесной кластер Синячихи, машиностроение Алапаевска, высококонкурентные премиум-рынки Екатеринбурга.</p>
            </div>
            <a href="Market_Intelligence.html" class="btn-card">
                <span>Аналитический Отчет</span>
                <span>&rarr;</span>
            </a>
        </div>

    </div>

        <!-- ГОТОВЫЕ ИНТЕРАКТИВНЫЕ ДЕМО-ОБРАЗЦЫ & ШАБЛОНЫ САЙТОВ -->
    <h2 class="section-heading">🌐 Живые Сайты &amp; Демо-Прототипы Для Встреч</h2>
    <p style="color: var(--text-dim); margin-top: -15px; margin-bottom: 25px;">Открывай прямо со смартфона или планшета перед директором — покажи уровень визуализации и B2B-функционал за 30 секунд.</p>

    <div class="demo-grid">

        <div class="demo-card">
            <div class="demo-thumb"><video src="assets/videos/wood.mp4" muted loop playsinline preload="metadata"></video><div class="demo-thumb-overlay"></div></div>
            <div class="demo-content">
            <div class="demo-title">🌲 Лесопромышленный B2B-Портал</div>
            <div class="demo-subtitle">СВЕЗА, Лестех, АДОЗ, АЛХ — калькулятор вагонных партий фанеры и леса по ГОСТ</div>
            <a href="demos/wood-industry-demo/index.html" class="demo-link" target="_blank">
                <span>Открыть Калькулятор Фанеры</span>
                <span>&nearr;</span>
            </a>
            </div>
        </div>
<div class="demo-card">
            <div class="demo-thumb"><video src="assets/videos/machinery.mp4" muted loop playsinline preload="metadata"></video><div class="demo-thumb-overlay"></div></div>
            <div class="demo-content">
            <div class="demo-title">🏭 Завод Металлоконструкций ЗКСК</div>
            <div class="demo-subtitle">ВСЗ, Уралмаш, Стройдормаш — 3D-каркасы цехов, ангаров и расчет металлоемкости</div>
            <a href="https://globalteamgroup.github.io/zksk-sample/" class="demo-link" target="_blank">
                <span>Открыть Сайт Завода ЗКСК</span>
                <span>&nearr;</span>
            </a>
            </div>
        </div>
<div class="demo-card">
            <div class="demo-thumb"><video src="assets/videos/machinery.mp4" muted loop playsinline preload="metadata"></video><div class="demo-thumb-overlay"></div></div>
            <div class="demo-content">
            <div class="demo-title">⚙️ Спецтехника &amp; Машиностроение</div>
            <div class="demo-subtitle">Стройдормаш, ЗИСТ, PSM — 3D-конфигуратор бурилок и подбор гидромоторов</div>
            <a href="demos/machinery-demo/index.html" class="demo-link" target="_blank">
                <span>Открыть 3D-Конфигуратор</span>
                <span>&nearr;</span>
            </a>
            </div>
        </div>
<div class="demo-card">
            <div class="demo-thumb"><video src="assets/videos/stroyka.mp4" muted loop playsinline preload="metadata"></video><div class="demo-thumb-overlay"></div></div>
            <div class="demo-content">
            <div class="demo-title">🏗️ Строительство &amp; Генподряд</div>
            <div class="demo-subtitle">Алапаевск-Строй, Атомстройкомплекс, Брусника — СРО, парк техники и сметы</div>
            <a href="https://globalteamgroup.github.io/stroyka-pro/" class="demo-link" target="_blank">
                <span>Открыть Сайт «Стройка-Про»</span>
                <span>&nearr;</span>
            </a>
            </div>
        </div>
<div class="demo-card">
            <div class="demo-thumb"><video src="assets/videos/estate.mp4" muted loop playsinline preload="metadata"></video><div class="demo-thumb-overlay"></div></div>
            <div class="demo-content">
            <div class="demo-title">🏙️ Девелопмент &amp; Клубные Дома</div>
            <div class="demo-subtitle">Брусника, УГМК-Застройщик, Forum Group — интерактивный генплан и 3D-резиденции</div>
            <a href="https://globalteamgroup.github.io/luxury-estate-sample/" class="demo-link" target="_blank">
                <span>Открыть Сайт Luxury Estate</span>
                <span>&nearr;</span>
            </a>
            </div>
        </div>
<div class="demo-card">
            <div class="demo-thumb"><video src="assets/videos/clinic.mp4" muted loop playsinline preload="metadata"></video><div class="demo-thumb-overlay"></div></div>
            <div class="demo-content">
            <div class="demo-title">💉 Медицинский Центр «Клиника Европа»</div>
            <div class="demo-subtitle">УГМК-Здоровье, Здоровье 365, Парацельс — видеоряд клиники и онлайн-запись к врачам</div>
            <a href="https://globalteamgroup.github.io/europa-clinic/" class="demo-link" target="_blank">
                <span>Открыть Сайт «Клиника Европа»</span>
                <span>&nearr;</span>
            </a>
            </div>
        </div>
<div class="demo-card">
            <div class="demo-thumb"><video src="assets/videos/dental.mp4" muted loop playsinline preload="metadata"></video><div class="demo-thumb-overlay"></div></div>
            <div class="demo-content">
            <div class="demo-title">🦷 Стоматология &amp; Эстетика «Люмьер»</div>
            <div class="demo-subtitle">Мегадента Клиник, Нудельман — 3D-моделирование улыбок и планы лечения</div>
            <a href="https://globalteamgroup.github.io/lumiere-clinic-sample/" class="demo-link" target="_blank">
                <span>Открыть Сайт Клиники «Люмьер»</span>
                <span>&nearr;</span>
            </a>
            </div>
        </div>
<div class="demo-card">
            <div class="demo-thumb"><video src="assets/videos/auto.mp4" muted loop playsinline preload="metadata"></video><div class="demo-thumb-overlay"></div></div>
            <div class="demo-content">
            <div class="demo-title">🏎️ Автоуход &amp; Детейлинг «Elite Detailing»</div>
            <div class="demo-subtitle">Detailing Alarm, Порше Центр, Автобан — 60fps скролл авто и бронепленка</div>
            <a href="https://globalteamgroup.github.io/elite-detailing/" class="demo-link" target="_blank">
                <span>Открыть Сайт Elite Detailing</span>
                <span>&nearr;</span>
            </a>
            </div>
        </div>
<div class="demo-card">
            <div class="demo-thumb"><video src="assets/videos/auto.mp4" muted loop playsinline preload="metadata"></video><div class="demo-thumb-overlay"></div></div>
            <div class="demo-content">
            <div class="demo-title">🚜 Сервис Спецтехники &amp; Автоколонн</div>
            <div class="demo-subtitle">СТО Синячихи, автобазы лесовозов — вызов мобильного механика и заказ запчастей</div>
            <a href="demos/service-demo/index.html" class="demo-link" target="_blank">
                <span>Открыть Сервисный Портал</span>
                <span>&nearr;</span>
            </a>
            </div>
        </div>
<div class="demo-card">
            <div class="demo-thumb"><video src="assets/videos/horeca.mp4" muted loop playsinline preload="metadata"></video><div class="demo-thumb-overlay"></div></div>
            <div class="demo-content">
            <div class="demo-title">🏨 Загородный Курорт &amp; Спа «HoReCa Grand»</div>
            <div class="demo-subtitle">Отель Эрмитаж, Металлург, Высоцкий, Чистые пруды — видеоряд курорта и бронь номеров</div>
            <a href="https://globalteamgroup.github.io/horeca-grand-sample/" class="demo-link" target="_blank">
                <span>Открыть Сайт HoReCa Grand</span>
                <span>&nearr;</span>
            </a>
            </div>
        </div>
<div class="demo-card">
            <div class="demo-thumb"><video src="assets/videos/horeca.mp4" muted loop playsinline preload="metadata"></video><div class="demo-thumb-overlay"></div></div>
            <div class="demo-content">
            <div class="demo-title">🍷 Ресторан Авторской Кухни &amp; Банкеты</div>
            <div class="demo-subtitle">Троекуровъ, Kitchen, Сойка, Гастроли — интерактивная карта столов и депозиты</div>
            <a href="demos/horeca-demo/index.html" class="demo-link" target="_blank">
                <span>Открыть Ресторанное Демо</span>
                <span>&nearr;</span>
            </a>
            </div>
        </div>
<div class="demo-card">
            <div class="demo-thumb"><video src="assets/videos/agro.mp4" muted loop playsinline preload="metadata"></video><div class="demo-thumb-overlay"></div></div>
            <div class="demo-content">
            <div class="demo-title">📍 Геоточка &amp; Ритейл</div>
            <div class="demo-subtitle">Талицкое молоко, СМАК, Черкашин — карта точек на Яндекс Картах</div>
            <a href="https://globalteampartners.github.io/geotochka/" class="demo-link" target="_blank">
                <span>Открыть Сайт Геоточка</span>
                <span>&nearr;</span>
            </a>
            </div>
        </div>
<div class="demo-card">
            <div class="demo-thumb"><video src="assets/videos/agro.mp4" muted loop playsinline preload="metadata"></video><div class="demo-thumb-overlay"></div></div>
            <div class="demo-content">
            <div class="demo-title">🏭 Заводы &amp; Дистрибуция «Тенториум»</div>
            <div class="demo-subtitle">Птицефабрика, АМК, Alma Ceramica — 3D-презентация цеха и B2B-дистрибуция</div>
            <a href="https://globalteampartners.github.io/tentorium-presentation/" class="demo-link" target="_blank">
                <span>Открыть Сайт Тенториум</span>
                <span>&nearr;</span>
            </a>
            </div>
        </div>
<div class="demo-card">
            <div class="demo-thumb"><video src="assets/videos/tourism.mp4" muted loop playsinline preload="metadata"></video><div class="demo-thumb-overlay"></div></div>
            <div class="demo-content">
            <div class="demo-title">🚂 Туризм &amp; АУЖД Урала</div>
            <div class="demo-subtitle">АУЖД, Музей Синячихи, отели — интерактивная продажа турпакетов и билетов</div>
            <a href="https://globalteamgroup.github.io/tourism-sample/" class="demo-link" target="_blank">
                <span>Открыть Туристический Портал</span>
                <span>&nearr;</span>
            </a>
            </div>
        </div>
<div class="demo-card">
            <div class="demo-thumb"><video src="assets/videos/machinery.mp4" muted loop playsinline preload="metadata"></video><div class="demo-thumb-overlay"></div></div>
            <div class="demo-content">
            <div class="demo-title">🌐 Global Plus | Шоурил (globalplus.tech)</div>
            <div class="demo-subtitle">Официальный презентационный портал агентства — разработка B2B-систем за 48 часов</div>
            <a href="https://globalteamgroup.github.io/global-plus/" class="demo-link" target="_blank">
                <span>Открыть Сайт Global Plus</span>
                <span>&nearr;</span>
            </a>
            </div>
        </div>
</div></div>

</div>

<footer>
    <p>&copy; 2026 Глобал Плюс &times; Global Team Partners. Конфиденциальный комплект регионального развития.</p>
    <p style="margin-top: 8px; opacity: 0.7;">Разработано для стратегического партнера в Свердловской области (Верхняя Синячиха &bull; Алапаевск &bull; Екатеринбург).</p>
</footer>

<script>
    // Автовоспроизведение превью-видео при появлении в зоне видимости
    const thumbs = document.querySelectorAll('.demo-thumb video');
    if ('IntersectionObserver' in window) {{
        const obs = new IntersectionObserver((entries) => {{
            entries.forEach(entry => {{
                const v = entry.target;
                if (entry.isIntersecting) {{
                    v.muted = true;
                    v.defaultMuted = true;
                    v.play().catch(() => {{}});
                }} else {{
                    v.pause();
                }}
            }});
        }}, {{ threshold: 0.25 }});
        thumbs.forEach(v => obs.observe(v));
    }}
</script>

</body>
</html>
"""

with open(os.path.join(WORKSPACE, "index.html"), "w", encoding="utf-8") as f:
    f.write(index_html)
print("index.html успешно обновлен!")

# ------------------------------------------------------------------------------
# 3. ГЕНЕРАЦИЯ Leads_List.html (с кнопкой быстрого перехода к шаблону сайта)
# ------------------------------------------------------------------------------
leads_rows = []
for c in COMPANIES:
    row = f"""
    <tr data-region="{c['region']}" data-sector="{c['sector']}" data-id="{c['id']}">
        <td>
            <strong>{c['name']}</strong><br>
            <span style="font-size:0.8rem; color:#94A3B8;">{c['focus']}</span>
        </td>
        <td><span class="region-pill">{c['region']}</span></td>
        <td><span class="badge {c['badge_class']}">{c['sector']}</span></td>
        <td><span class="persona-tag">{c['target_persona']}</span></td>
        <td style="font-size:0.85rem; color:#E2E8F0;">
            {c['trojan_pitch']}
            <div style="margin-top:6px; font-size:0.8rem; color:#C5A059;">
                <strong>Шаблон сайта:</strong> <a href="{c['template_url']}" target="_blank" style="color:#E0C07A; text-decoration:underline;">{c['template_name']}</a>
            </div>
        </td>
        <td style="white-space:nowrap;">
            <a href="Dynamic_Pitch_Deck.html?id={c['id']}" target="_blank" class="btn-action btn-deck" title="Открыть интерактивную презентацию">📊 Слайды</a>
            <a href="Dynamic_One_Pager.html?id={c['id']}" target="_blank" class="btn-action btn-pager" title="Открыть КП-одностраничник">📄 1-Pager</a>
            <a href="{c['template_url']}" target="_blank" class="btn-action btn-tpl" title="Открыть живой шаблон сайта Global Plus">🌐 Шаблон</a>
        </td>
    </tr>
    """
    leads_rows.append(row)

leads_html = f"""<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>База 62 Целевых Предприятий | Глобал Плюс</title>
    <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;700&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
    <style>
        :root {{
            --bg-base: #0B0E14;
            --bg-surface: #121721;
            --bg-card: #18202E;
            --gold: #C5A059;
            --gold-light: #E0C07A;
            --red: #D32F2F;
            --green: #10B981;
            --white: #F8FAFC;
            --text-dim: #94A3B8;
            --border: rgba(197, 160, 89, 0.2);
            --border-card: rgba(255, 255, 255, 0.08);
        }}
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{
            background-color: var(--bg-base);
            color: var(--white);
            font-family: 'Inter', sans-serif;
            padding: 30px 20px;
            line-height: 1.5;
        }}
        .top-nav {{
            max-width: 1350px;
            margin: 0 auto 24px;
            display: flex;
            align-items: center;
            justify-content: space-between;
        }}
        .btn-back {{
            display: inline-flex;
            align-items: center;
            gap: 8px;
            background: rgba(255, 255, 255, 0.05);
            border: 1px solid var(--border-card);
            color: var(--gold);
            padding: 8px 18px;
            border-radius: 6px;
            text-decoration: none;
            font-weight: 600;
            font-size: 0.9rem;
            transition: all 0.2s;
        }}
        .btn-back:hover {{
            background: var(--gold);
            color: #000;
        }}
        .container {{
            max-width: 1350px;
            margin: 0 auto;
        }}
        h1 {{
            font-family: 'Playfair Display', serif;
            color: var(--gold);
            font-size: 2.2rem;
            margin-bottom: 8px;
        }}
        p.subtitle {{
            color: var(--text-dim);
            font-size: 1rem;
            margin-bottom: 24px;
        }}

        /* ФИЛЬТРЫ И ПОИСК */
        .controls-panel {{
            background: var(--bg-surface);
            border: 1px solid var(--border-card);
            border-radius: 12px;
            padding: 20px;
            margin-bottom: 24px;
            display: flex;
            flex-direction: column;
            gap: 16px;
        }}
        .search-box input {{
            width: 100%;
            background: rgba(0, 0, 0, 0.4);
            border: 1px solid var(--border-card);
            padding: 12px 18px;
            border-radius: 8px;
            color: #fff;
            font-size: 1rem;
            outline: none;
            transition: border-color 0.2s;
        }}
        .search-box input:focus {{
            border-color: var(--gold);
        }}
        .filter-group {{
            display: flex;
            align-items: center;
            gap: 10px;
            flex-wrap: wrap;
        }}
        .filter-label {{
            font-size: 0.85rem;
            font-weight: 600;
            color: var(--gold);
            min-width: 90px;
        }}
        .filter-btn {{
            background: rgba(255, 255, 255, 0.05);
            border: 1px solid var(--border-card);
            color: var(--text-dim);
            padding: 6px 14px;
            border-radius: 20px;
            font-size: 0.8rem;
            cursor: pointer;
            transition: all 0.2s;
        }}
        .filter-btn:hover, .filter-btn.active {{
            background: var(--gold);
            color: #000;
            border-color: var(--gold);
            font-weight: 600;
        }}

        /* ТАБЛИЦА */
        .table-responsive {{
            background: var(--bg-surface);
            border: 1px solid var(--border-card);
            border-radius: 12px;
            overflow-x: auto;
        }}
        table {{
            width: 100%;
            border-collapse: collapse;
            text-align: left;
        }}
        th, td {{
            padding: 16px 18px;
            border-bottom: 1px solid var(--border-card);
            font-size: 0.9rem;
            vertical-align: top;
        }}
        th {{
            background: #18202E;
            color: var(--gold);
            font-weight: 600;
            text-transform: uppercase;
            font-size: 0.75rem;
            letter-spacing: 1px;
        }}
        tr:hover td {{
            background: rgba(255, 255, 255, 0.02);
        }}
        .badge {{
            display: inline-block;
            padding: 4px 10px;
            border-radius: 12px;
            font-size: 0.75rem;
            font-weight: 600;
        }}
        .bg-wood {{ background: rgba(34, 197, 94, 0.15); color: #4ADE80; border: 1px solid rgba(34, 197, 94, 0.3); }}
        .bg-machine {{ background: rgba(59, 130, 246, 0.15); color: #60A5FA; border: 1px solid rgba(59, 130, 246, 0.3); }}
        .bg-realestate {{ background: rgba(234, 179, 8, 0.15); color: #FACC15; border: 1px solid rgba(234, 179, 8, 0.3); }}
        .bg-horeca {{ background: rgba(236, 72, 153, 0.15); color: #F472B6; border: 1px solid rgba(236, 72, 153, 0.3); }}
        .bg-medical {{ background: rgba(168, 85, 247, 0.15); color: #C084FC; border: 1px solid rgba(168, 85, 247, 0.3); }}
        .bg-auto {{ background: rgba(249, 115, 22, 0.15); color: #FB923C; border: 1px solid rgba(249, 115, 22, 0.3); }}
        .bg-food {{ background: rgba(20, 184, 166, 0.15); color: #2DD4BF; border: 1px solid rgba(20, 184, 166, 0.3); }}
        .bg-service {{ background: rgba(148, 163, 184, 0.15); color: #CBD5E1; border: 1px solid rgba(148, 163, 184, 0.3); }}

        .region-pill {{
            font-size: 0.75rem;
            color: var(--text-dim);
            background: rgba(255, 255, 255, 0.05);
            padding: 3px 8px;
            border-radius: 4px;
            display: inline-block;
        }}
        .persona-tag {{
            font-size: 0.8rem;
            color: #E2E8F0;
            font-weight: 500;
        }}

        .btn-action {{
            display: inline-flex;
            align-items: center;
            gap: 4px;
            padding: 6px 10px;
            border-radius: 6px;
            text-decoration: none;
            font-size: 0.75rem;
            font-weight: 600;
            margin-right: 4px;
            margin-bottom: 4px;
            transition: all 0.2s;
        }}
        .btn-deck {{
            background: var(--gold);
            color: #000;
        }}
        .btn-deck:hover {{
            background: var(--gold-light);
        }}
        .btn-pager {{
            background: rgba(255, 255, 255, 0.08);
            border: 1px solid var(--border-card);
            color: #fff;
        }}
        .btn-pager:hover {{
            background: #fff;
            color: #000;
        }}
        .btn-tpl {{
            background: rgba(16, 185, 129, 0.15);
            border: 1px solid rgba(16, 185, 129, 0.4);
            color: #6EE7B7;
        }}
        .btn-tpl:hover {{
            background: var(--green);
            color: #000;
        }}
    </style>
</head>
<body>

<div class="top-nav">
    <a href="index.html" class="btn-back">&larr; Вернуться в Центр Продаж</a>
    <div style="font-size: 0.85rem; color: var(--gold);">Региональный охват: 62 ключевых предприятия &bull; 15 шаблонов сайтов</div>
</div>

<div class="container">
    <h1>📋 Единая База 62 Целевых Предприятий</h1>
    <p class="subtitle">Верхняя Синячиха &bull; Алапаевск &bull; Екатеринбург | Готовые точки входа, ЛПР, презентации и прикрепленные шаблоны сайтов Global Plus</p>

    <!-- ПАНЕЛЬ ПОИСКА И ФИЛЬТРАЦИИ -->
    <div class="controls-panel">
        <div class="search-box">
            <input type="text" id="searchInput" placeholder="🔍 Быстрый поиск по названию, специализации, ЛПР или шаблону сайта...">
        </div>
        
        <div class="filter-group">
            <span class="filter-label">Локация:</span>
            <button class="filter-btn active" data-filter="all-region">Все локации (62)</button>
            <button class="filter-btn" data-filter="Верхняя Синячиха">Верхняя Синячиха (8)</button>
            <button class="filter-btn" data-filter="Алапаевск и район">Алапаевск и район (16)</button>
            <button class="filter-btn" data-filter="Екатеринбург">Екатеринбург (38)</button>
        </div>

        <div class="filter-group">
            <span class="filter-label">Отрасль:</span>
            <button class="filter-btn active" data-sector="all-sector">Все отрасли</button>
            <button class="filter-btn" data-sector="Лесопромышленность & Деревообработка">Деревообработка & Лес</button>
            <button class="filter-btn" data-sector="Машиностроение & Металл">Машиностроение & Металл</button>
            <button class="filter-btn" data-sector="Девелопмент & Недвижимость">Девелопмент</button>
            <button class="filter-btn" data-sector="HoReCa & Отели">HoReCa & Отели</button>
            <button class="filter-btn" data-sector="Медицина & Эстетика">Медицина</button>
            <button class="filter-btn" data-sector="Авто & Детейлинг">Авто & Спецтехника</button>
            <button class="filter-btn" data-sector="Пищепром & Агро">Пищепром & Агро</button>
            <button class="filter-btn" data-sector="Туризм, Спорт & Услуги">Туризм & Сервисы</button>
        </div>
    </div>

    <!-- ТАБЛИЦА БАЗЫ ДАННЫХ -->
    <div class="table-responsive">
        <table id="leadsTable">
            <thead>
                <tr>
                    <th style="min-width: 220px;">Предприятие / Бренд</th>
                    <th>Локация</th>
                    <th>Отрасль</th>
                    <th>Целевое ЛПР</th>
                    <th style="min-width: 280px;">Питч "Троянского коня" & Шаблон Сайта</th>
                    <th style="min-width: 210px;">Инструменты Димы</th>
                </tr>
            </thead>
            <tbody>
                {''.join(leads_rows)}
            </tbody>
        </table>
    </div>
</div>

<script>
    const searchInput = document.getElementById('searchInput');
    const rows = document.querySelectorAll('#leadsTable tbody tr');
    let currentRegion = 'all-region';
    let currentSector = 'all-sector';

    function filterTable() {{
        const query = searchInput.value.toLowerCase().trim();

        rows.forEach(row => {{
            const rowText = row.innerText.toLowerCase();
            const rowRegion = row.getAttribute('data-region');
            const rowSector = row.getAttribute('data-sector');

            const matchesSearch = !query || rowText.includes(query);
            const matchesRegion = (currentRegion === 'all-region') || (rowRegion === currentRegion);
            const matchesSector = (currentSector === 'all-sector') || (rowSector === currentSector);

            if (matchesSearch && matchesRegion && matchesSector) {{
                row.style.display = '';
            }} else {{
                row.style.display = 'none';
            }}
        }});
    }}

    searchInput.addEventListener('input', filterTable);

    document.querySelectorAll('[data-filter]').forEach(btn => {{
        btn.addEventListener('click', () => {{
            document.querySelectorAll('[data-filter]').forEach(b => b.classList.remove('active'));
            btn.classList.add('active');
            currentRegion = btn.getAttribute('data-filter');
            filterTable();
        }});
    }});

    document.querySelectorAll('[data-sector]').forEach(btn => {{
        btn.addEventListener('click', () => {{
            document.querySelectorAll('[data-sector]').forEach(b => b.classList.remove('active'));
            btn.classList.add('active');
            currentSector = btn.getAttribute('data-sector');
            filterTable();
        }});
    }});
</script>

</body>
</html>
"""

with open(os.path.join(WORKSPACE, "Leads_List.html"), "w", encoding="utf-8") as f:
    f.write(leads_html)
print("Leads_List.html успешно обновлен с кнопками шаблонов!")

# ------------------------------------------------------------------------------
# 4. ГЕНЕРАЦИЯ Comprehensive_Pitches.html (с блоком шаблона в каждой карточке)
# ------------------------------------------------------------------------------
cards_pitches = []
for c in COMPANIES:
    card = f"""
    <div class="pitch-card" data-sector="{c['sector']}">
        <div class="pitch-header">
            <div>
                <span class="region-tag">{c['region']}</span>
                <span class="badge {c['badge_class']}">{c['sector']}</span>
                <h3 style="font-family:'Playfair Display',serif; font-size:1.5rem; margin-top:8px; color:#fff;">{c['name']}</h3>
                <p style="color:#94A3B8; font-size:0.9rem;">{c['focus']}</p>
            </div>
            <div style="text-align:right;">
                <div style="font-size:0.8rem; color:var(--text-dim);">ПАКЕТ ВНЕДРЕНИЯ (SETUP)</div>
                <div style="font-family:'Playfair Display',serif; font-size:1.8rem; color:var(--gold); font-weight:700;">{c['price_setup']}</div>
                <div style="font-size:0.85rem; color:#10B981;">Абонентка: <strong>{c['price_retainer']}</strong></div>
            </div>
        </div>

        <div class="pitch-grid">
            <div class="pitch-box">
                <h4>🎯 Целевое ЛПР на переговорах</h4>
                <p>{c['target_persona']}</p>
            </div>
            <div class="pitch-box">
                <h4>⚠️ Выявленная боль и потери предприятия</h4>
                <p style="color:#FCA5A5;">{c['pain_point']}</p>
            </div>
        </div>

        <div class="pitch-solution">
            <h4>💡 Оффер "Троянского коня" (Быстрый запуск за 48 часов)</h4>
            <p>{c['trojan_pitch']}</p>
        </div>

        <!-- РЕКОМЕНДУЕМЫЙ ШАБЛОН САЙТА GLOBAL PLUS -->
        <div class="template-box">
            <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:10px; margin-bottom:8px;">
                <span class="tpl-tag">🌐 РЕКОМЕНДУЕМЫЙ ШАБЛОН САЙТА (GLOBAL PLUS):</span>
                <a href="{c['template_url']}" target="_blank" class="btn-live-link">Открыть сайт ↗</a>
            </div>
            <div style="font-weight:600; color:#F8FAFC; margin-bottom:4px;">{c['template_name']}</div>
            <div style="font-size:0.85rem; color:#94A3B8;">{c['template_desc']}</div>
        </div>

        <div class="pitch-roi">
            <strong>📈 Обоснование окупаемости (ROI):</strong> {c['roi_desc']}
        </div>

        <div class="pitch-actions">
            <a href="Dynamic_Pitch_Deck.html?id={c['id']}" target="_blank" class="btn-deck">📊 Открыть интерактивную презентацию</a>
            <a href="Dynamic_One_Pager.html?id={c['id']}" target="_blank" class="btn-pager">📄 Печать 1-Pager (А4)</a>
            <a href="{c['template_url']}" target="_blank" class="btn-tpl-card">🌐 Тестировать сайт клиента</a>
        </div>
    </div>
    """
    cards_pitches.append(card)

comprehensive_html = f"""<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>62 Коммерческих Предложения & Расценки | Глобал Плюс</title>
    <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;700&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
    <style>
        :root {{
            --bg-base: #0B0E14;
            --bg-surface: #121721;
            --bg-card: #18202E;
            --gold: #C5A059;
            --gold-light: #E0C07A;
            --red: #D32F2F;
            --green: #10B981;
            --white: #F8FAFC;
            --text-dim: #94A3B8;
            --border: rgba(197, 160, 89, 0.2);
            --border-card: rgba(255, 255, 255, 0.08);
        }}
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{
            background-color: var(--bg-base);
            color: var(--white);
            font-family: 'Inter', sans-serif;
            padding: 40px 20px;
            line-height: 1.6;
        }}
        .top-nav {{
            max-width: 1200px;
            margin: 0 auto 30px;
            display: flex;
            align-items: center;
            justify-content: space-between;
        }}
        .btn-back {{
            display: inline-flex;
            align-items: center;
            gap: 8px;
            background: rgba(255, 255, 255, 0.05);
            border: 1px solid var(--border-card);
            color: var(--gold);
            padding: 8px 18px;
            border-radius: 6px;
            text-decoration: none;
            font-weight: 600;
            font-size: 0.9rem;
            transition: all 0.2s;
        }}
        .btn-back:hover {{
            background: var(--gold);
            color: #000;
        }}
        .container {{
            max-width: 1200px;
            margin: 0 auto;
        }}
        h1 {{
            font-family: 'Playfair Display', serif;
            color: var(--gold);
            font-size: 2.3rem;
            margin-bottom: 8px;
        }}
        p.subtitle {{
            color: var(--text-dim);
            font-size: 1.05rem;
            margin-bottom: 35px;
        }}
        
        .pitches-list {{
            display: flex;
            flex-direction: column;
            gap: 24px;
        }}
        .pitch-card {{
            background: var(--bg-surface);
            border: 1px solid var(--border-card);
            border-radius: 14px;
            padding: 28px;
            transition: all 0.3s;
            position: relative;
        }}
        .pitch-card:hover {{
            border-color: var(--gold);
            box-shadow: 0 10px 25px rgba(0,0,0,0.3);
        }}
        .pitch-header {{
            display: flex;
            justify-content: space-between;
            align-items: flex-start;
            flex-wrap: wrap;
            gap: 16px;
            border-bottom: 1px solid var(--border-card);
            padding-bottom: 18px;
            margin-bottom: 18px;
        }}
        .region-tag {{
            background: rgba(255, 255, 255, 0.08);
            color: #fff;
            padding: 3px 10px;
            border-radius: 4px;
            font-size: 0.75rem;
            font-weight: 600;
            display: inline-block;
            margin-right: 8px;
        }}
        .badge {{
            display: inline-block;
            padding: 4px 10px;
            border-radius: 12px;
            font-size: 0.75rem;
            font-weight: 600;
        }}
        .bg-wood {{ background: rgba(34, 197, 94, 0.15); color: #4ADE80; border: 1px solid rgba(34, 197, 94, 0.3); }}
        .bg-machine {{ background: rgba(59, 130, 246, 0.15); color: #60A5FA; border: 1px solid rgba(59, 130, 246, 0.3); }}
        .bg-realestate {{ background: rgba(234, 179, 8, 0.15); color: #FACC15; border: 1px solid rgba(234, 179, 8, 0.3); }}
        .bg-horeca {{ background: rgba(236, 72, 153, 0.15); color: #F472B6; border: 1px solid rgba(236, 72, 153, 0.3); }}
        .bg-medical {{ background: rgba(168, 85, 247, 0.15); color: #C084FC; border: 1px solid rgba(168, 85, 247, 0.3); }}
        .bg-auto {{ background: rgba(249, 115, 22, 0.15); color: #FB923C; border: 1px solid rgba(249, 115, 22, 0.3); }}
        .bg-food {{ background: rgba(20, 184, 166, 0.15); color: #2DD4BF; border: 1px solid rgba(20, 184, 166, 0.3); }}
        .bg-service {{ background: rgba(148, 163, 184, 0.15); color: #CBD5E1; border: 1px solid rgba(148, 163, 184, 0.3); }}

        .pitch-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 16px;
            margin-bottom: 16px;
        }}
        .pitch-box {{
            background: rgba(0, 0, 0, 0.25);
            padding: 16px;
            border-radius: 8px;
            border: 1px solid var(--border-card);
        }}
        .pitch-box h4 {{
            font-size: 0.85rem;
            color: var(--gold);
            margin-bottom: 8px;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }}
        .pitch-box p {{
            font-size: 0.9rem;
            color: #E2E8F0;
        }}
        .pitch-solution {{
            background: rgba(197, 160, 89, 0.08);
            border-left: 4px solid var(--gold);
            padding: 14px 18px;
            border-radius: 0 8px 8px 0;
            margin-bottom: 16px;
        }}
        .pitch-solution h4 {{
            font-size: 0.85rem;
            color: var(--gold-light);
            margin-bottom: 6px;
            text-transform: uppercase;
        }}
        .pitch-solution p {{
            font-size: 0.95rem;
            color: #fff;
            font-weight: 500;
        }}

        .template-box {{
            background: rgba(16, 185, 129, 0.08);
            border: 1px solid rgba(16, 185, 129, 0.3);
            border-radius: 8px;
            padding: 14px 18px;
            margin-bottom: 16px;
        }}
        .tpl-tag {{
            font-size: 0.75rem;
            font-weight: 700;
            color: #10B981;
            letter-spacing: 1px;
        }}
        .btn-live-link {{
            color: #6EE7B7;
            font-size: 0.8rem;
            text-decoration: underline;
            font-weight: 600;
        }}

        .pitch-roi {{
            font-size: 0.9rem;
            color: #34D399;
            background: rgba(16, 185, 129, 0.1);
            padding: 10px 14px;
            border-radius: 6px;
            margin-bottom: 18px;
        }}
        .pitch-actions {{
            display: flex;
            gap: 12px;
            flex-wrap: wrap;
        }}
        .pitch-actions a {{
            padding: 9px 18px;
            border-radius: 6px;
            text-decoration: none;
            font-size: 0.85rem;
            font-weight: 600;
            transition: all 0.2s;
        }}
        .btn-deck {{
            background: var(--gold);
            color: #000;
        }}
        .btn-deck:hover {{
            background: var(--gold-light);
        }}
        .btn-pager {{
            background: rgba(255, 255, 255, 0.08);
            border: 1px solid var(--border-card);
            color: #fff;
        }}
        .btn-pager:hover {{
            background: #fff;
            color: #000;
        }}
        .btn-tpl-card {{
            background: rgba(16, 185, 129, 0.2);
            border: 1px solid rgba(16, 185, 129, 0.5);
            color: #6EE7B7;
        }}
        .btn-tpl-card:hover {{
            background: var(--green);
            color: #000;
        }}
    </style>
</head>
<body>

<!-- КИНЕМАТОГРАФИЧЕСКИЙ ФОН GLOBAL PLUS -->
<div class="cinematic-bg-wrap">
    <video class="cinematic-video" autoplay muted loop playsinline src="assets/videos/machinery.mp4"></video>
    <div class="cinematic-overlay"></div>
    <div class="grain-overlay"></div>
</div>

<div class="top-nav">
    <a href="index.html" class="btn-back">&larr; Вернуться в Центр Продаж</a>
    <div style="font-size: 0.85rem; color: var(--gold);">62 готовых коммерческих расчета с шаблонами сайтов</div>
</div>

<div class="container">
    <h1>🔍 Каталог 62 Коммерческих Предложений & Сайтов</h1>
    <p class="subtitle">Персонализированные пакеты внедрения, ценообразование, абонентская плата, экономическое обоснование (ROI) и подходящие шаблоны сайтов Global Plus</p>

    <div class="pitches-list">
        {''.join(cards_pitches)}
    </div>
</div>

</body>
</html>
"""

with open(os.path.join(WORKSPACE, "Comprehensive_Pitches.html"), "w", encoding="utf-8") as f:
    f.write(comprehensive_html)
print("Comprehensive_Pitches.html успешно обновлен с блоками шаблонов!")

# ------------------------------------------------------------------------------
# 5. ГЕНЕРАЦИЯ Dynamic_Pitch_Deck.html (с кнопкой запуска живого шаблона)
# ------------------------------------------------------------------------------
deck_companies_json = json.dumps(COMPANIES, ensure_ascii=False)

deck_html = f"""<!DOCTYPE html>
<html lang="ru">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Интерактивная Презентация | Глобал Плюс</title>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,600;0,700;1,400&family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
<style>
    body {{
        font-family: 'Inter', sans-serif;
        background: #0A0C10;
        color: #fff;
        margin: 0;
        overflow: hidden;
        user-select: none;
    }}
    .watermark {{
        position: fixed;
        top: 25px;
        left: 30px;
        font-family: 'Playfair Display', serif;
        font-size: 16px;
        letter-spacing: 2px;
        color: rgba(197, 160, 89, 0.4);
        z-index: 100;
        display: flex;
        align-items: center;
        gap: 15px;
    }}
    .btn-exit {{
        color: rgba(255,255,255,0.4);
        text-decoration: none;
        font-size: 12px;
        letter-spacing: 1px;
        text-transform: uppercase;
        border: 1px solid rgba(255,255,255,0.15);
        padding: 4px 10px;
        border-radius: 4px;
        transition: 0.2s;
    }}
    .btn-exit:hover {{
        color: #fff;
        border-color: #fff;
    }}
    .slide {{
        width: 100vw;
        height: 100vh;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        position: absolute;
        top: 0;
        left: 0;
        transition: transform 0.6s cubic-bezier(0.2, 0.8, 0.2, 1), opacity 0.6s ease;
        text-align: center;
        padding: 40px;
        box-sizing: border-box;
        opacity: 0;
        pointer-events: none;
    }}
    .slide.active {{
        transform: translateY(0);
        opacity: 1;
        pointer-events: all;
    }}
    .slide:not(.active) {{
        transform: translateY(100%);
    }}
    .slide.prev {{
        transform: translateY(-100%);
    }}
    
    .pill-tag {{
        background: rgba(197, 160, 89, 0.15);
        border: 1px solid #C5A059;
        color: #E0C07A;
        padding: 6px 18px;
        border-radius: 30px;
        font-size: clamp(10px, 1.2vw, 13px);
        letter-spacing: 3px;
        text-transform: uppercase;
        font-weight: 700;
        margin-bottom: 20px;
    }}
    h1 {{
        font-family: 'Playfair Display', serif;
        font-size: clamp(2rem, 5vw, 4.2rem);
        margin: 0 0 15px 0;
        color: #C5A059;
        line-height: 1.1;
    }}
    h2 {{
        font-size: clamp(1.1rem, 2.2vw, 1.8rem);
        color: #F8FAFC;
        font-weight: 400;
        margin-bottom: 25px;
        max-width: 900px;
    }}
    p.body-text {{
        font-size: clamp(1rem, 1.6vw, 1.35rem);
        max-width: 850px;
        color: #94A3B8;
        line-height: 1.6;
        margin: 0 auto;
    }}
    
    .card-pain {{
        background: rgba(211, 47, 47, 0.1);
        border: 1px solid rgba(211, 47, 47, 0.3);
        border-radius: 12px;
        padding: 25px 35px;
        max-width: 800px;
        margin: 20px auto;
        color: #FFCDD2;
        font-size: clamp(1rem, 1.5vw, 1.25rem);
    }}
    .card-sol {{
        background: rgba(197, 160, 89, 0.1);
        border: 1px solid rgba(197, 160, 89, 0.4);
        border-radius: 12px;
        padding: 25px 35px;
        max-width: 800px;
        margin: 20px auto;
        color: #FFF8E1;
        font-size: clamp(1rem, 1.5vw, 1.25rem);
    }}

    .pricing-banner {{
        background: rgba(16, 185, 129, 0.12);
        border: 1px solid rgba(16, 185, 129, 0.4);
        border-radius: 16px;
        padding: 25px 50px;
        margin-top: 25px;
    }}
    .pricing-banner .val {{
        font-family: 'Playfair Display', serif;
        font-size: clamp(1.8rem, 3.5vw, 3rem);
        color: #34D399;
        font-weight: 700;
    }}
    .pricing-banner .sub {{
        color: #94A3B8;
        font-size: 1rem;
        margin-top: 4px;
    }}

    .buttons-row {{
        display: flex;
        gap: 16px;
        justify-content: center;
        flex-wrap: wrap;
        margin-top: 25px;
    }}
    .btn-demo {{
        padding: 14px 35px;
        background: #C5A059;
        color: #000;
        text-decoration: none;
        font-size: clamp(0.85rem, 1.2vw, 1.1rem);
        font-weight: 700;
        border-radius: 40px;
        letter-spacing: 1px;
        transition: all 0.3s;
        box-shadow: 0 10px 25px rgba(197, 160, 89, 0.3);
    }}
    .btn-demo:hover {{
        background: #fff;
        transform: scale(1.05);
    }}
    .btn-template-deck {{
        padding: 14px 35px;
        background: #10B981;
        color: #000;
        text-decoration: none;
        font-size: clamp(0.85rem, 1.2vw, 1.1rem);
        font-weight: 700;
        border-radius: 40px;
        letter-spacing: 1px;
        transition: all 0.3s;
        box-shadow: 0 10px 25px rgba(16, 185, 129, 0.3);
    }}
    .btn-template-deck:hover {{
        background: #6EE7B7;
        transform: scale(1.05);
    }}

    .nav {{
        position: fixed;
        bottom: 30px;
        left: 50%;
        transform: translateX(-50%);
        display: flex;
        gap: 16px;
        z-index: 100;
    }}
    .nav-dot {{
        width: 12px;
        height: 12px;
        border-radius: 50%;
        background: rgba(255, 255, 255, 0.2);
        cursor: pointer;
        transition: 0.3s;
    }}
    .nav-dot.active {{
        background: #C5A059;
        transform: scale(1.4);
    }}
</style>
</head>
<body>

<!-- ДИНАМИЧЕСКИЙ ОТРАСЛЕВОЙ ВИДЕОФОН GLOBAL PLUS -->
<div class="cinematic-bg-wrap">
    <video id="bgVideo" class="cinematic-video" autoplay muted loop playsinline src="assets/videos/machinery.mp4"></video>
    <div class="cinematic-overlay"></div>
    <div class="grain-overlay"></div>
</div>

<div class="watermark">
    <span>ГЛОБАЛ ПЛЮС &times; GLOBAL TEAM PARTNERS</span>
    <a href="Leads_List.html" class="btn-exit">&larr; В базу лидов</a>
</div>

<!-- СЛАЙД 0: ТИТУЛ -->
<div class="slide active" id="slide0">
    <div class="pill-tag" id="d-sector-tag">СТРАТЕГИЧЕСКОЕ ПРЕДЛОЖЕНИЕ 2026</div>
    <h1 id="d-name">Название Компании</h1>
    <h2 id="d-focus">Специализация предприятия</h2>
    <p class="body-text">Персональная программа цифровой трансформации сбыта, ликвидации потерь и внедрения ИИ-инфраструктуры.</p>
    <p style="font-size: 0.9rem; color: #64748B; margin-top: 30px;">(Листайте стрелками, свайпом или клавишей Пробел &darr;)</p>
</div>

<!-- СЛАЙД 1: ДИАГНОСТИКА И БОЛЬ -->
<div class="slide" id="slide1">
    <div class="pill-tag" style="background: rgba(211,47,47,0.15); border-color:#D32F2F; color:#FF8A80;">ТЕКУЩИЕ УЗКИЕ МЕСТА</div>
    <h1 style="color:#F87171;">Точки Потери Прибыли</h1>
    <div class="card-pain" id="d-pain">
        Выявленная боль бизнес-процессов...
    </div>
    <p class="body-text">Традиционные методы работы с клиентами и ручные согласования создают задержки и снижают маржинальность в борьбе с конкурентами.</p>
</div>

<!-- СЛАЙД 2: РЕШЕНИЕ И ДЕМО -->
<div class="slide" id="slide2">
    <div class="pill-tag">ИНЖЕНЕРНОЕ РЕШЕНИЕ ЗА 48 ЧАСОВ</div>
    <h1>Быстрый Старт & Боевой Прототип</h1>
    <div class="card-sol" id="d-trojan">
        Оффер Троянского коня...
    </div>
    <div class="buttons-row">
        <a href="#" id="d-demo" class="btn-demo" target="_blank">КАЛЬКУЛЯТОР / ДЕМО-МОДУЛЬ ⚡</a>
        <a href="#" id="d-template" class="btn-template-deck" target="_blank">ШАБЛОН САЙТА GLOBAL PLUS 🌐</a>
    </div>
</div>

<!-- СЛАЙД 3: ЭКОНОМИКА И ПАРТНЕРСТВО -->
<div class="slide" id="slide3">
    <div class="pill-tag" style="background: rgba(16,185,129,0.15); border-color:#10B981; color:#6EE7B7;">ФОРМАТ СОТРУДНИЧЕСТВА</div>
    <h1>Инвестиции и Окупаемость (ROI)</h1>
    <p class="body-text" id="d-roi">Ожидаемый экономический эффект...</p>
    
    <div class="pricing-banner">
        <div class="val" id="d-price">Пакет внедрения</div>
        <div class="sub">Включает запуск под ключ + гарантийное сопровождение</div>
    </div>
    
    <p style="margin-top: 25px; color: #94A3B8; font-size: 0.95rem;">
        Глобал Плюс берет на себя всю техническую поддержку. Никаких простоев, максимальная конверсия с первого дня.
    </p>
</div>

<div class="nav">
    <div class="nav-dot active" onclick="goTo(0)"></div>
    <div class="nav-dot" onclick="goTo(1)"></div>
    <div class="nav-dot" onclick="goTo(2)"></div>
    <div class="nav-dot" onclick="goTo(3)"></div>
</div>

<script>
    const db = {deck_companies_json};
    const urlParams = new URLSearchParams(window.location.search);
    const targetId = urlParams.get('id');

    let currentCompany = db.find(c => c.id === targetId) || db[0];

    document.getElementById('d-name').innerText = currentCompany.name;
    document.getElementById('d-focus').innerText = currentCompany.focus + " (" + currentCompany.region + ")";
    document.getElementById('d-pain').innerText = currentCompany.pain_point;
    document.getElementById('d-trojan').innerText = currentCompany.trojan_pitch;
    document.getElementById('d-demo').href = currentCompany.demo_link;
    document.getElementById('d-template').href = currentCompany.template_url;
    document.getElementById('d-template').title = currentCompany.template_name;
    document.getElementById('d-roi').innerText = currentCompany.roi_desc;
    document.getElementById('d-price').innerText = currentCompany.price_setup + " | Абонентка: " + currentCompany.price_retainer;
    document.getElementById('d-sector-tag').innerText = "ИНДУСТРИЯ: " + currentCompany.sector.toUpperCase();
    document.title = currentCompany.name + " — Стратегическая Презентация";

    // ДИНАМИЧЕСКИЙ ОТРАСЛЕВОЙ ВИДЕОФОН
    const SECTOR_VIDEOS = {{
        "Лесопромышленность & Деревообработка": "assets/videos/wood.mp4",
        "Машиностроение & Металл": "assets/videos/machinery.mp4",
        "Девелопмент & Недвижимость": "assets/videos/estate.mp4",
        "Медицина & Эстетика": "assets/videos/clinic.mp4",
        "Авто & Детейлинг": "assets/videos/auto.mp4",
        "HoReCa & Отели": "assets/videos/horeca.mp4",
        "Пищепром & Агро": "assets/videos/agro.mp4",
        "Туризм, Спорт & Услуги": "assets/videos/tourism.mp4"
    }};

    let videoFile = SECTOR_VIDEOS[currentCompany.sector] || "assets/videos/machinery.mp4";
    const cid = (currentCompany.id || "").toLowerCase();
    const cfocus = (currentCompany.focus || "").toLowerCase();
    if (cid.includes("denta") || cfocus.includes("стоматолог")) {{
        videoFile = "assets/videos/dental.mp4";
    }} else if (cid.includes("stroy") || cfocus.includes("генподряд") || cfocus.includes("монтаж") || cfocus.includes("строительств")) {{
        videoFile = "assets/videos/stroyka.mp4";
    }}

    const bgVid = document.getElementById('bgVideo');
    if (bgVid) {{
        bgVid.muted = true;
        bgVid.defaultMuted = true;
        bgVid.playsInline = true;
        bgVid.setAttribute('playsinline', '');
        bgVid.setAttribute('muted', '');
        bgVid.src = videoFile;
        bgVid.load();
        const p = bgVid.play();
        if (p !== undefined) {{
            p.catch(e => {{
                console.log('Autoplay muted fallback:', e);
                const unlock = () => {{
                    bgVid.play();
                    window.removeEventListener('click', unlock);
                    window.removeEventListener('touchstart', unlock);
                    window.removeEventListener('keydown', unlock);
                }};
                window.addEventListener('click', unlock);
                window.addEventListener('touchstart', unlock);
                window.addEventListener('keydown', unlock);
            }});
        }}
    }}

    // Слайдер
    let curSlide = 0;
    const totalSlides = 4;

    function goTo(idx) {{
        if (idx < 0 || idx >= totalSlides) return;
        document.querySelectorAll('.slide').forEach((s, i) => {{
            s.classList.remove('active', 'prev');
            if (i === idx) s.classList.add('active');
            else if (i < idx) s.classList.add('prev');
        }});
        document.querySelectorAll('.nav-dot').forEach((d, i) => {{
            d.classList.toggle('active', i === idx);
        }});
        curSlide = idx;
    }}

    window.addEventListener('keydown', (e) => {{
        if (e.code === 'Space' || e.code === 'ArrowDown' || e.code === 'ArrowRight') {{
            goTo((curSlide + 1) % totalSlides);
        }} else if (e.code === 'ArrowUp' || e.code === 'ArrowLeft') {{
            goTo((curSlide - 1 + totalSlides) % totalSlides);
        }}
    }});

    // Поддержка свайпов на тачскринах
    let touchStartY = 0;
    window.addEventListener('touchstart', e => {{ touchStartY = e.touches[0].clientY; }});
    window.addEventListener('touchend', e => {{
        let touchEndY = e.changedTouches[0].clientY;
        if (touchStartY - touchEndY > 50) goTo((curSlide + 1) % totalSlides);
        else if (touchEndY - touchStartY > 50) goTo((curSlide - 1 + totalSlides) % totalSlides);
    }});
</script>

</body>
</html>
"""

with open(os.path.join(WORKSPACE, "Dynamic_Pitch_Deck.html"), "w", encoding="utf-8") as f:
    f.write(deck_html)
print("Dynamic_Pitch_Deck.html успешно обновлен с кнопками сайтов!")

# ------------------------------------------------------------------------------
# 6. ГЕНЕРАЦИЯ Dynamic_One_Pager.html (с указанием шаблона сайта)
# ------------------------------------------------------------------------------
pager_html = f"""<!DOCTYPE html>
<html lang="ru">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Коммерческое Предложение (One-Pager) | Глобал Плюс</title>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>
    body {{
        background: #1A1F2C;
        color: #1E293B;
        font-family: 'Inter', sans-serif;
        margin: 0;
        padding: 40px 20px;
        display: flex;
        justify-content: center;
    }}
    .sheet {{
        background: #FFFFFF;
        width: 100%;
        max-width: 820px;
        min-height: 1100px;
        padding: 60px;
        box-sizing: border-box;
        box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5);
        border-radius: 4px;
        position: relative;
    }}
    .header {{
        display: flex;
        justify-content: space-between;
        align-items: flex-start;
        border-bottom: 2px solid #C5A059;
        padding-bottom: 25px;
        margin-bottom: 30px;
    }}
    .brand {{
        font-family: 'Playfair Display', serif;
        font-size: 20px;
        font-weight: 700;
        color: #0F172A;
        letter-spacing: 1px;
    }}
    .brand span {{ color: #C5A059; }}
    .doc-type {{
        text-align: right;
        font-size: 11px;
        text-transform: uppercase;
        letter-spacing: 2px;
        color: #64748B;
        font-weight: 600;
    }}
    .title-block {{ margin-bottom: 30px; }}
    h1 {{
        font-family: 'Playfair Display', serif;
        font-size: 28px;
        color: #0F172A;
        margin: 0 0 8px 0;
    }}
    .company-sub {{
        font-size: 14px;
        color: #C5A059;
        font-weight: 600;
    }}
    .section-title {{
        font-size: 13px;
        text-transform: uppercase;
        letter-spacing: 1.5px;
        color: #0F172A;
        font-weight: 700;
        margin: 25px 0 12px 0;
        border-bottom: 1px solid #E2E8F0;
        padding-bottom: 6px;
    }}
    .block-text {{
        font-size: 13.5px;
        line-height: 1.6;
        color: #334155;
    }}
    .highlight-box {{
        background: #F8FAFC;
        border-left: 4px solid #C5A059;
        padding: 16px 20px;
        margin: 15px 0;
        border-radius: 0 6px 6px 0;
    }}
    .template-box-pager {{
        background: #ECFDF5;
        border: 1px solid #A7F3D0;
        border-radius: 6px;
        padding: 14px 18px;
        margin: 14px 0;
        font-size: 13px;
    }}
    .template-box-pager a {{
        color: #047857;
        font-weight: 700;
        text-decoration: underline;
    }}
    .pricing-table {{
        width: 100%;
        border-collapse: collapse;
        margin: 20px 0;
    }}
    .pricing-table th, .pricing-table td {{
        padding: 12px 16px;
        font-size: 13px;
        border: 1px solid #E2E8F0;
        text-align: left;
    }}
    .pricing-table th {{
        background: #F1F5F9;
        color: #0F172A;
    }}
    .price-num {{
        font-weight: 700;
        color: #0F172A;
    }}
    .footer-sign {{
        margin-top: 45px;
        border-top: 1px solid #E2E8F0;
        padding-top: 20px;
        display: flex;
        justify-content: space-between;
        font-size: 12px;
        color: #64748B;
    }}
    .btn-print {{
        position: fixed;
        top: 20px;
        right: 20px;
        background: #C5A059;
        color: #000;
        border: none;
        padding: 10px 20px;
        border-radius: 6px;
        font-weight: 700;
        cursor: pointer;
        font-size: 13px;
    }}
    @media print {{
        body {{ background: #fff; padding: 0; }}
        .sheet {{ box-shadow: none; padding: 40px; }}
        .btn-print, .cinematic-bg-wrap {{ display: none !important; }}
    }}
</style>
</head>
<body>

<!-- ДИНАМИЧЕСКИЙ ОТРАСЛЕВОЙ ВИДЕОФОН GLOBAL PLUS -->
<div class="cinematic-bg-wrap">
    <video id="bgVideo" class="cinematic-video" autoplay muted loop playsinline src="assets/videos/machinery.mp4"></video>
    <div class="cinematic-overlay"></div>
    <div class="grain-overlay"></div>
</div>

<button class="btn-print" onclick="window.print()">🖨️ Печать / Сохранить в PDF</button>

<div class="sheet">
    <div class="header">
        <div>
            <div class="brand">ГЛОБАЛ ПЛЮС <span>&times;</span> GLOBAL TEAM PARTNERS</div>
            <div style="font-size: 11px; color: #64748B; margin-top: 4px;">Центр регионального развития • Свердловская область</div>
        </div>
        <div class="doc-type">
            Стратегический меморандум<br>
            Конфиденциально
        </div>
    </div>

    <div class="title-block">
        <h1 id="d-name">НАО «СВЕЗА Верхняя Синячиха»</h1>
        <div class="company-sub" id="d-sub">Лесопромышленность & Деревообработка | Верхняя Синячиха</div>
    </div>

    <div class="section-title">1. Аудит Процессов и Точки Потери Маржи</div>
    <div class="block-text highlight-box" id="d-pain">
        Выявленная боль бизнес-процессов...
    </div>

    <div class="section-title">2. Инженерное Решение: Запуск за 48 Часов</div>
    <div class="block-text" id="d-sol">
        Оффер Троянского коня...
    </div>

    <div class="template-box-pager">
        <strong>🌐 Рекомендуемый боевой шаблон сайта:</strong> 
        <a href="#" id="d-tpl-link" target="_blank"><span id="d-tpl-name">Название шаблона</span> ↗</a>
        <div style="color: #065F46; font-size: 12px; margin-top: 4px;" id="d-tpl-desc">Описание шаблона...</div>
    </div>

    <div class="section-title">3. Программа Внедрения и Стоимость</div>
    <table class="pricing-table">
        <thead>
            <tr>
                <th>Этап внедрения</th>
                <th>Срок</th>
                <th>Содержание работ</th>
                <th>Инвестиции</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td><strong>Фаза 1: Запуск прототипа</strong></td>
                <td>48 часов</td>
                <td>Развертывание интерактивной B2B-витрины / мобильного портала</td>
                <td class="price-num" id="d-p1">По прайсу</td>
            </tr>
            <tr>
                <td><strong>Фаза 2: Интеграция &amp; ИИ</strong></td>
                <td>1–2 недели</td>
                <td>Подключение Telegram/WhatsApp ИИ-бота, интеграция с CRM / 1С</td>
                <td class="price-num" id="d-p2">Включено</td>
            </tr>
            <tr>
                <td><strong>Фаза 3: Сопровождение</strong></td>
                <td>Ежемесячно</td>
                <td>Техническая поддержка, обновление остатков, докрутка конверсий</td>
                <td class="price-num" id="d-p3" style="color: #10B981;">По тарифу</td>
            </tr>
        </tbody>
    </table>

    <div class="section-title">4. Ожидаемый Экономический Эффект (ROI)</div>
    <div class="block-text" id="d-roi" style="margin-bottom: 25px; font-weight: 500; color: #047857;">
        Расчет окупаемости...
    </div>

    <div class="footer-sign">
        <div>
            <strong>Региональный представитель:</strong> Дмитрий<br>
            Глобал Плюс &bull; Свердловская область
        </div>
        <div style="text-align: right;">
            Действительно до конца 2026 г.<br>
            Global Plus &times; GlobalTeamPartners
        </div>
    </div>
</div>

<script>
    const db = {deck_companies_json};
    const urlParams = new URLSearchParams(window.location.search);
    const targetId = urlParams.get('id');

    let c = db.find(item => item.id === targetId) || db[0];

    document.getElementById('d-name').innerText = c.name;
    document.getElementById('d-sub').innerText = c.sector + " | " + c.region + " | ЛПР: " + c.target_persona;
    document.getElementById('d-pain').innerText = c.pain_point;
    document.getElementById('d-sol').innerText = c.trojan_pitch;
    document.getElementById('d-tpl-link').href = c.template_url;
    document.getElementById('d-tpl-name').innerText = c.template_name;
    document.getElementById('d-tpl-desc').innerText = c.template_desc;
    document.getElementById('d-p1').innerText = c.price_setup;
    document.getElementById('d-p3').innerText = c.price_retainer;
    document.getElementById('d-roi').innerText = "✓ " + c.roi_desc;
    document.title = "КП: " + c.name + " | Глобал Плюс";

    // ДИНАМИЧЕСКИЙ ОТРАСЛЕВОЙ ВИДЕОФОН
    const SECTOR_VIDEOS = {{
        "Лесопромышленность & Деревообработка": "assets/videos/wood.mp4",
        "Машиностроение & Металл": "assets/videos/machinery.mp4",
        "Девелопмент & Недвижимость": "assets/videos/estate.mp4",
        "Медицина & Эстетика": "assets/videos/clinic.mp4",
        "Авто & Детейлинг": "assets/videos/auto.mp4",
        "HoReCa & Отели": "assets/videos/horeca.mp4",
        "Пищепром & Агро": "assets/videos/agro.mp4",
        "Туризм, Спорт & Услуги": "assets/videos/tourism.mp4"
    }};

    let videoFile = SECTOR_VIDEOS[c.sector] || "assets/videos/machinery.mp4";
    const cid = (c.id || "").toLowerCase();
    const cfocus = (c.focus || "").toLowerCase();
    if (cid.includes("denta") || cfocus.includes("стоматолог")) {{
        videoFile = "assets/videos/dental.mp4";
    }} else if (cid.includes("stroy") || cfocus.includes("генподряд") || cfocus.includes("монтаж") || cfocus.includes("строительств")) {{
        videoFile = "assets/videos/stroyka.mp4";
    }}

    const bgVid = document.getElementById('bgVideo');
    if (bgVid) {{
        bgVid.muted = true;
        bgVid.defaultMuted = true;
        bgVid.playsInline = true;
        bgVid.setAttribute('playsinline', '');
        bgVid.setAttribute('muted', '');
        bgVid.src = videoFile;
        bgVid.load();
        const p = bgVid.play();
        if (p !== undefined) {{
            p.catch(e => {{
                console.log('Autoplay muted fallback:', e);
                const unlock = () => {{
                    bgVid.play();
                    window.removeEventListener('click', unlock);
                    window.removeEventListener('touchstart', unlock);
                    window.removeEventListener('keydown', unlock);
                }};
                window.addEventListener('click', unlock);
                window.addEventListener('touchstart', unlock);
                window.addEventListener('keydown', unlock);
            }});
        }}
    }}
</script>

</body>
</html>
"""

with open(os.path.join(WORKSPACE, "Dynamic_One_Pager.html"), "w", encoding="utf-8") as f:
    f.write(pager_html)
print("Dynamic_One_Pager.html успешно обновлен!")

# ------------------------------------------------------------------------------
# 7. ОБНОВЛЕНИЕ Solo_Executive_Strategy.html (Плейбук Димы с главой о шаблонах)
# ------------------------------------------------------------------------------
solo_strategy_raw_md = """# 🐺 Плейбук Димы: Стратегия На Земле
### Практическое руководство регионального представителя (Глобал Плюс &times; GlobalTeamPartners)

> **Миссия Дмитрия:** Построить в Свердловской области (Верхняя Синячиха, Алапаевск, Екатеринбург) системную партнерскую сеть из **15–25 постоянных корпоративных клиентов** на цифровизацию отделов сбыта, ликвидацию кадрового дефицита и внедрение кинематографичных сайтов и ИИ-инфраструктуры от **Global Plus**.
>
> Ты — **не продавец сайтов**. Ты — **руководитель регионального развития технологической группы Global Plus**, который приносит уральским предприятиям реальный рост выручки и сокращение рутины.

---

## ♟️ 1. Позиционирование Дмитрия на Переговорах

Когда ты заходишь на завод или в кабинет генерального директора, твой статус и речь должны кардинально отличаться от типовых звонарей:
* ❌ **Как говорят неудачники:** *"Здравствуйте, мы веб-студия, делаем сайты и боты, вам случайно не нужно что-то обновить?"* — За это сразу выставляют за дверь или отправляют к секретарю.
* ✅ **Как говоришь ты (Дмитрий):** *"Добрый день, [Имя Отчество]. Я Дмитрий, региональный партнер технологической группы Глобал Плюс / GlobalTeamPartners. Мы специализируемся на автоматизации оптового сбыта, разработке кинематографичных сайтов с видеофоном и внедрении ИИ-инфраструктуры для промышленных предприятий Урала. Я детально изучил ваше производство: ваши менеджеры теряют до 30% оптовых заявок в нерабочее время, а кадровый дефицит сдерживает темпы отгрузок. Моя инженерная группа за 48 часов разработала интерактивный цифровой модуль специально под вашу номенклатуру продукции. Уделите мне 60 секунд на планшете."*

**Твой образ:** Уверенный, деловой уралец, который говорит на языке цифр, рентабельности и фактов, за спиной которого стоят ведущие инженеры консорциума Global Plus.

---

## 🛠️ 2. Трехшаговая Модель «Троянский Конь»: Алгоритм к Сделке

Главная ошибка классических продаж в B2B — пытаться сразу продать полугодовой контракт на миллионы рублей. Мы действуем иначе:

```
[Шаг 1: Разведка и Диагноз] ➔ [Шаг 2: Прототип за 48 часов] ➔ [Шаг 3: Абонентский Контракт]
   Показываем потерю денег        Демо на iPad за 30 сек         LTV: 50 000 – 200 000 ₽/мес
```

### 🟢 Шаг 1: Разведка и точечный диагноз боли
Перед визитом открой базу [Leads_List.html](Leads_List.html) и выбери предприятие:
* **В Верхней Синячихе и Алапаевске:** Ты знаешь местную специфику лично. Найди слабое место: отсутствие круглосуточного калькулятора партий (фанеры, шнеков, пиломатериалов), нехватка станочников ЧПУ, прайс-лист в старом нечитаемом файле, медленная обработка оптовых счетов.
* **Сформулируй финансовую потерю:** *"Вы теряете от 400 000 до 1 500 000 рублей в месяц, когда крупный закупщик из Тюмени, ХМАО или Москвы не может мгновенно получить расчет спецификации в субботу вечером и уходит к дилерам в другой регион".*

### 🟡 Шаг 2: Быстрый старт (Живой Прототип за 48 часов)
У тебя на планшете уже открыты интерактивные демо-порталы и шаблоны сайтов:
1. Для лесопромышленников (СВЕЗА, Лестех, АДОЗ, АЛХ) ➔ **Калькулятор партий фанеры и кубатуры по ГОСТу**.
2. Для буровиков и машиностроителей (Стройдормаш, ЗИСТ, PSM) ➔ **3D-селектор бурильных машин и подбор шнеков**.
3. Для застройщиков Екатеринбурга (Брусника, Атом, УГМК) ➔ **Кинематографичный портал Belgrade Waterfront & 3D-планировки**.
4. Для ресторанов и отелей (Троекуров, Kitchen, Hyatt) ➔ **Salon 1905 Fine Dining с VIP-системой бронирования**.
5. Для клиник (УГМК-Здоровье, Нудельман) ➔ **Aesthetic Clinic с AI-триажем и онлайн-записью**.
6. Для детейлинга и авто (Detailing Alarm, Порше Центр) ➔ **Auto Shine с 60fps-анимацией оклейки авто**.
7. Для ритейла и пищепрома (Талицкое молоко, СМАК, Черкашин) ➔ **Геоточка с сетью на Яндекс Картах**.

Ты протягиваешь планшет:
> *"Посмотрите, вот так должен работать ваш отдел сбыта в 2026 году. Покупатель выбирает объем партии за 10 секунд, система автоматически проверяет склад и формирует спецификацию. Мы не предлагаем вам ждать полгода. Мы запускаем пилотный прототип за 48 часов на ваших данных".*

### 🔴 Шаг 3: Перевод на долгосрочное абонентское сопровождение (LTV)
После запуска базового прототипа ты не уходишь:
* *"Теперь, когда система собирает заявки круглосуточно, мы подключаем ИИ-ассистента в Telegram, интегрируем всё с вашей 1С или CRM и обеспечиваем полную техническую поддержку 24/7"*.
* Фиксируешь абонентскую плату: **от 35 000 до 150 000 руб./месяц** с каждого предприятия.
* **15 предприятий на абонентке = от 600 000 до 1 500 000 руб. стабильной ежемесячной выручки!**

---

## 📱 3. Мастерство Работы с Планшетом на Встрече (30-секундный Вау-Эффект)

Директора уральских заводов перегружены отчетами и совещаниями. Если ты начнешь показывать слайды презентации PowerPoint на 40 страниц — он уснет через 2 минуты.

**Сценарий показа на планшете (iPad / планшет / смартфон):**
1. **Первые 5 секунд:** Планшет уже разблокирован, открыта главная страница демо или `Dynamic_Pitch_Deck.html` под его компанию. Ты держишь его двумя руками и кладешь перед ним на стол.
2. **Секунды 6–15:** Твой палец делает 2 клика: выбор типа продукции ➔ выбор объема партии. Цифра пересчитывается мгновенно, появляется кнопка «Сформировать спецификацию ГОСТ».
3. **Секунды 16–30:** Ты говоришь: *«Вот это действие сейчас у ваших менеджеров занимает 3 часа телефонных согласований. В нашей системе клиент нажимает одну кнопку, а счет уже лежит у него в WhatsApp и в вашей 1С. Готовы запустить это на этой неделе?»*

---

## 🌐 3.1. Демонстрация Шаблонов Сайтов Global Plus по Отраслям

У тебя в арсенале есть официальный [Каталог Шаблонов Сайтов Global Plus](Templates_Catalog.html). Когда директор говорит: *«А как это будет выглядеть визуально? У нас сайт устарел, но мы не понимаем, что сейчас модно»*, ты открываешь соответствующий живой шаблон:

| Отрасль и Клиент | Боевой Шаблон Global Plus | Что показать на экране за 15 секунд |
|---|---|---|
| **Лесопромышленность & Фанера** (СВЕЗА, Лестех, АДОЗ, АЛХ) | [УралЛесПром](demos/wood-industry-demo/index.html) | Введи объем партии березовой фанеры: мгновенный расчет веса, вагонных норм по ГОСТ и спецификации со счетом. |
| **Тяжелая Промышленность & Заводы** (ВСЗ, Уралмаш, Стройдормаш) | [Завод ЗКСК](https://globalteamgroup.github.io/zksk-sample/) & [3D-Конфигуратор](demos/machinery-demo/index.html) | Покажи интерактивные 3D-каркасы цехов, расчет металлоемкости тоннажа и подбор бурилок под тип грунта. |
| **Строительство & Генподряд** (Алапаевск-Строй, Атом, Брусника) | [Стройка-Про](https://globalteamgroup.github.io/stroyka-pro/) | Продемонстрируй допуски СРО, парк строительной техники с характеристиками и сметный калькулятор этапов СМР. |
| **Девелопмент & Клубные Дома** (УГМК-Застройщик, Forum Group, PRINZIP) | [Luxury Estate](https://globalteamgroup.github.io/luxury-estate-sample/) | Покажи интерактивный генплан поселка, 3D-резиденции, видовые панорамы и закрытый брокерский чат. |
| **Клиники & Стоматология** (УГМК-Здоровье, Нудельман, Дента-Люкс) | [Клиника Европа](https://globalteamgroup.github.io/europa-clinic/) & [Клиника Люмьер](https://globalteamgroup.github.io/lumiere-clinic-sample/) | Живой видеофон клиники, 3D-моделирование улыбок, протоколы имплантации До/После и запись к врачу со смартфона. |
| **Детейлинг & Премиум Авто** (Detailing Alarm, Порше Центр, Автобан) | [Elite Detailing](https://globalteamgroup.github.io/elite-detailing/) | Проведи пальцем по экрану: автомобиль поворачивается в 60fps, подсвечиваются зоны оклейки полиуретаном и расчет сметы. |
| **Сервис Спецтехники & Автопарки** (СТО Синячихи, лесовозы, базы) | [Сервисный Центр](demos/service-demo/index.html) | Покажи онлайн-вызов выездного механика на делянку или карьер и моментальный заказ гидравлики. |
| **Отели & Базы Отдыха** (Эрмитаж, Металлург, Чистые пруды, Высоцкий) | [HoReCa Grand](https://globalteamgroup.github.io/horeca-grand-sample/) | Атмосферный видеоряд загородного курорта, прямое бронирование номеров и коттеджей без комиссии агрегаторов. |
| **Рестораны & Банкеты** (Троекуровъ, Kitchen, Сойка, Гастроли) | [Ресторанное Демо](demos/horeca-demo/index.html) | Интерактивная схема панорамных столиков, банкетный калькулятор меню и внесение депозита онлайн. |
| **Ритейл & Молоко/Мясо** (Талицкое молоко, СМАК, Черкашин, АМК) | [Геоточка (Яндекс Карты)](https://globalteampartners.github.io/geotochka/) | Карта присутствия с автопоиском ближайшей фирменной точки свежей продукции для оптовиков и покупателей. |
| **Фабрики & Франшизы** (Птицефабрика, Alma Ceramica, АДОЗ, АЛХ) | [Тенториум Фабрика](https://globalteampartners.github.io/tentorium-presentation/) | 3D-тур по цехам, лаборатории контроля чистоты ISO/HACCP и оптовый дистрибьюторский кабинет. |
| **Туризм & АУЖД** (АУЖД узкоколейка, Музей Синячихи, отели) | [Туристический Портал Урала](https://globalteamgroup.github.io/tourism-sample/) | Онлайн-покупка билетов на ретропоезд и бронирование экскурсионных пакетов с выбором вагона и гида. |
| **Шоурил Global Plus** (Визитка агентства для всех директоров) | [Global Plus (globalplus.tech)](https://globalteamgroup.github.io/global-plus/) | Презентация возможностей агентства: Cinematic Scroll, кейсы удвоения B2B-конверсий и запуск за 48 часов. |

---

## 📅 4. Регламент 4-Недельного Спринта Дмитрия

### 📌 Неделя 1: Локальный Блицкриг (Синячиха & Алапаевск)
* **Цель:** Отработать 10–15 ключевых предприятий района (СВЕЗА, Лестех, Стройдормаш, ЗИСТ, Бурмаш, АДОЗ, АЛХ, Молочный комбинат, Металлург, Энергоресурс).
* **Преимущество:** Ты рядом, можешь приехать лично за 20 минут.
* **План:** 2 встречи в день. Итог: 3 запущенных пилота.

### 📌 Неделя 2: Екатеринбург — Быстрый Средний Чек (HoReCa, Медицина, Авто)
* **Цель:** Назначить 6–8 встреч в Екатеринбурге на четверг и пятницу (центр города: Радищева, 8 Марта, Ленина, БЦ Высоцкий).
* **Кому показывать:** Премиум-рестораны (Троекуров, Kitchen, Сойка, Гастроли), клиники (УГМК-Здоровье, Нудельман), детейлинг-центры (Detailing Alarm, Restyle).
* **Итог:** Рестораторы и главврачи принимают решения быстрее заводов (цикл сделки 3–5 дней).

### 📌 Неделя 3: Екатеринбург — Крупные Девелоперы & Промышленность
* **Цель:** Встречи с коммерческими директорами строительных холдингов (Брусника, Атомстройкомплекс, Prinzip, УГМК-Застройщик) и машиностроителями (Пневмостроймашина, УЗГА, Уралмаш).
* **Презентация:** Демонстрация AI-брокеров, 3D-планировок квартир и B2B-конфигураторов оборудования.

### 📌 Неделя 4: Финализация и Сбор Абонентских Плат
* **Цель:** Подписание договоров, настройка доменов, передача технических ТЗ инженерам Global Plus, получение первых абонентских оплат (Retainer).

---

## 🛡️ 5. Золотые Правила Уральских Переговоров

1. **Никакой воды и пафоса.** Говори предельно понятно: не "диджитализация customer experience", а *"клиент нажал кнопку, через 5 секунд ему в WhatsApp упал готовый расчет, а вашему снабженцу — уведомление"*.
2. **Уважай производство.** Директора заводов Алапаевска и Синячихи знают каждый винтик. Прояви искреннее уважение к их труду и масштабу.
3. **Держи слово.** На Урале репутация строится годами, а теряется за один сорванный срок. Пообещал демо в четверг в 10:00 — покажи в 09:50.
"""

solo_html_content = markdown.markdown(solo_strategy_raw_md, extensions=['tables', 'fenced_code'])

def render_doc_page(title, nav_back_text, accent_color, content_html):
    return f"""<!DOCTYPE html>
<html lang="ru">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} | Глобал Плюс</title>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,600;0,700;1,400&family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
<style>
  :root {{
    --bg-base: #0B0E14;
    --bg-surface: #121721;
    --bg-card: #18202E;
    --gold: #C5A059;
    --gold-light: #E0C07A;
    --red: #D32F2F;
    --green: #10B981;
    --blue: #2563EB;
    --white: #F8FAFC;
    --text-dim: #94A3B8;
    --border: rgba(197, 160, 89, 0.2);
    --border-card: rgba(255, 255, 255, 0.08);
    --accent: {accent_color};
  }}
  * {{ margin: 0; padding: 0; box-sizing: border-box; }}
  body {{
    font-family: 'Inter', -apple-system, sans-serif;
    background: var(--bg-base);
    color: var(--white);
    padding: 40px 20px 80px;
    max-width: 900px;
    margin: 0 auto;
    line-height: 1.75;
  }}
  .top-nav {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 35px;
    padding-bottom: 20px;
    border-bottom: 1px solid var(--border-card);
  }}
  .btn-back {{
    display: inline-flex;
    align-items: center;
    gap: 8px;
    padding: 10px 20px;
    background: var(--accent);
    color: #000;
    text-decoration: none;
    border-radius: 6px;
    font-weight: 700;
    font-size: 0.9rem;
    transition: all 0.2s;
  }}
  .btn-back:hover {{
    filter: brightness(1.15);
    transform: translateY(-2px);
  }}
  .brand-badge {{
    font-size: 0.8rem;
    letter-spacing: 2px;
    text-transform: uppercase;
    color: var(--gold);
    font-weight: 700;
  }}
  
  /* ТИПОГРАФИКА СТАТИЧЕСКОГО КОНТЕНТА */
  .doc-content h1 {{
    font-family: 'Playfair Display', serif;
    font-size: clamp(2.2rem, 4vw, 3rem);
    color: var(--gold);
    line-height: 1.2;
    margin-bottom: 12px;
  }}
  .doc-content h2 {{
    font-family: 'Playfair Display', serif;
    font-size: clamp(1.5rem, 2.8vw, 2rem);
    color: var(--white);
    margin-top: 45px;
    margin-bottom: 18px;
    border-bottom: 1px solid var(--border-card);
    padding-bottom: 10px;
  }}
  .doc-content h3 {{
    font-family: 'Playfair Display', serif;
    font-size: 1.25rem;
    color: var(--gold-light);
    margin-top: 30px;
    margin-bottom: 12px;
  }}
  .doc-content p {{
    color: #E2E8F0;
    margin-bottom: 18px;
    font-size: 1.05rem;
  }}
  .doc-content ul, .doc-content ol {{
    margin-left: 24px;
    margin-bottom: 24px;
    color: #CBD5E1;
  }}
  .doc-content li {{
    margin-bottom: 10px;
    font-size: 1.02rem;
  }}
  .doc-content a {{
    color: var(--gold-light);
    text-decoration: underline;
    font-weight: 600;
  }}
  .doc-content blockquote {{
    background: rgba(197, 160, 89, 0.08);
    border-left: 4px solid var(--gold);
    padding: 20px 24px;
    margin: 25px 0;
    border-radius: 0 8px 8px 0;
    font-size: 1.05rem;
    color: #F1F5F9;
  }}
  .doc-content hr {{
    border: none;
    height: 1px;
    background: var(--border-card);
    margin: 40px 0;
  }}
  .doc-content code {{
    background: rgba(255, 255, 255, 0.08);
    color: var(--gold-light);
    padding: 3px 8px;
    border-radius: 4px;
    font-family: monospace;
    font-size: 0.9em;
  }}
  .doc-content pre {{
    background: #141A26;
    border: 1px solid var(--border-card);
    border-radius: 8px;
    padding: 20px;
    overflow-x: auto;
    margin: 25px 0;
  }}
  .doc-content pre code {{
    background: transparent;
    padding: 0;
    color: #E2E8F0;
  }}
  .doc-content table {{
    width: 100%;
    border-collapse: collapse;
    margin: 30px 0;
    background: var(--bg-surface);
    border-radius: 8px;
    overflow: hidden;
  }}
  .doc-content th, .doc-content td {{
    padding: 14px 18px;
    border: 1px solid var(--border-card);
    text-align: left;
    font-size: 0.95rem;
  }}
  .doc-content th {{
    background: #18202E;
    color: var(--gold);
    font-weight: 600;
  }}
  .doc-content tr:hover td {{
    background: rgba(255, 255, 255, 0.02);
  }}

  /* КАРТОЧКА БЫСТРОГО ДЕЙСТВИЯ */
  .action-banner {{
    background: linear-gradient(135deg, rgba(197,160,89,0.15) 0%, rgba(197,160,89,0.05) 100%);
    border: 1px solid var(--gold);
    border-radius: 12px;
    padding: 24px;
    margin: 35px 0;
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap;
    gap: 16px;
  }}
  .action-banner h4 {{
    font-family: 'Playfair Display', serif;
    font-size: 1.3rem;
    color: var(--gold-light);
    margin-bottom: 4px;
  }}
  .action-banner p {{
    color: var(--text-dim);
    font-size: 0.9rem;
    margin: 0;
  }}
  .btn-banner {{
    background: var(--gold);
    color: #000;
    padding: 12px 24px;
    border-radius: 6px;
    text-decoration: none;
    font-weight: 700;
    font-size: 0.9rem;
  }}
  .btn-banner:hover {{
    background: var(--gold-light);
  }}
</style>
</head>
<body>

<div class="top-nav">
  <a href="index.html" class="btn-back">&larr; {nav_back_text}</a>
  <div class="brand-badge">Глобал Плюс &times; GlobalTeamPartners</div>
</div>

<div class="doc-content">
{content_html}
</div>

<div class="action-banner">
  <div>
    <h4>Готов перейти к действиям?</h4>
    <p>Открой базу 62 предприятий и начни показ шаблонов сайтов с планшета.</p>
  </div>
  <a href="Leads_List.html" class="btn-banner">Открыть Базу Лидов &rarr;</a>
</div>

</body>
</html>
"""

solo_page = render_doc_page("Плейбук Партнера: Стратегия На Земле", "Вернуться в Центр Продаж", "#C5A059", solo_html_content)

with open(os.path.join(WORKSPACE, "Solo_Executive_Strategy.html"), "w", encoding="utf-8") as f:
    f.write(solo_page)
print("Solo_Executive_Strategy.html успешно обновлен с главой о шаблонах сайтов!")

print("\nУСПЕХ! Все страницы успешно сгенерированы и готовы к деплою!")
