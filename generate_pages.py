# -*- coding: utf-8 -*-
"""
Генератор всех страниц Sales Kit для Димы (Глобал Плюс × GlobalTeamPartners)
"""
import os
import json
import sys

if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

WORKSPACE = r"c:\Users\Vlaslav\Downloads\Дима Верхняя Синичиха Алапаевск"

with open(os.path.join(WORKSPACE, "companies_database.json"), "r", encoding="utf-8") as f:
    COMPANIES = json.load(f)

# Группировка по секторам для каталога и фильтров
SECTORS = sorted(list(set(c["sector"] for c in COMPANIES)))
REGIONS = ["Верхняя Синячиха", "Алапаевск и район", "Екатеринбург"]

print(f"Загружено {len(COMPANIES)} компаний из {len(SECTORS)} секторов и {len(REGIONS)} регионов.")

# ==============================================================================
# 1. ГЕНЕРАЦИЯ index.html (Главный Хаб)
# ==============================================================================
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
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
            position: relative;
            overflow: hidden;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
        }}
        .hub-card:hover {{
            transform: translateY(-6px);
            border-color: var(--gold);
            box-shadow: 0 20px 35px rgba(0, 0, 0, 0.4), 0 0 25px rgba(197, 160, 89, 0.1);
        }}
        .hub-card::before {{
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 4px;
            background: var(--card-accent, var(--gold));
        }}
        .hub-card.lead-database {{ --card-accent: var(--gold); }}
        .hub-card.strategy {{ --card-accent: var(--red); }}
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
    <p class="subtitle">Интегрированная система экспансии и коммерческих предложений: Верхняя Синячиха &bull; Алапаевск &bull; Екатеринбург</p>
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
            <div class="stat-num">3</div>
            <div class="stat-label">Географических пояса</div>
        </div>
        <div class="stat-card">
            <div class="stat-num">48 ч</div>
            <div class="stat-label">Запуск прототипа</div>
        </div>
        <div class="stat-card">
            <div class="stat-num">100%</div>
            <div class="stat-label">Ориентация на результат</div>
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
                <p class="card-desc">Полный реестр целевых заводов, комбинатов, девелоперов, клиник и ресторанов Синячихи, Алапаевска и Екатеринбурга. Точные ЛПР, выявленные боли, готовые питчи "Троянского коня".</p>
            </div>
            <a href="Leads_List.html" class="btn-card">
                <span>Открыть Базу Лидов (62 компании)</span>
                <span>&rarr;</span>
            </a>
        </div>

        <!-- КАРТОЧКА 2: ПЛЕЙБУК ДИМЫ -->
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

        <!-- КАРТОЧКА 3: БЫСТРЫЕ СКРИПТЫ -->
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

        <!-- КАРТОЧКА 4: 62 ПИТЧА И ЦЕНЫ -->
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

        <!-- КАРТОЧКА 5: СТРАТЕГИЯ БРЕНДОВ -->
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

        <!-- КАРТОЧКА 6: АНАЛИЗ РЫНКА -->
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

    <!-- ГОТОВЫЕ ИНТЕРАКТИВНЫЕ ДЕМО-ОБРАЗЦЫ -->
    <h2 class="section-heading">🌐 Живые Демо-Прототипы Для Показа На Встречах</h2>
    <p style="color: var(--text-dim); margin-top: -15px; margin-bottom: 25px;">Открывай прямо со смартфона или планшета перед директором — это снимает 90% сомнений за 30 секунд.</p>

    <div class="demo-grid">

        <div class="demo-card">
            <div class="demo-title">🌲 Лесопромышленный B2B-Портал</div>
            <div class="demo-subtitle">СВЕЗА, Лестех, АДОЗ, АЛХ — калькулятор партий фанеры и пиломатериалов</div>
            <a href="demos/wood-industry-demo/index.html" class="demo-link" target="_blank">
                <span>Открыть Интерактивное Демо</span>
                <span>&nearr;</span>
            </a>
        </div>

        <div class="demo-card">
            <div class="demo-title">⚙️ Спецтехника &amp; Машиностроение</div>
            <div class="demo-subtitle">Стройдормаш, ЗИСТ, PSM — 3D-конфигуратор бурилок и подбор гидромоторов</div>
            <a href="demos/machinery-demo/index.html" class="demo-link" target="_blank">
                <span>Открыть Интерактивное Демо</span>
                <span>&nearr;</span>
            </a>
        </div>

        <div class="demo-card">
            <div class="demo-title">🏙️ Девелопмент &amp; Премиум ЖК</div>
            <div class="demo-subtitle">Брусника, Атом, УГМК-Застройщик — 3D-планировки, ипотека и бронирование</div>
            <a href="demos/real-estate-demo/index.html" class="demo-link" target="_blank">
                <span>Открыть Интерактивное Демо</span>
                <span>&nearr;</span>
            </a>
        </div>

        <div class="demo-card">
            <div class="demo-title">🍷 Премиум HoReCa &amp; Отели</div>
            <div class="demo-subtitle">Троекуров, Kitchen, Hyatt — VIP-бронь столов, залов и AI-депозиты</div>
            <a href="demos/horeca-demo/index.html" class="demo-link" target="_blank">
                <span>Открыть Интерактивное Демо</span>
                <span>&nearr;</span>
            </a>
        </div>

        <div class="demo-card">
            <div class="demo-title">💉 Медицина &amp; Эстетика</div>
            <div class="demo-subtitle">УГМК-Здоровье, Нудельман — онлайн-триаж, запись и калькулятор лечения</div>
            <a href="demos/medical-demo/index.html" class="demo-link" target="_blank">
                <span>Открыть Интерактивное Демо</span>
                <span>&nearr;</span>
            </a>
        </div>

        <div class="demo-card">
            <div class="demo-title">📦 B2B Поставки &amp; Сервисы</div>
            <div class="demo-subtitle">Черкашин, СМАК, АУЖД, ФОК — личные кабинеты оптовиков и онлайн-касса</div>
            <a href="demos/service-demo/index.html" class="demo-link" target="_blank">
                <span>Открыть Интерактивное Демо</span>
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
print("index.html успешно создан!")

