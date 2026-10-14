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
TEMPLATES_CATALOG = [
    {
        "id": "tpl-aesthetic",
        "title": "Aesthetic Clinic & Medical Beauty",
        "category": "Медицина, Стоматология & Эстетика",
        "badge": "Видеофон 60fps • AI-Триаж • Онлайн-запись",
        "url": "https://globalteampartners.github.io/aesthetic-clinic-demo/",
        "demo_type": "Кинематографичный портал клиники",
        "desc": "Премиальный медицинский портал с динамическим видеофоном, презентацией врачей, защищенной формой записи и умным триажем симптомов пациента.",
        "features": [
            "Кинематографичный видеофон без задержек на мобильных устройствах",
            "Интерактивный прейскурант и калькулятор комплексного плана лечения",
            "Многоканальный AI-триаж в Telegram и на сайте",
            "Презентация врачей высшей категории и оборудования"
        ],
        "target_leads": "УГМК-Здоровье, Центр косметологии им. Нудельмана, Здоровье 365, Линлайн, Парацельс, Мегадента Клиник, Клиника «Здоровье» & «Дента-Люкс» (Алапаевск)",
        "pitch_talk": "«Посмотрите на сайт вашей клиники: в 8 утра пациент видит статичную страницу и ждет ответа колл-центра. В нашем решении он за 15 секунд выбирает доктора, видит живую клинику и оставляет бронь через Telegram с подтверждением явки 98%»."
    },
    {
        "id": "tpl-auto",
        "title": "Auto Shine | Premium Detailing & Protection",
        "category": "Автобизнес, Детейлинг & Спецтехника",
        "badge": "Canvas-скролл авто • Калькулятор бронепленки",
        "url": "https://globalteampartners.github.io/auto-shine-demo/",
        "demo_type": "Интерактивный сайт детейлинг-студии",
        "desc": "Покадровая анимация оклейки спорткара полиуретановой пленкой SunTek, 3D-демонстрация гидрофобного эффекта керамики, расчет сметы оклейки.",
        "features": [
            "Плавный 60fps скролл автомобиля с подсветкой защитных зон",
            "Калькулятор пакетов: Оклейка переда, Тотальная защита, Керамика 9H",
            "Моментальная запись в бокс с бронированием даты",
            "Галерея макро-съемки качества швов и реставрации кожи"
        ],
        "target_leads": "Detailing Alarm Ekb, Restyle, Порше Центр Екатеринбург, ГК «Автобан», Планета Авто, СТО спецтехники (Синячиха), АвтоЛидер (Алапаевск)",
        "pitch_talk": "«Владельцы премиальных авто выбирают глазами. Когда клиент видит, как на экране интерактивно натягивается пленка и играет свет на кузове — он не спорит о цене, а сразу бронирует бокс на детейлинг»."
    },
    {
        "id": "tpl-realestate",
        "title": "Belgrade Waterfront | Premium Real Estate",
        "category": "Девелопмент, ЖК & Клубные Дома",
        "badge": "Архитектурный скролл • 3D-Планировки • Ипотека",
        "url": "https://globalteampartners.github.io/belgrade-waterfront-demo/",
        "demo_type": "Кинематографичный портал застройщика",
        "desc": "Сайт клубной архитектуры с демонстрацией высотных башен, панорамных видов из окон, виртуальным туром по террасам и AI-ипотечным брокером.",
        "features": [
            "Кинематографичный скролл высоток и фасадных линий",
            "Интерактивная карта жилых кварталов и инфраструктуры",
            "AI-брокер подбора планировок под сценарии жизни семьи",
            "Приватная бронь пентхаусов и коммерческих помещений"
        ],
        "target_leads": "Брусника, Атомстройкомплекс, УГМК-Застройщик (Макаровский, Исеть), Forum Group (Тихвинъ), PRINZIP (Мельница), КОРТРОС Академический, Синара-Девелопмент",
        "pitch_talk": "«Вы тратите миллионы на рекламу жилья, но страницы типовые. Наш портал за 3 секунды влюбляет покупателя: кинематографичный ракурс набережной, 3D-раскладка террасы и закрытый брокерский чат в Telegram»."
    },
    {
        "id": "tpl-horeca",
        "title": "Salon 1905 | Fine Dining & VIP Gastronomy",
        "category": "Премиум HoReCa, Рестораны & Отели",
        "badge": "Видеоряд зала • Выбор столиков • Депозиты",
        "url": "https://globalteampartners.github.io/salon-1905-demo/",
        "demo_type": "Премиальный ресторанный сайт",
        "desc": "Атмосферный кинематографичный портал высокой кухни, винной коллекции, банкетных залов и системы депозитного бронирования столов.",
        "features": [
            "Атмосферный видеоряд подачи авторских блюд шефом",
            "Интерактивная карта рассадки с выбором панорамных столиков",
            "Модуль внесения депозитов онлайн (ликвидация no-show)",
            "Расчет банкетного меню и предварительный заказ вин"
        ],
        "target_leads": "Ресторан Троекуровъ, Kitchen (24 этаж), Сойка, Гастроли, Momo Pan Asian, Небоскреб Высоцкий, Отель & Ресторан «Эрмитаж» (Алапаевск), Гостиница «Металлург», База «Чистые пруды»",
        "pitch_talk": "«В пятницу вечером хостес разрывается между звонками, а 20% броней срываются. В нашей системе гость выбирает столик с видом, вносит депозит за 1 минуту и получает персональное приглашение»."
    },
    {
        "id": "tpl-geotochka",
        "title": "Геоточка — Сеть Точек на Яндекс Картах",
        "category": "Гео-Маркетинг, Сетевой Ритейл & Дилеры",
        "badge": "Локальное SEO • Яндекс Карты • Сеть баз",
        "url": "https://globalteampartners.github.io/geotochka/",
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
        "category": "Франчайзинг, B2B-Дистрибуция & Фабрики",
        "badge": "3D-Производство • Личный кабинет B2B • Франшиза",
        "url": "https://globalteampartners.github.io/tentorium-presentation/",
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
        "id": "tpl-vtvip",
        "title": "Визуализированный Трансфер (VT-VIP)",
        "category": "VIP-Транспорт, Туризм & Спецперевозки",
        "badge": "Парк техники • Бронирование рейсов • Туризм",
        "url": "https://globalteampartners.github.io/vt-vip/",
        "demo_type": "Представительский транспорт & маршруты",
        "desc": "Цифровая платформа заказа представительского трансфера, туристических маршрутов, спецтехники и экскурсионных пакетов с выбором класса обслуживания.",
        "features": [
            "Визуализированный каталог автопарка и подвижного состава",
            "Конструктор туристических маршрутов с остановками и гидом",
            "Моментальный расчет стоимости по километражу и классу комфорта",
            "Онлайн-оплата билетов с получением посадочного талона в мессенджер"
        ],
        "target_leads": "Алапаевская узкоколейная ж/д (АУЖД туризм), Музей деревянного зодчества (Нижняя Синячиха), ООО «Синячиха-Лес» (лесотранспорт), трансферные парки отелей",
        "pitch_talk": "«На АУЖД и в музей Нижней Синячихи едут туристы со всей страны, но они не могут купить билет и выбрать вагон онлайн. Наша система позволяет москвичу или екатеринбуржцу забронировать ретропоезд с телефона за 1 минуту»."
    },
    {
        "id": "tpl-machinery",
        "title": "B2B Heavy Machinery & Equipment Configurator",
        "category": "Машиностроение, Спецтехника & Металл",
        "badge": "3D-Селектор бурилок • Подбор шнеков • Выгрузка КП",
        "url": "demos/machinery-demo/index.html",
        "demo_type": "B2B-конфигуратор промышленного оборудования",
        "desc": "Интерактивный селектор бурильно-крановых машин, подбор бурового инструмента по категориям грунта, кросс-подбор гидромоторов PSM-Hydraulics.",
        "features": [
            "Интерактивный 3D-подбор машин под глубину бурения и тип грунта",
            "Кросс-подбор отечественных аналогов импортной гидравлики",
            "Моментальная генерация заказной спецификации и ТЗ за 15 секунд",
            "Прямая интеграция заявок с отделом сбыта завода и 1С"
        ],
        "target_leads": "АО «Стройдормаш», ООО «ЗИСТ», ООО «Бурмаш», ПАО «Уралмашзавод», УЗГА, Синара СТМ, PSM-Hydraulics, Уральский турбинный завод, СТЗ/ТМК, ВИЗ-Сталь, Котельный завод",
        "pitch_talk": "«Главный конструктор и отдел сбыта тратят недели на согласование опросных листов. В нашей системе энергетик или строитель выбирает категорию грунта, а система сама подбирает бурилку и выкатывает готовое КП»."
    },
    {
        "id": "tpl-wood",
        "title": "УралЛесПром | Оптовый B2B-Портал Древесины",
        "category": "Лесопромышленность & Деревообработка",
        "badge": "Калькулятор партий ГОСТ • Вагонные нормы • 1С",
        "url": "demos/wood-industry-demo/index.html",
        "demo_type": "B2B-портал оптовых поставок фанеры и леса",
        "desc": "Интерактивный калькулятор кубатуры, веса и оптовой стоимости партий березовой фанеры (ФК/ФСФ) и пиломатериалов по ГОСТ с проверкой остатков на складах.",
        "features": [
            "Калькулятор вагонных и фурных партий по ГОСТ 3916.1-96",
            "Автоматический пересчет веса, кубатуры и стоимости с НДС",
            "Моментальная выписка спецификации со счетом для строительных трестов",
            "Прямой трекинг железнодорожных накладных РЖД"
        ],
        "target_leads": "НАО «СВЕЗА Верхняя Синячиха», ООО «Лестех», Верхнесинячихинский лесохим, ООО «Алапаевский ДОЗ» (АДОЗ), Алапаевский лесопромышленный холдинг (АЛХ)",
        "pitch_talk": "«Снабженец из Тюмени или ХМАО хочет заказать 3 фуры фанеры 18 мм в субботу вечером. Вместо ожидания понедельника он вводит объем, видит точный вес партии и получает счет за 10 секунд. Сделка закрыта!»"
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
    <div class="template-card" data-category="{t['category']}">
        <div class="template-header">
            <div>
                <span class="tpl-category">{t['category']}</span>
                <h3 class="tpl-title">{t['title']}</h3>
                <span class="tpl-badge">{t['badge']}</span>
            </div>
            <a href="{t['url']}" target="_blank" class="btn-open-live">Открыть сайт во весь экран ↗</a>
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
            gap: 30px;
        }}
        .template-card {{
            background: var(--bg-surface);
            border: 1px solid var(--border-card);
            border-radius: 16px;
            padding: 32px;
            transition: all 0.3s;
        }}
        .template-card:hover {{
            border-color: var(--gold);
            box-shadow: 0 10px 30px rgba(0,0,0,0.5);
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

    <!-- ФИЛЬТРЫ ПО ОТРАСЛЯМ -->
    <div class="filter-panel">
        <button class="filter-btn active" data-filter="all">Все шаблоны ({len(TEMPLATES_CATALOG)})</button>
        <button class="filter-btn" data-filter="Медицина, Стоматология & Эстетика">Медицина & Стоматология</button>
        <button class="filter-btn" data-filter="Автобизнес, Детейлинг & Спецтехника">Авто & Детейлинг</button>
        <button class="filter-btn" data-filter="Девелопмент, ЖК & Клубные Дома">Девелопмент & ЖК</button>
        <button class="filter-btn" data-filter="Премиум HoReCa, Рестораны & Отели">HoReCa & Рестораны</button>
        <button class="filter-btn" data-filter="Гео-Маркетинг, Сетевой Ритейл & Дилеры">Гео-Маркетинг</button>
        <button class="filter-btn" data-filter="Франчайзинг, B2B-Дистрибуция & Фабрики">Производство & Фабрики</button>
        <button class="filter-btn" data-filter="VIP-Транспорт, Туризм & Спецперевозки">Транспорт & Туризм</button>
        <button class="filter-btn" data-filter="Машиностроение, Спецтехника & Металл">Машиностроение</button>
        <button class="filter-btn" data-filter="Лесопромышленность & Деревообработка">Лесопром & Фанера</button>
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
            document.querySelectorAll('.template-card').forEach(card => {{
                if (cat === 'all' || card.getAttribute('data-category') === cat) {{
                    card.style.display = 'block';
                }} else {{
                    card.style.display = 'none';
                }}
            }});
        }});
    }});
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
            background: var(--bg-surface);
            border: 1px solid var(--border-card);
            border-radius: 12px;
            padding: 24px;
            transition: all 0.3s;
        }}
        .demo-card:hover {{
            border-color: rgba(197, 160, 89, 0.5);
            transform: translateY(-4px);
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
            <div class="stat-num">9</div>
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
                <h3 class="card-title">Каталог Шаблонов Global Plus <span class="badge-hot">НОВОЕ</span></h3>
                <p class="card-desc">Реальные кинематографичные сайты с видеофоном, скроллом и формами по отраслям (Медицина, Детейлинг, Девелопмент, HoReCa, Гео-карты, Заводы). Открывай на планшете перед директорами.</p>
            </div>
            <a href="Templates_Catalog.html" class="btn-card">
                <span>Смотреть 9 Шаблонов Сайтов</span>
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
            <div class="demo-title">💉 Медицина &amp; Эстетика</div>
            <div class="demo-subtitle">УГМК-Здоровье, Нудельман — кинематографичный портал клиники с видеофоном</div>
            <a href="https://globalteampartners.github.io/aesthetic-clinic-demo/" class="demo-link" target="_blank">
                <span>Открыть Сайт Aesthetic Clinic</span>
                <span>&nearr;</span>
            </a>
        </div>

        <div class="demo-card">
            <div class="demo-title">🏎️ Авто &amp; Детейлинг</div>
            <div class="demo-subtitle">Detailing Alarm, Порше Центр, Автобан — 60fps скролл авто и бронепленка</div>
            <a href="https://globalteampartners.github.io/auto-shine-demo/" class="demo-link" target="_blank">
                <span>Открыть Сайт Auto Shine</span>
                <span>&nearr;</span>
            </a>
        </div>

        <div class="demo-card">
            <div class="demo-title">🏙️ Девелопмент &amp; Премиум ЖК</div>
            <div class="demo-subtitle">Брусника, Атом, УГМК-Застройщик — кинематографичный архитектурный портал</div>
            <a href="https://globalteampartners.github.io/belgrade-waterfront-demo/" class="demo-link" target="_blank">
                <span>Открыть Сайт Belgrade Waterfront</span>
                <span>&nearr;</span>
            </a>
        </div>

        <div class="demo-card">
            <div class="demo-title">🍷 Премиум HoReCa &amp; Отели</div>
            <div class="demo-subtitle">Троекуров, Kitchen, Высоцкий — видеоряд залов и VIP-бронь столов</div>
            <a href="https://globalteampartners.github.io/salon-1905-demo/" class="demo-link" target="_blank">
                <span>Открыть Сайт Salon 1905</span>
                <span>&nearr;</span>
            </a>
        </div>

        <div class="demo-card">
            <div class="demo-title">📍 Геоточка &amp; Ритейл</div>
            <div class="demo-subtitle">Талицкое молоко, СМАК, Черкашин — карта точек на Яндекс Картах</div>
            <a href="https://globalteampartners.github.io/geotochka/" class="demo-link" target="_blank">
                <span>Открыть Сайт Геоточка</span>
                <span>&nearr;</span>
            </a>
        </div>

        <div class="demo-card">
            <div class="demo-title">🏭 Заводы &amp; Дистрибуция</div>
            <div class="demo-subtitle">Птицефабрика, АМК, Alma Ceramica — 3D-презентация производства</div>
            <a href="https://globalteampartners.github.io/tentorium-presentation/" class="demo-link" target="_blank">
                <span>Открыть Сайт Тенториум</span>
                <span>&nearr;</span>
            </a>
        </div>

        <div class="demo-card">
            <div class="demo-title">🌲 Лесопромышленный B2B-Портал</div>
            <div class="demo-subtitle">СВЕЗА, Лестех, АДОЗ, АЛХ — калькулятор партий фанеры и пиломатериалов</div>
            <a href="demos/wood-industry-demo/index.html" class="demo-link" target="_blank">
                <span>Открыть Калькулятор Фанеры</span>
                <span>&nearr;</span>
            </a>
        </div>

        <div class="demo-card">
            <div class="demo-title">⚙️ Спецтехника &amp; Машиностроение</div>
            <div class="demo-subtitle">Стройдормаш, ЗИСТ, PSM — 3D-конфигуратор бурилок и подбор гидромоторов</div>
            <a href="demos/machinery-demo/index.html" class="demo-link" target="_blank">
                <span>Открыть 3D-Конфигуратор</span>
                <span>&nearr;</span>
            </a>
        </div>

        <div class="demo-card">
            <div class="demo-title">🚂 Туризм &amp; VIP-Трансфер</div>
            <div class="demo-subtitle">АУЖД, Музей Синячихи, отели — интерактивная продажа турпакетов онлайн</div>
            <a href="https://globalteampartners.github.io/vt-vip/" class="demo-link" target="_blank">
                <span>Открыть Сайт VT-VIP</span>
                <span>&nearr;</span>
            </a>
        </div>

    </div>

</div>

<footer>
    <p>&copy; 2026 Глобал Плюс &times; Global Team Partners. Конфиденциальный комплект регионального развития.</p>
    <p style="margin-top: 8px; opacity: 0.7;">Разработано для стратегического партнера в Свердловской области (Верхняя Синячиха &bull; Алапаевск &bull; Екатеринбург).</p>
</footer>

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
    <div style="font-size: 0.85rem; color: var(--gold);">Региональный охват: 62 ключевых предприятия &bull; 9 шаблонов сайтов</div>
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

<div class="watermark">
    <span>ГЛОБАЛ ПЛЮС &times; GLOBAL TEAM PARTNERS</span>
    <a href="Leads_List.html" class="btn-exit">&larr; В базу лидов</a>
</div>

<!-- СЛАЙД 0: ТИТУЛ -->
<div class="slide active" id="slide0">
    <div class="pill-tag">СТРАТЕГИЧЕСКОЕ ПРЕДЛОЖЕНИЕ 2026</div>
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
    document.title = currentCompany.name + " — Стратегическая Презентация";

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
        .btn-print {{ display: none; }}
    }}