# ==============================================================================
# 2. ГЕНЕРАЦИЯ Leads_List.html (Интерактивная база лидов)
# ==============================================================================
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
        <td style="font-size:0.85rem; color:#E2E8F0;">{c['trojan_pitch']}</td>
        <td style="white-space:nowrap;">
            <a href="Dynamic_Pitch_Deck.html?id={c['id']}" target="_blank" class="btn-action btn-deck" title="Открыть презентацию">📊 Слайды</a>
            <a href="Dynamic_One_Pager.html?id={c['id']}" target="_blank" class="btn-action btn-pager" title="Открыть КП-одностраничник">📄 1-Pager</a>
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
            max-width: 1300px;
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
            max-width: 1300px;
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
        .search-box {{
            width: 100%;
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
            flex-wrap: wrap;
            gap: 8px;
            align-items: center;
        }}
        .filter-label {{
            font-size: 0.8rem;
            color: var(--gold);
            text-transform: uppercase;
            letter-spacing: 1px;
            font-weight: 700;
            margin-right: 8px;
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
            overflow-x: auto;
            background: var(--bg-surface);
            border: 1px solid var(--border-card);
            border-radius: 12px;
        }}
        table {{
            width: 100%;
            border-collapse: collapse;
            text-align: left;
            font-size: 0.9rem;
        }}
        th {{
            background: #18202E;
            color: var(--gold-light);
            padding: 14px 16px;
            font-weight: 600;
            border-bottom: 2px solid var(--border);
            white-space: nowrap;
        }}
        td {{
            padding: 16px;
            border-bottom: 1px solid rgba(255, 255, 255, 0.05);
            vertical-align: middle;
        }}
        tr:hover td {{
            background: rgba(255, 255, 255, 0.02);
        }}
        .badge {{
            display: inline-block;
            padding: 4px 10px;
            border-radius: 6px;
            font-size: 0.75rem;
            font-weight: 600;
            white-space: nowrap;
        }}
        .bg-wood {{ background: rgba(16, 185, 129, 0.15); color: #34D399; border: 1px solid rgba(16, 185, 129, 0.3); }}
        .bg-machine {{ background: rgba(59, 130, 246, 0.15); color: #60A5FA; border: 1px solid rgba(59, 130, 246, 0.3); }}
        .bg-realestate {{ background: rgba(234, 179, 8, 0.15); color: #FACC15; border: 1px solid rgba(234, 179, 8, 0.3); }}
        .bg-horeca {{ background: rgba(217, 70, 239, 0.15); color: #E879F9; border: 1px solid rgba(217, 70, 239, 0.3); }}
        .bg-medical {{ background: rgba(239, 68, 68, 0.15); color: #F87171; border: 1px solid rgba(239, 68, 68, 0.3); }}
        .bg-auto {{ background: rgba(20, 184, 166, 0.15); color: #2DD4BF; border: 1px solid rgba(20, 184, 166, 0.3); }}
        .bg-food {{ background: rgba(249, 115, 22, 0.15); color: #FB923C; border: 1px solid rgba(249, 115, 22, 0.3); }}
        .bg-service {{ background: rgba(168, 85, 247, 0.15); color: #C084FC; border: 1px solid rgba(168, 85, 247, 0.3); }}

        .region-pill {{
            background: rgba(255, 255, 255, 0.08);
            color: #fff;
            padding: 3px 8px;
            border-radius: 4px;
            font-size: 0.75rem;
            white-space: nowrap;
        }}
        .persona-tag {{
            color: var(--gold-light);
            font-size: 0.8rem;
            font-weight: 500;
        }}
        .btn-action {{
            display: inline-block;
            padding: 6px 10px;
            border-radius: 4px;
            text-decoration: none;
            font-size: 0.75rem;
            font-weight: 600;
            margin-right: 4px;
            transition: all 0.2s;
        }}
        .btn-deck {{
            background: rgba(197, 160, 89, 0.2);
            color: var(--gold-light);
            border: 1px solid rgba(197, 160, 89, 0.4);
        }}
        .btn-deck:hover {{
            background: var(--gold);
            color: #000;
        }}
        .btn-pager {{
            background: rgba(255, 255, 255, 0.08);
            color: #fff;
            border: 1px solid var(--border-card);
        }}
        .btn-pager:hover {{
            background: #fff;
            color: #000;
        }}
    </style>
</head>
<body>

<div class="top-nav">
    <a href="index.html" class="btn-back">&larr; Вернуться в Центр Продаж</a>
    <div style="font-size: 0.85rem; color: var(--gold);">Региональный охват: 62 ключевых предприятия</div>
</div>

<div class="container">
    <h1>📋 Единая База 62 Целевых Предприятий</h1>
    <p class="subtitle">Верхняя Синячиха &bull; Алапаевск &bull; Екатеринбург | Готовые точки входа, ЛПР и персонализированные предложения</p>

    <!-- ПАНЕЛЬ ПОИСКА И ФИЛЬТРАЦИИ -->
    <div class="controls-panel">
        <div class="search-box">
            <input type="text" id="searchInput" placeholder="🔍 Быстрый поиск по названию, специализации или предложению...">
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
        </div>
    </div>

    <!-- ТАБЛИЦА БАЗЫ ДАННЫХ -->
    <div class="table-responsive">
        <table id="leadsTable">
            <thead>
                <tr>
                    <th style="min-width: 240px;">Предприятие / Бренд</th>
                    <th>Локация</th>
                    <th>Отрасль</th>
                    <th>Целевое ЛПР</th>
                    <th style="min-width: 300px;">Питч "Троянского коня"</th>
                    <th>Инструменты Димы</th>
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
print("Leads_List.html успешно создан!")

# ==============================================================================
# 3. ГЕНЕРАЦИЯ Solo_Executive_Strategy.html (Плейбук для Димы)
# ==============================================================================
strategy_md = """# 🐺 Плейбук Регионального Директора: Экспансия на Урале
### Практическое руководство для Дмитрия (Глобал Плюс &times; GlobalTeamPartners)

> **Миссия:** Построить в Свердловской области (Верхняя Синячиха, Алапаевск, Екатеринбург) системный пул из 15–25 постоянных корпоративных клиентов на цифровизацию, автоматизацию сбыта и внедрение ИИ-решений. Ты — не продавец веб-сайтов, а **партнер международной IT-группы Global Plus**, который приносит уральским предприятиям рост маржи и решение острейшей проблемы кадрового голода.

---

## ♟️ 1. Позиционирование Дмитрия

Когда ты заходишь на завод или в кабинет генерального директора, твоя позиция:
* ❌ **Как не надо:** *"Здравствуйте, мы веб-студия, делаем сайты и чат-боты, вам случайно не нужно обновить сайт?"* (Сразу отправят к секретарю или сисадмину).
*  **Как надо:** *"Добрый день, [Имя Отчество]. Я Дмитрий, региональный партнер технологической группы Глобал Плюс / GlobalTeamPartners. Мы автоматизируем отделы сбыта и внедряем ИИ-инфраструктуру для промышленных предприятий и лидеров рынка. Я изучил ваши процессы: ваши менеджеры теряют до 30% оптовых заявок в нерабочее время, а кадровый дефицит тормозит отгрузки. Моя команда уже собрала для вашего предприятия готовый цифровой прототип. Уделите мне 60 секунд на планшете."*

**Твой образ:** Уверенный, деловой, свой человек на Урале, который говорит на языке цифр, рентабельности и конкретики, за спиной которого стоит мощная международная инженерная команда.

---

## 🛠️ 2. Методология "Троянский Конь": 3 Шага к Сделке

```
[Шаг 1: Разведка] ➡️ [Шаг 2: Прототип за 48 часов] ➡️ [Шаг 3: Абонентский контракт]
  (Боль & Цифры)         (Шок от скорости на iPad)            (LTV: 50–200 тыс/мес)
```

### 🟢 Шаг 1: Разведка и точечный диагноз
Перед встречей открой `Leads_List.html` и выбери предприятие. 
* В Синячихе и Алапаевске ты знаешь заводы лично. Найди слабое место: не отвечает телефон вечером, нет онлайн-расчета кубатуры древесины или массы металлопроката, старый прайс в формате PDF 2021 года, дефицит рабочих рук.
* Сформулируй потерю: *"Вы теряете минимум 500 000 рублей в месяц на том, что крупный оптовик из Тюмени или Москвы не может мгновенно получить счет в субботу вечером и уходит к конкурентам".*

### 🟡 Шаг 2: Быстрый старт (Прототип за 48 часов)
У тебя уже есть открытые на планшете/смартфоне интерактивные демо-образцы:
* Для лесопереработки: **Лесопромышленный B2B-портал** с калькулятором партий.
* Для бурильщиков и машиностроителей: **Портал спецтехники** с 3D-подбором шнеков.
* Для застройщиков: **Кинематографичный девелоперский сайт** с 3D-планировками.
* Для ресторанов и отелей: **VIP-система бронирования столиков и банкетов**.
* Для клиник: **AI-триаж и онлайн-запись**.

Ты протягиваешь планшет:
> *"Посмотрите, вот так должен работать ваш отдел сбыта в 2026 году. Клиент выбирает объем партии за 10 секунд, система автоматически проверяет склад и формирует спецификацию. Мы не просим вас платить миллионы за годовую разработку. Мы запускаем пилот за 48 часов на ваших данных".*

### 🔴 Шаг 3: Перевод на долгосрочное абонентское сопровождение (LTV)
После запуска базового прототипа ты не уходишь:
* *"Теперь, когда система собирает заявки круглосуточно, мы подключаем ИИ-ассистента в Telegram, интегрируем всё с вашей 1С или CRM и обеспечиваем полную техническую поддержку 24/7"*.
* Фиксируешь абонентскую плату: от **35 000 до 150 000 руб./месяц** с каждого предприятия.
* 10 предприятий на абонентке = **от 500 000 до 1 500 000 руб. чистой ежемесячной выручки**!

---

## 📅 3. Месячный Ритм Работы Димы

### Неделя 1: Локальный блицкриг (Верхняя Синячиха & Алапаевск)
* Отработай 10–15 ключевых местных предприятий (Свеза, Лестех, Стройдормаш, ЗИСТ, АДОЗ, АЛХ, Молочный комбинат, Металлург).
* Преимущество: ты рядом, можешь приехать на завод в течение часа, встретиться лично за чаем или в цеху.
* Цель: 3 пилотных внедрения в родном районе.

### Неделя 2: Выход на средний чек Екатеринбурга (HoReCa, Авто, Медицина)
* Назначь встречи в Екатеринбурге на четверг и пятницу (по 3–4 встречи в день в центре: Радищева, 8 Марта, Ленина, БЦ Высоцкий).
* Зайди в знаковые рестораны (Троекуров, Kitchen, Сойка), клиники (УГМК-Здоровье, Нудельман), детейлинг-центры.
* Показывай экраны на iPad: рестораторы и главврачи реагируют мгновенно.

### Неделя 3: Промышленные гиганты и Девелоперы Екатеринбурга
* Встречи с коммерческими директорами застройщиков (Брусника, Атомстройкомплекс, Prinzip) и машиностроителей (Пневмостроймашина, УЗГА, Уралмашзавод).
* Демонстрация AI-брокеров, ипотечных калькуляторов и B2B-конфигураторов оборудования.

### Неделя 4: Финализация договоров и сбор предоплат
* Подписание сервисных контрактов, настройка доменов, передача технических ТЗ инженерам Global Plus, получение первых абонентских оплат.

---

## 🎯 4. Золотые Правила Уральских Переговоров
1. **Никакой воды и модных англицизмов.** Говори просто: не "омниканальный customer journey", а *"клиент нажимает кнопку, через 5 секунд ему в WhatsApp приходит готовый расчет, а вашему снабженцу падает уведомление"*.
2. **Уважай производственников.** Директора заводов Алапаевска и Синячихи выросли на производстве. Покажи уважение к их продукции, пойми сложность их технологического цикла.
3. **Держи слово.** На Урале репутация строится годами, а теряется за один сорванный срок. Пообещал запустить демо в пятницу в 12:00 — покажи в 11:30.
"""

strategy_html = f"""<!DOCTYPE html>
<html lang="ru">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Плейбук Партнера: Стратегия На Земле | Глобал Плюс</title>
<script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,600;0,700;1,400&family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
<style>
  body {{ font-family: 'Inter', sans-serif; background: #0B0E14; color: #F8FAFC; padding: 40px 20px; max-width: 860px; margin: 0 auto; line-height: 1.7; }}
  h1, h2, h3 {{ color: #C5A059; font-family: 'Playfair Display', serif; margin-top: 1.5em; margin-bottom: 0.5em; }}
  h1 {{ font-size: 2.4rem; line-height: 1.2; margin-top: 0; }}
  a {{ color: #D32F2F; text-decoration: none; font-weight: bold; }}
  .btn-back {{ display: inline-flex; align-items: center; gap: 8px; margin-bottom: 30px; padding: 10px 20px; background: #D32F2F; color: #fff; text-decoration: none; border-radius: 6px; font-weight: bold; font-size: 0.9rem; transition: 0.2s; }}
  .btn-back:hover {{ background: #B71C1C; }}
  hr {{ border: 0; height: 1px; background: rgba(197,160,89,0.25); margin: 35px 0; }}
  li {{ margin-bottom: 12px; color: #CBD5E1; }}
  blockquote {{ background: rgba(255,255,255,0.04); padding: 18px 24px; border-left: 4px solid #C5A059; margin: 25px 0; border-radius: 0 8px 8px 0; font-size: 1.05rem; }}
  strong {{ color: #fff; }}
  code {{ background: rgba(255,255,255,0.1); padding: 2px 6px; border-radius: 4px; font-family: monospace; color: #E0C07A; }}
  pre {{ background: #121721; padding: 16px; border-radius: 8px; overflow-x: auto; border: 1px solid rgba(255,255,255,0.08); margin: 20px 0; }}
</style>
</head>
<body>
<a href="index.html" class="btn-back">&larr; Вернуться в Центр Продаж</a>
<div id="content"></div>
<script>
  const markdownText = `{strategy_md}`;
  document.getElementById('content').innerHTML = marked.parse(markdownText);
</script>
</body>
</html>
"""

with open(os.path.join(WORKSPACE, "Solo_Executive_Strategy.html"), "w", encoding="utf-8") as f:
    f.write(strategy_html)
print("Solo_Executive_Strategy.html успешно создан!")

# ==============================================================================
# 4. ГЕНЕРАЦИЯ Fast_Collab_Pitches.html (Скрипты звонков и переписок)
# ==============================================================================
scripts_md = """# 🚀 Скрипты Первого Контакта & Быстрых Сделок
### Алгоритмы звонков, сообщений в WhatsApp/Telegram и отработка возражений

> **Цель скриптов:** Не продать сайт по телефону, а продать **15 минут личной встречи с показом живого прототипа на планшете**.

---

## 📞 Блок 1: Телефонные Звонки Директорам Заводов

### Скрипт 1: Обход секретаря / приемной завода
* **Секретарь:** *"Завод 'Стройдормаш', приемная, слушаю вас."*
* **Дима:** *"Добрый день! Соедините, пожалуйста, с коммерческим директором или директором по развитию. Это Дмитрий из технологической группы Глобал Плюс. Мы подготовили расчет по цифровизации приема оптовых заказов на спецтехнику, вопрос по плановым отгрузкам."*
* **Секретарь:** *"Отправьте ваше коммерческое на почту info@..."*
* **Дима:** *"На info@ отправляют типовой спам. У нас не спам, а персональная инженерная разработка под ваше производство. Я сейчас нахожусь в Алапаевске, мне нужно передать материалы лично руководителю. Как зовут коммерческого директора?"*
* **Результат:** Получаешь ФИО и прямой контакт.

---

### Скрипт 2: Прямой звонок руководителю (Директор / Собственник)
* **Дима:** *"Здравствуйте, [Имя Отчество]! Меня зовут Дмитрий, представляю уральский офис IT-группы Глобал Плюс. Звоню коротко по делу на 60 секунд."*
* **ЛПР:** *"Слушаю, что у вас?"*
* **Дима:** *"Мы проанализировали работу отделов сбыта в Свердловской области. Крупные предприятия сейчас теряют до трети оптовых заявок в вечернее время и выходные дни, потому что заказчикам приходится ждать понедельника для расчета спецификаций. Моя команда за 48 часов разработала готовый интерактивный B2B-модуль специально под вашу продукцию [назвать продукцию: фанера / шнеки / сваи / керамогранит]. Я хочу подъехать к вам на 15 минут в среду, открыть планшет и показать, как вы начнете забирать клиентов у конкурентов. В среду в 11:00 или в 15:00 вам удобнее?"*

---

## 💬 Блок 2: Сообщения в WhatsApp / Telegram (Для ЛПР)

### Шаблон 1: Для производственников (Лесопереработка, Металл, Машиностроение)
> *«[Имя Отчество], добрый день! Меня зовут Дмитрий, партнер группы Глобал Плюс. Мы специализируемся на внедрении цифровых систем сбыта для уральской промышленности.*
> 
> *Заметили, что ваши оптовые клиенты не могут мгновенно рассчитать объем партии и стоимость доставки на сайте во внерабочее время. Чтобы не быть голословными, мы собрали живой интерактивный прототип B2B-калькулятора под вашу номенклатуру: [Ссылка на демо-портал].*
> 
> *Готов встретиться на 15 минут в [Алапаевске / Екатеринбурге], чтобы показать, как эта система экономит до 100 часов работы отдела сбыта в месяц. Завтра будет время для короткой встречи?»*

---

### Шаблон 2: Для застройщиков и девелоперов Екатеринбурга
> *«[Имя], добрый день! Изучили воронку продаж вашего ЖК [Название]. При текущей стоимости клика в контексте каждый упущенный лид обходится вам от 4 000 до 8 000 рублей.*
> 
> *Мы разработали кинематографичный формат презентации планировок с виртуальным AI-брокером: [Ссылка на девелоперское демо]. Конверсия в просмотр квартир вырастает на 25-30%.*
> 
> *Буду в центре Екатеринбурга в четверг, с удовольствием покажу метрики на iPad. Какой слот времени вам удобен?»*

---

### Шаблон 3: Для ресторанов и отелей (HoReCa)
> *«[Имя], приветствую! Ресторан [Название] — безусловный лидер по кухне, но ваши гости до сих пор вынуждены звонить администратору в пятницу вечером, чтобы узнать о наличии столиков, или ждать ответа в директ.*
> 
> *Мы внедрили систему моментального бронирования с депозитами и умным Telegram-консьержем: [Ссылка на демо HoReCa]. No-show падает до нуля, а средний чек банкетов растет на 20%.*
> 
> *Давайте выпьем кофе у вас в заведении в среду, покажу систему в действии за 5 минут.»*

---

## 🛡️ Блок 3: Отработка 10 Главных Возражений

1. **«У нас уже есть свой программист / сисадмин»**
   * *Ответ:* «Сисадмин обслуживает серверы и сеть, а штатные программисты перегружены поддержкой 1С. Мы не меняем ваших людей, а даем им готовый внешний конверсионный инструмент, который начинает приносить деньги со следующей недели, не отвлекая ваших IT-специалистов».

2. **«Сейчас не до этого, кризис / не сезон»**
   * *Ответ:* «Именно в несезон выигрывает тот, кто забирает каждую входящую заявку круглосуточно. Пока конкуренты спят, ваш умный портал выдает коммерческие предложения оптовикам за 10 секунд».

3. **«Нам это не нужно, нас все и так знают в районе»**
   * *Ответ:* «В Синячихе и Алапаевске вас знают, но деньги лежат в крупных контрактах из Екатеринбурга, Тюмени, Сургута и Москвы. А там снабженцы выбирают тех, у кого понятный цифровой сервис и моментальный расчет».

4. **«Это слишком дорого»**
   * *Ответ:* «Мы не продаем разработку за миллионы. Базовый запуск стоит меньше, чем зарплата одного помощника менеджера по продажам за месяц. При этом окупаемость наступает уже с первой крупной отгрузки».

5. **«Пришлите на почту, мы посмотрим»**
   * *Ответ:* «На почте лежит 50 непрочитанных писем от спамеров. Я ценю ваше время: откройте ссылку с телефона прямо сейчас на 30 секунд. Вы увидите ваше предприятие в новом формате».
"""

scripts_html = f"""<!DOCTYPE html>
<html lang="ru">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Скрипты Первого Контакта & Питчи | Глобал Плюс</title>
<script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,600;0,700;1,400&family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
<style>
  body {{ font-family: 'Inter', sans-serif; background: #0B0E14; color: #F8FAFC; padding: 40px 20px; max-width: 860px; margin: 0 auto; line-height: 1.7; }}
  h1, h2, h3 {{ color: #C5A059; font-family: 'Playfair Display', serif; margin-top: 1.5em; margin-bottom: 0.5em; }}
  h1 {{ font-size: 2.3rem; line-height: 1.2; margin-top: 0; }}
  a {{ color: #10B981; text-decoration: none; font-weight: bold; }}
  .btn-back {{ display: inline-flex; align-items: center; gap: 8px; margin-bottom: 30px; padding: 10px 20px; background: #10B981; color: #000; text-decoration: none; border-radius: 6px; font-weight: bold; font-size: 0.9rem; transition: 0.2s; }}
  .btn-back:hover {{ background: #059669; color: #fff; }}
  hr {{ border: 0; height: 1px; background: rgba(197,160,89,0.25); margin: 35px 0; }}
  li {{ margin-bottom: 12px; color: #CBD5E1; }}
  blockquote {{ background: rgba(16, 185, 129, 0.08); padding: 18px 24px; border-left: 4px solid #10B981; margin: 25px 0; border-radius: 0 8px 8px 0; font-size: 1.05rem; }}
  strong {{ color: #fff; }}
  code {{ background: rgba(255,255,255,0.1); padding: 2px 6px; border-radius: 4px; font-family: monospace; color: #E0C07A; }}
</style>
</head>
<body>
<a href="index.html" class="btn-back">&larr; Вернуться в Центр Продаж</a>
<div id="content"></div>
<script>
  const markdownText = `{scripts_md}`;
  document.getElementById('content').innerHTML = marked.parse(markdownText);
</script>
</body>
</html>
"""

with open(os.path.join(WORKSPACE, "Fast_Collab_Pitches.html"), "w", encoding="utf-8") as f:
    f.write(scripts_html)
print("Fast_Collab_Pitches.html успешно создан!")

# ==============================================================================
# 5. ГЕНЕРАЦИЯ Comprehensive_Pitches.html (Каталог 62 офферов)
# ==============================================================================
cards_pitches = []
for c in COMPANIES:
    card = f"""
    <div class="pitch-card" id="{c['id']}">
        <div class="pitch-header">
            <div>
                <span class="region-tag">{c['region']}</span>
                <span class="sector-tag">{c['sector']}</span>
                <h3 class="company-title">{c['name']}</h3>
                <div class="focus-text">{c['focus']}</div>
            </div>
            <div class="pricing-box">
                <div class="price-val">{c['price_setup']}</div>
                <div class="price-sub">+ {c['price_retainer']}</div>
            </div>
        </div>

        <div class="pitch-body">
            <div class="body-row">
                <span class="row-label">Целевой ЛПР:</span>
                <span class="row-val">{c['target_persona']}</span>
            </div>
            <div class="body-row">
                <span class="row-label">Критическая боль:</span>
                <span class="row-val text-pain">{c['pain_point']}</span>
            </div>
            <div class="body-row">
                <span class="row-label">Оффер "Троянского коня":</span>
                <span class="row-val text-trojan">{c['trojan_pitch']}</span>
            </div>
            <div class="body-row">
                <span class="row-label">Окупаемость (ROI):</span>
                <span class="row-val text-roi">{c['roi_desc']}</span>
            </div>
        </div>

        <div class="pitch-footer">
            <a href="{c['demo_link']}" target="_blank" class="btn-demo-link">🌐 Открыть Живое Демо</a>
            <div class="deck-actions">
                <a href="Dynamic_Pitch_Deck.html?id={c['id']}" target="_blank" class="btn-tool btn-deck">📊 Интерактивный Deck</a>
                <a href="Dynamic_One_Pager.html?id={c['id']}" target="_blank" class="btn-tool btn-pager">📄 КП-Одностраничник</a>
            </div>
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
            padding: 3px 8px;
            border-radius: 4px;
            font-size: 0.75rem;
            margin-right: 8px;
        }}
        .sector-tag {{
            background: rgba(197, 160, 89, 0.15);
            color: var(--gold-light);
            padding: 3px 8px;
            border-radius: 4px;
            font-size: 0.75rem;
            font-weight: 600;
        }}
        .company-title {{
            font-family: 'Playfair Display', serif;
            font-size: 1.6rem;
            color: #fff;
            margin-top: 8px;
            margin-bottom: 4px;
        }}
        .focus-text {{
            color: var(--text-dim);
            font-size: 0.9rem;
        }}
        .pricing-box {{
            text-align: right;
            background: rgba(16, 185, 129, 0.08);
            border: 1px solid rgba(16, 185, 129, 0.25);
            padding: 10px 18px;
            border-radius: 8px;
        }}
        .price-val {{
            font-family: 'Playfair Display', serif;
            font-size: 1.6rem;
            font-weight: 700;
            color: var(--green);
        }}
        .price-sub {{
            font-size: 0.8rem;
            color: var(--text-dim);
        }}
        
        .pitch-body {{
            display: flex;
            flex-direction: column;
            gap: 10px;
            margin-bottom: 22px;
        }}
        .body-row {{
            display: grid;
            grid-template-columns: 180px 1fr;
            gap: 16px;
            font-size: 0.95rem;
        }}
        @media (max-width: 768px) {{
            .body-row {{ grid-template-columns: 1fr; gap: 4px; }}
        }}
        .row-label {{
            color: var(--text-dim);
            font-weight: 600;
            font-size: 0.85rem;
        }}
        .row-val {{
            color: #E2E8F0;
        }}
        .text-pain {{
            color: #F87171;
        }}
        .text-trojan {{
            color: var(--gold-light);
            font-weight: 500;
        }}
        .text-roi {{
            color: #34D399;
            font-weight: 500;
        }}

        .pitch-footer {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            flex-wrap: wrap;
            gap: 12px;
            padding-top: 16px;
            border-top: 1px solid rgba(255, 255, 255, 0.04);
        }}
        .btn-demo-link {{
            color: #6EE7B7;
            text-decoration: none;
            font-size: 0.9rem;
            font-weight: 600;
            display: inline-flex;
            align-items: center;
            gap: 6px;
            transition: color 0.2s;
        }}
        .btn-demo-link:hover {{
            color: #fff;
        }}
        .deck-actions {{
            display: flex;
            gap: 8px;
        }}
        .btn-tool {{
            padding: 8px 16px;
            border-radius: 6px;
            font-size: 0.85rem;
            font-weight: 600;
            text-decoration: none;
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
    </style>
</head>
<body>

<div class="top-nav">
    <a href="index.html" class="btn-back">&larr; Вернуться в Центр Продаж</a>
    <div style="font-size: 0.85rem; color: var(--gold);">62 готовых коммерческих расчета</div>
</div>

<div class="container">
    <h1>🔍 Каталог 62 Коммерческих Предложений</h1>
    <p class="subtitle">Персонализированные пакеты внедрения, ценообразование, абонентская плата и экономическое обоснование (ROI)</p>

    <div class="pitches-list">
        {''.join(cards_pitches)}
    </div>
</div>

</body>
</html>
"""

with open(os.path.join(WORKSPACE, "Comprehensive_Pitches.html"), "w", encoding="utf-8") as f:
    f.write(comprehensive_html)
print("Comprehensive_Pitches.html успешно создан!")

# ==============================================================================
# 6. ГЕНЕРАЦИЯ Exclusive_Strategy.html (Двойной Бренд Глобал Плюс & GlobalTeamPartners)
# ==============================================================================
exclusive_md = """# 👑 Стратегия Двойного Бренда: «Глобал Плюс» &times; «GlobalTeamPartners»
### Как выигрывать тендеры и доверие уральских собственников за счет синергии двух сущностей

> **Суть стратегии:** Уральский бизнес с подозрением относится к «абстрактным московским или зарубежным IT-компаниям, которые берут предоплату и пропадают». В то же время местные микро-студии не вызывают уважения, потому что не умеют внедрять современный ИИ и сложные B2B-архитектуры. 
> 
> **Наше решение — идеальный дуализм:** 
> 1. **«Глобал Плюс»** — это свой, надежный, физически доступный региональный партнер (Дмитрий в Алапаевске и Синячихе, всегда готовый приехать на завод, пожать руку, подписать договор по безналу с НДС).
> 2. **«GlobalTeamPartners»** — это распределенный международный консорциум передовых инженеров, ИИ-разработчиков и дизайнеров, который обеспечивает технологическое превосходство уровня Москвы, Дубая и Торонто.

---

## 🏛️ Сравнительная Матрица Брендов

| Параметр | «Глобал Плюс» (Локальный Флагман) | «GlobalTeamPartners» (Технологический Движок) |
|---|---|---|
| **Юридическая роль** | Официальный контрагент в РФ, договор, акты, безнал, гарантии | Архитектурное бюро, ИИ-лаборатория, глобальный стек |
| **Роль Дмитрия** | Руководитель регионального развития, управляющий партнер | Член международного управляющего совета |
| **Ключевой месседж** | «Мы рядом, мы отвечаем лицом и репутацией на Урале» | «Вы получаете технологии уровня топ-10 мировых лидеров» |
| **Кому презентовать** | Директорам заводов, консервативным собственникам, главврачам | Молодым прогрессивным девелоперам, маркетинговым директорам |

---

## 🎭 Сценарий Использования на Переговорах

### Фаза 1: Вход через надежность «Глобал Плюс»
Когда директор завода спрашивает: *«А вы кто такие и откуда?»*
* **Ответ Дмитрия:** *«Я представляю 'Глобал Плюс'. Наш офис и производство здесь, на Урале. Я лично нахожусь в Алапаевском районе и курирую каждый проект. Мы работаем по официальному российскому договору, с поэтапной оплатой и гарантийным обслуживанием»*.
* **Эффект:** Снята тревога о «мошенниках из интернета».

### Фаза 2: Вау-эффект через масштаб «GlobalTeamPartners»
Когда директор спрашивает: *«А вы точно справитесь с нагрузкой и подключением нейросетей к нашей 1С?»*
* **Ответ Дмитрия:** *«Безусловно. Наша технологическая база работает в партнерстве с международным консорциумом Global Team Partners. Наши инженеры создавали цифровые экосистемы в Сербии, ОАЭ и Канаде. Ваш проект разрабатывается на том же стеке, что и передовые мировые платформы. Вот примеры наших зарубежных и федеральных кейсов»*.
* **Эффект:** Предприятие понимает, что получает космический уровень качества по адекватной уральской цене.

---

## 💰 Модель Монетизации и Долгосрочный Доход Партнера
1. **Этап Setup (Внедрение за 48 часов – 2 недели):**
   * Разовый чек: от 120 000 до 1 200 000 рублей.
   * Покрывает быстрый запуск прототипа, интеграцию базы данных и обучение персонала.
2. **Этап Retainer (Ежемесячная подписка):**
   * Ежемесячный чек: от 25 000 до 210 000 рублей/месяц.
   * Включает: хостинг, поддержку ИИ-ботов, обновление номенклатуры, докрутку рекламных воронок, отчетность собственнику.
3. **Финансовая цель Дмитрия:**
   * 15 активных предприятий на абонентке &times; средний чек 60 000 ₽ = **900 000 ₽ ежемесячной стабильной выручки** без необходимости постоянного холодного поиска!
"""

exclusive_html = f"""<!DOCTYPE html>
<html lang="ru">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Стратегия Двойного Бренда | Глобал Плюс & GlobalTeamPartners</title>
<script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,600;0,700;1,400&family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
<style>
  body {{ font-family: 'Inter', sans-serif; background: #0B0E14; color: #F8FAFC; padding: 40px 20px; max-width: 860px; margin: 0 auto; line-height: 1.7; }}
  h1, h2, h3 {{ color: #C5A059; font-family: 'Playfair Display', serif; margin-top: 1.5em; margin-bottom: 0.5em; }}
  h1 {{ font-size: 2.3rem; line-height: 1.2; margin-top: 0; }}
  a {{ color: #C5A059; text-decoration: none; font-weight: bold; }}
  .btn-back {{ display: inline-flex; align-items: center; gap: 8px; margin-bottom: 30px; padding: 10px 20px; background: #C5A059; color: #000; text-decoration: none; border-radius: 6px; font-weight: bold; font-size: 0.9rem; transition: 0.2s; }}
  .btn-back:hover {{ background: #E0C07A; }}
  hr {{ border: 0; height: 1px; background: rgba(197,160,89,0.25); margin: 35px 0; }}
  li {{ margin-bottom: 12px; color: #CBD5E1; }}
  blockquote {{ background: rgba(197, 160, 89, 0.08); padding: 18px 24px; border-left: 4px solid #C5A059; margin: 25px 0; border-radius: 0 8px 8px 0; font-size: 1.05rem; }}
  strong {{ color: #fff; }}
  table {{ width: 100%; border-collapse: collapse; margin: 25px 0; background: #121721; border-radius: 8px; overflow: hidden; }}
  th, td {{ padding: 12px 16px; border: 1px solid rgba(255,255,255,0.08); text-align: left; font-size: 0.9rem; }}
  th {{ background: #18202E; color: #C5A059; font-weight: 600; }}
</style>
</head>
<body>
<a href="index.html" class="btn-back">&larr; Вернуться в Центр Продаж</a>
<div id="content"></div>
<script>
  const markdownText = `{exclusive_md}`;
  document.getElementById('content').innerHTML = marked.parse(markdownText);
</script>
</body>
</html>
"""

with open(os.path.join(WORKSPACE, "Exclusive_Strategy.html"), "w", encoding="utf-8") as f:
    f.write(exclusive_html)
print("Exclusive_Strategy.html успешно создан!")

# ==============================================================================
# 7. ГЕНЕРАЦИЯ Market_Intelligence.html (Анализ рынков Урала)
# ==============================================================================
market_md = """# 🧠 Разведка Рынка Урала: Синячиха, Алапаевск, Екатеринбург
### Экономический ландшафт, специфика менталитета ЛПР и точки входа

---

## 📍 Пояс 1: Верхняя Синячиха (Моногород Лесопереработки)
* **Экономический профиль:** Исторический центр глубокой деревообработки Свердловской области. Ключевой гигант — НАО «СВЕЗА Верхняя Синячиха» (мировые поставки березовой фанеры), крупное предприятие «Лестех», лесохимический сектор, лесозаготовительные артели.
* **Специфика:** Моногород с выраженной рабочей специализацией. Главная боль директоров — **острейший дефицит рабочих кадров и специалистов ЧПУ**, а также необходимость ускорения B2B-отгрузок оптовым дилерам.
* **Точки входа:**
  1. HR-автоматизация найма и онбординга рабочих через Telegram-ботов для комбинатов.
  2. B2B-калькуляторы кубатуры фанеры и пиломатериалов для оптовиков.
  3. Социальные и сервисные сервисы (ФОК «Орион», Нижнесинячихинский музей зодчества — один из главных туристических объектов Урала).

---

## 📍 Пояс 2: Город Алапаевск и Район (Индустриально-Машиностроительный Узел)
* **Экономический профиль:** Исторический центр горнозаводского Урала. Лидер в масштабах всей РФ — завод «Стройдормаш» (бурильно-крановые машины для энергетики и мостостроения), завод «ЗИСТ» (буровой инструмент), «Бурмаш», «АДОЗ» (деревянная тара спецназначения), «Алапаевские сплавы и металлы» (медь, бронза, латунь), Молочный комбинат (АМК), Котельный завод.
* **Туристический потенциал:** Всемирно известная **Алапаевская узкоколейная железная дорога (АУЖД)** — самая протяженная пассажирская узкоколейка планеты, притягивающая туристов со всего мира.
* **Специфика переговоров:** Руководители заводов — производственники старой закалки или прагматичные коммерсанты. Не терпят пустословия. Любят цифры: сколько часов сэкономим, сколько новых заявок получим, как исключим ошибки в 1С.

---

## 📍 Пояс 3: Екатеринбург (Миллионник & Столица Урала)
* **Экономический профиль:** 4-й по величине город России, колоссальная концентрация капитала, высококонкурентные рынки девелопмента, платной медицины, премиальной HoReCa и логистики.
* **Ключевые секторы с высокими чеками:**
  * **Девелопмент:** «Брусника», «Атомстройкомплекс», «УГМК-Застройщик», «Forum Group», «PRINZIP». Бьются за каждого покупателя квартир бизнес-класса. Им нужны 3D-планировки, AI-ипотечные боты и кинематографичные презентации.
  * **Премиум HoReCa:** Отели «Hyatt Regency», «Высоцкий», рестораны «Троекуров», «Kitchen», «Сойка», «Гастроли». Готовы платить за статус, ликвидацию no-show и автоматизацию банкетных депозитов.
  * **Частная медицина:** «УГМК-Здоровье», Клиника Нудельмана, «Здоровье 365», «Линлайн». Тратят миллионы на маркетинг, страдают от перегрузки колл-центров. Нуждаются в AI-триаже и удобной онлайн-записи.
  * **Тяжелое машиностроение:** «Уралмашзавод», «УЗГА», «Синара», «Пневмостроймашина». Нуждаются в цифровых каталогах импортозамещения и привлечении лучших технических кадров.
"""

market_html = f"""<!DOCTYPE html>
<html lang="ru">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Разведка Рынка Урала | Глобал Плюс</title>
<script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,600;0,700;1,400&family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
<style>
  body {{ font-family: 'Inter', sans-serif; background: #0B0E14; color: #F8FAFC; padding: 40px 20px; max-width: 860px; margin: 0 auto; line-height: 1.7; }}
  h1, h2, h3 {{ color: #C5A059; font-family: 'Playfair Display', serif; margin-top: 1.5em; margin-bottom: 0.5em; }}
  h1 {{ font-size: 2.3rem; line-height: 1.2; margin-top: 0; }}
  a {{ color: #2563EB; text-decoration: none; font-weight: bold; }}
  .btn-back {{ display: inline-flex; align-items: center; gap: 8px; margin-bottom: 30px; padding: 10px 20px; background: #2563EB; color: #fff; text-decoration: none; border-radius: 6px; font-weight: bold; font-size: 0.9rem; transition: 0.2s; }}
  .btn-back:hover {{ background: #1D4ED8; }}
  hr {{ border: 0; height: 1px; background: rgba(197,160,89,0.25); margin: 35px 0; }}
  li {{ margin-bottom: 12px; color: #CBD5E1; }}
  strong {{ color: #fff; }}
</style>
</head>
<body>
<a href="index.html" class="btn-back">&larr; Вернуться в Центр Продаж</a>
<div id="content"></div>
<script>
  const markdownText = `{market_md}`;
  document.getElementById('content').innerHTML = marked.parse(markdownText);
</script>
</body>
</html>
"""

with open(os.path.join(WORKSPACE, "Market_Intelligence.html"), "w", encoding="utf-8") as f:
    f.write(market_html)
print("Market_Intelligence.html успешно создан!")

# ==============================================================================
# 8. ГЕНЕРАЦИЯ Dynamic_Pitch_Deck.html (Интерактивная презентация для любой компании)
# ==============================================================================
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

    .btn-demo {{
        margin-top: 30px;
        padding: 16px 45px;
        background: #C5A059;
        color: #000;
        text-decoration: none;
        font-size: clamp(0.9rem, 1.4vw, 1.2rem);
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
    <p class="body-text">Персональная программа цифровой трансформации сбыта и внедрения ИИ-инфраструктуры.</p>
    <p style="font-size: 0.9rem; color: #64748B; margin-top: 30px;">(Листайте стрелками, свайпом или клавишей Пробел &darr;)</p>
</div>

<!-- СЛАЙД 1: ДИАГНОСТИКА И БОЛЬ -->
<div class="slide" id="slide1">
    <div class="pill-tag" style="background: rgba(211,47,47,0.15); border-color:#D32F2F; color:#FF8A80;">ТЕКУЩИЕ УЗКИЕ МЕСТА</div>
    <h1 style="color:#F87171;">Точки Потери Прибыли</h1>
    <div class="card-pain" id="d-pain">
        Выявленная боль бизнес-процессов...
    </div>
    <p class="body-text">Традиционные методы работы с клиентами и ручные расчеты создают задержки и снижают маржинальность в борьбе с конкурентами.</p>
</div>

<!-- СЛАЙД 2: РЕШЕНИЕ И ДЕМО -->
<div class="slide" id="slide2">
    <div class="pill-tag">ИНЖЕНЕРНОЕ РЕШЕНИЕ</div>
    <h1>Быстрый Старт за 48 Часов</h1>
    <div class="card-sol" id="d-trojan">
        Оффер Троянского коня...
    </div>
    <a href="#" id="d-demo" class="btn-demo" target="_blank">ОТКРЫТЬ ЖИВОЙ ПРОТОТИП 🌐</a>
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
    const db = {json.dumps(COMPANIES, ensure_ascii=False)};
    const urlParams = new URLSearchParams(window.location.search);
    const targetId = urlParams.get('id');

    let currentCompany = db.find(c => c.id === targetId) || db[0];

    document.getElementById('d-name').innerText = currentCompany.name;
    document.getElementById('d-focus').innerText = currentCompany.focus + " (" + currentCompany.region + ")";
    document.getElementById('d-pain').innerText = currentCompany.pain_point;
    document.getElementById('d-trojan').innerText = currentCompany.trojan_pitch;
    document.getElementById('d-demo').href = currentCompany.demo_link;
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
print("Dynamic_Pitch_Deck.html успешно создан!")

# ==============================================================================
# 9. ГЕНЕРАЦИЯ Dynamic_One_Pager.html (КП-Одностраничник)
# ==============================================================================
pager_html = f"""<!DOCTYPE html>
<html lang="ru">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Коммерческое Предложение | Глобал Плюс</title>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,600;0,700;1,400&family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
<style>
    body {{
        font-family: 'Inter', sans-serif;
        background: #0B0E14;
        color: #1E293B;
        padding: 40px 20px;
        margin: 0;
    }}
    .sheet {{
        background: #FFFFFF;
        max-width: 820px;
        margin: 0 auto;
        padding: 50px 60px;
        border-radius: 12px;
        box-shadow: 0 20px 45px rgba(0,0,0,0.4);
        position: relative;
    }}
    .header-bar {{
        display: flex;
        justify-content: space-between;
        align-items: flex-start;
        border-bottom: 2px solid #E2E8F0;
        padding-bottom: 25px;
        margin-bottom: 30px;
    }}
    .logo-text {{
        font-family: 'Playfair Display', serif;
        font-size: 22px;
        font-weight: 700;
        color: #0F172A;
    }}
    .logo-text span {{
        color: #C5A059;
    }}
    .badge-conf {{
        background: #FEF2F2;
        border: 1px solid #FCA5A5;
        color: #B91C1C;
        font-size: 11px;
        padding: 4px 10px;
        border-radius: 4px;
        font-weight: 700;
        letter-spacing: 1px;
    }}
    .title-box {{
        margin-bottom: 25px;
    }}
    .target-company {{
        font-family: 'Playfair Display', serif;
        font-size: 32px;
        font-weight: 700;
        color: #0F172A;
        line-height: 1.2;
        margin-bottom: 6px;
    }}
    .target-sub {{
        font-size: 14px;
        color: #64748B;
        font-weight: 500;
    }}
    .section-title {{
        font-size: 12px;
        text-transform: uppercase;
        letter-spacing: 2px;
        color: #94A3B8;
        font-weight: 700;
        margin-bottom: 8px;
    }}
    .card-block {{
        background: #F8FAFC;
        border: 1px solid #E2E8F0;
        border-radius: 8px;
        padding: 18px 22px;
        margin-bottom: 20px;
    }}
    .card-block.pain {{
        border-left: 4px solid #EF4444;
    }}
    .card-block.sol {{
        border-left: 4px solid #10B981;
    }}
    .block-text {{
        font-size: 15px;
        line-height: 1.6;
        color: #334155;
    }}
    .pricing-table {{
        width: 100%;
        border-collapse: collapse;
        margin: 25px 0;
    }}
    .pricing-table th {{
        background: #F1F5F9;
        text-align: left;
        padding: 12px 16px;
        font-size: 13px;
        color: #475569;
        border-bottom: 1px solid #CBD5E1;
    }}
    .pricing-table td {{
        padding: 14px 16px;
        border-bottom: 1px solid #E2E8F0;
        font-size: 14px;
    }}
    .price-num {{
        font-weight: 700;
        color: #0F172A;
        font-size: 16px;
    }}
    .footer-sign {{
        margin-top: 40px;
        padding-top: 25px;
        border-top: 1px solid #E2E8F0;
        display: flex;
        justify-content: space-between;
        align-items: center;
        font-size: 13px;
        color: #64748B;
    }}
    .btn-print {{
        position: fixed;
        bottom: 30px;
        right: 30px;
        background: #C5A059;
        color: #000;
        padding: 12px 24px;
        border-radius: 30px;
        font-weight: 700;
        text-decoration: none;
        box-shadow: 0 10px 25px rgba(0,0,0,0.3);
        cursor: pointer;
        border: none;
    }}
    @media print {{
        body {{ background: #fff; padding: 0; }}
        .sheet {{ box-shadow: none; padding: 20px; }}
        .btn-print {{ display: none; }}
    }}
</style>
</head>
<body>

<button class="btn-print" onclick="window.print()">🖨️ Распечатать / В PDF</button>

<div class="sheet">
    <div class="header-bar">
        <div>
            <div class="logo-text">ГЛОБАЛ ПЛЮС <span>&times;</span> GLOBAL TEAM PARTNERS</div>
            <div style="font-size: 12px; color: #64748B; margin-top: 4px;">Уральский Департамент Автоматизации &bull; Свердловская область</div>
        </div>
        <div class="badge-conf">КОНФИДЕНЦИАЛЬНО</div>
    </div>

    <div class="title-box">
        <div class="target-company" id="d-name">Компания</div>
        <div class="target-sub" id="d-sub">Отрасль &bull; Локация</div>
    </div>

    <div class="section-title">1. Анализ Текущей Ситуации &amp; Узкие Места</div>
    <div class="card-block pain">
        <div class="block-text" id="d-pain">Описание боли...</div>
    </div>

    <div class="section-title">2. Предлагаемое Решение (Быстрый Старт)</div>
    <div class="card-block sol">
        <div class="block-text" id="d-sol">Описание решения...</div>
    </div>

    <div class="section-title">3. Стоимость Внедрения &amp; Сопровождения</div>
    <table class="pricing-table">
        <thead>
            <tr>
                <th>Этап</th>
                <th>Срок запуска</th>
                <th>Состав работ</th>
                <th>Стоимость</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td><strong>Фаза 1: Прототип</strong></td>
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
    const db = {json.dumps(COMPANIES, ensure_ascii=False)};
    const urlParams = new URLSearchParams(window.location.search);
    const targetId = urlParams.get('id');

    let c = db.find(item => item.id === targetId) || db[0];

    document.getElementById('d-name').innerText = c.name;
    document.getElementById('d-sub').innerText = c.sector + " | " + c.region + " | ЛПР: " + c.target_persona;
    document.getElementById('d-pain').innerText = c.pain_point;
    document.getElementById('d-sol').innerText = c.trojan_pitch;
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
print("Dynamic_One_Pager.html успешно создан!")

print("\nВсе основные страницы сгенерированы успешно!")