</style>
</head>
<body>

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

| Отрасль и Клиент | Шаблон Сайта Global Plus | Что показать на экране за 15 секунд |
|---|---|---|
| **Клиники & Стоматология** (УГМК-Здоровье, Нудельман, Дента-Люкс) | [Aesthetic Clinic](https://globalteampartners.github.io/aesthetic-clinic-demo/) | Покажи живой видеофон операционной, онлайн-калькулятор плана лечения и форму записи врача. |
| **Детейлинг & Премиум Авто** (Detailing Alarm, Порше Центр, Автобан) | [Auto Shine Detailing](https://globalteampartners.github.io/auto-shine-demo/) | Проведи пальцем по экрану: автомобиль плавно поворачивается в 60fps, подсвечиваются зоны оклейки полиуретаном. |
| **Девелопмент & ЖК** (Брусника, Атом, УГМК-Застройщик, Forum Group) | [Belgrade Waterfront](https://globalteampartners.github.io/belgrade-waterfront-demo/) | Покажи скролл клубных башен, панорамные виды на водоем и виртуальный выбор планировок. |
| **Рестораны & Банкеты** (Троекуров, Kitchen, Высоцкий, Эрмитаж) | [Salon 1905 Fine Dining](https://globalteampartners.github.io/salon-1905-demo/) | Покажи видео подачи блюд шефом, выбор панорамного столика и онлайн-депозит. |
| **Ритейл & Молоко/Мясо** (Талицкое молоко, СМАК, Черкашин, АМК) | [Геоточка (Яндекс Карты)](https://globalteampartners.github.io/geotochka/) | Покажи карту присутствия с автоматическим нахождением ближайшей точки свежей продукции. |
| **Фабрики & Франшизы** (Птицефабрика, Alma Ceramica, АДОЗ, АЛХ) | [Тенториум Фабрика](https://globalteampartners.github.io/tentorium-presentation/) | Покажи 3D-тур по цехам, экологический контроль качества и кабинет оптовика. |
| **Туризм & Маршруты** (АУЖД узкоколейка, Музей Синячихи, отели) | [VT-VIP Трансфер](https://globalteampartners.github.io/vt-vip/) | Покажи онлайн-покупку билетов на поезд/экскурсию с выбором вагона и гида. |

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
