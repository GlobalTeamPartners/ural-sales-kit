# -*- coding: utf-8 -*-
"""
Генератор интерактивных демо-порталов для демонстрации на встречах с клиентами
demos/wood-industry-demo/index.html
demos/machinery-demo/index.html
demos/real-estate-demo/index.html
demos/horeca-demo/index.html
demos/medical-demo/index.html
demos/service-demo/index.html
"""
import os
import sys

if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

WORKSPACE = r"c:\Users\Vlaslav\Downloads\Дима Верхняя Синичиха Алапаевск"
DEMOS_DIR = os.path.join(WORKSPACE, "demos")

os.makedirs(os.path.join(DEMOS_DIR, "wood-industry-demo"), exist_ok=True)
os.makedirs(os.path.join(DEMOS_DIR, "machinery-demo"), exist_ok=True)
os.makedirs(os.path.join(DEMOS_DIR, "real-estate-demo"), exist_ok=True)
os.makedirs(os.path.join(DEMOS_DIR, "horeca-demo"), exist_ok=True)
os.makedirs(os.path.join(DEMOS_DIR, "medical-demo"), exist_ok=True)
os.makedirs(os.path.join(DEMOS_DIR, "service-demo"), exist_ok=True)

# ------------------------------------------------------------------------------
# 1. ДЕМО 1: ЛЕСОПРОМЫШЛЕННЫЙ B2B-ПОРТАЛ (СВЕЗА, Лестех, АДОЗ, АЛХ)
# ------------------------------------------------------------------------------
wood_demo_html = """<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>УралЛесПром | Цифровой B2B-Портал Оптовых Поставок Древесины и Фанеры</title>
    <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700;800&family=Playfair+Display:wght@700&display=swap" rel="stylesheet">
    <style>
        :root {
            --primary: #15803D;
            --primary-dark: #166534;
            --accent: #EAB308;
            --dark: #0F172A;
            --surface: #1E293B;
            --light: #F8FAFC;
            --gray: #94A3B8;
        }
        * { margin: 0; padding: 0; box-sizing: border-box; font-family: 'Montserrat', sans-serif; }
        body { background: var(--dark); color: var(--light); line-height: 1.6; }
        .topbar { background: #022c22; border-bottom: 1px solid rgba(255,255,255,0.1); padding: 10px 24px; font-size: 13px; display: flex; justify-content: space-between; align-items: center; }
        .hero { padding: 80px 24px; background: linear-gradient(180deg, #064e3b 0%, var(--dark) 100%); text-align: center; }
        .hero h1 { font-family: 'Playfair Display', serif; font-size: clamp(2rem, 4vw, 3.2rem); margin-bottom: 16px; }
        .hero p { max-width: 750px; margin: 0 auto 30px; color: #cbd5e1; font-size: 1.1rem; }
        .container { max-width: 1180px; margin: 0 auto; padding: 40px 20px; }
        .calc-card { background: var(--surface); border-radius: 16px; padding: 36px; border: 1px solid rgba(255,255,255,0.1); margin-bottom: 40px; box-shadow: 0 20px 40px rgba(0,0,0,0.4); }
        .calc-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 24px; margin-top: 20px; }
        .input-group label { display: block; font-size: 13px; font-weight: 600; margin-bottom: 8px; color: #cbd5e1; }
        .input-group select, .input-group input { width: 100%; background: #0f172a; border: 1px solid rgba(255,255,255,0.15); color: #fff; padding: 12px 16px; border-radius: 8px; font-size: 15px; outline: none; }
        .result-box { background: rgba(22, 101, 52, 0.3); border: 2px solid var(--primary); border-radius: 12px; padding: 24px; margin-top: 25px; display: flex; justify-content: space-between; align-items: center; flex-wrap: gap; gap: 20px; }
        .price-total { font-size: 2rem; font-weight: 800; color: #4ade80; }
        .btn-order { background: var(--primary); color: #fff; border: none; padding: 14px 32px; border-radius: 8px; font-weight: 700; font-size: 15px; cursor: pointer; transition: 0.2s; }
        .btn-order:hover { background: #22c55e; }
        .features-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 24px; }
        .feat-card { background: #182234; padding: 24px; border-radius: 12px; border: 1px solid rgba(255,255,255,0.06); }
        .feat-icon { font-size: 28px; margin-bottom: 12px; }
        .badge-demo { background: #eab308; color: #000; padding: 4px 10px; border-radius: 20px; font-weight: 800; font-size: 11px; }
    </style>
</head>
<body>

<div class="topbar">
    <div>🌲 <strong>Свердловский Лесопромышленный Комплекс</strong> &bull; Верхняя Синячиха &bull; Алапаевск</div>
    <div><span class="badge-demo">ДЕМО ДЛЯ КЛИЕНТА ГЛОБАЛ ПЛЮС</span> &bull; 8 (800) 500-24-26</div>
</div>

<div class="hero">
    <h1>Оптовые Поставки Фанеры и Пиломатериалов</h1>
    <p>Автоматизированная B2B-система: моментальный расчет вагонных и фурных партий по ГОСТу с проверкой остатков на складах Верхней Синячихи.</p>
</div>

<div class="container">
    <div class="calc-card">
        <h2 style="font-size: 1.5rem; margin-bottom: 8px;">📊 Интерактивный Калькулятор Партии (ГОСТ 3916.1-96)</h2>
        <p style="color: var(--gray); font-size: 14px;">Рассчитайте кубатуру, вес и точную оптовую стоимость отгрузки за 10 секунд:</p>

        <div class="calc-grid">
            <div class="input-group">
                <label>Тип продукции:</label>
                <select id="prodType" onchange="calc()">
                    <option value="65000">Фанера березовая ФСФ 1525×1525 (сорт 2/4)</option>
                    <option value="82000">Фанера ламинированная 1220×2440 (сетка/гладкая)</option>
                    <option value="28000">Пиломатериал хвойный обрезной ГОСТ 8486-86</option>
                    <option value="36000">Евровагонка сорт А (хвоя/осина)</option>
                    <option value="12000">Пеллеты топливные древесные (биг-бэг 1 т)</option>
                </select>
            </div>
            <div class="input-group">
                <label>Толщина / Калибр:</label>
                <select id="thickness" onchange="calc()">
                    <option value="1">18 мм (стандарт опалубки)</option>
                    <option value="1.2">21 мм (усиленная)</option>
                    <option value="0.8">12 мм (конструкционная)</option>
                    <option value="0.6">9 мм (обшивочная)</option>
                </select>
            </div>
            <div class="input-group">
                <label>Объем партии (м³ / тонн):</label>
                <input type="number" id="volume" value="35" min="1" max="1000" oninput="calc()">
            </div>
            <div class="input-group">
                <label>Способ доставки:</label>
                <select id="delivery">
                    <option value="auto">Автофура 20 тонн (до объекта)</option>
                    <option value="rail">Крытый вагон 68 тонн (РЖД)</option>
                    <option value="pickup">Самовывоз (склад Верхняя Синячиха)</option>
                </select>
            </div>
        </div>

        <div class="result-box">
            <div>
                <div style="font-size: 14px; color: #cbd5e1;">Итоговая оптовая стоимость партии с НДС:</div>
                <div class="price-total" id="totalPrice">2 275 000 ₽</div>
                <div style="font-size: 12px; color: var(--gray);" id="weightText">Ориентировочный вес: 24.5 т &bull; Готовность к отгрузке: 48 ч</div>
            </div>
            <button class="btn-order" onclick="alert('Заявка сформирована! В боевой версии спецификация мгновенно уходит в 1С и WhatsApp коммерческого директора.')">📄 Сформировать Спецификацию и Счет</button>
        </div>
    </div>

    <div class="features-grid">
        <div class="feat-card">
            <div class="feat-icon">⚡</div>
            <h3>Мгновенная выгрузка счета</h3>
            <p style="color: var(--gray); font-size: 14px; margin-top: 8px;">Снабженцы строительных холдингов получают готовый счет с печатью за 1 минуту вместо суточного ожидания ответа менеджера.</p>
        </div>
        <div class="feat-card">
            <div class="feat-icon">🚂</div>
            <h3>Прямой трекинг РЖД</h3>
            <p style="color: var(--gray); font-size: 14px; margin-top: 8px;">Автоматическая интеграция с накладными РЖД по станции Синячиха / Алапаевск с SMS-оповещением клиента в пути.</p>
        </div>
        <div class="feat-card">
            <div class="feat-icon">🤖</div>
            <h3>ИИ-ассистент по ГОСТам</h3>
            <p style="color: var(--gray); font-size: 14px; margin-top: 8px;">Нейросеть отвечает на любые технические вопросы клиентов по влажности, плотности и сертификатам в Telegram 24/7.</p>
        </div>
    </div>
</div>

<script>
    function calc() {
        const base = parseFloat(document.getElementById('prodType').value);
        const thick = parseFloat(document.getElementById('thickness').value);
        const vol = parseFloat(document.getElementById('volume').value) || 0;
        const total = Math.round(base * thick * vol);
        document.getElementById('totalPrice').innerText = total.toLocaleString('ru-RU') + " ₽";
        document.getElementById('weightText').innerText = "Ориентировочный вес: " + (vol * 0.7).toFixed(1) + " т • Готовность к отгрузке: 48 ч";
    }
    calc();
</script>

</body>
</html>
"""

with open(os.path.join(DEMOS_DIR, "wood-industry-demo", "index.html"), "w", encoding="utf-8") as f:
    f.write(wood_demo_html)
print("demos/wood-industry-demo/index.html создан!")

# ------------------------------------------------------------------------------
# 2. ДЕМО 2: МАШИНОСТРОЕНИЕ & СПЕЦТЕХНИКА (Стройдормаш, ЗИСТ, PSM-Hydraulics)
# ------------------------------------------------------------------------------
machinery_demo_html = """<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>УралМашПром | Цифровой B2B Селектор Бурильной Техники и Гидравлики</title>
    <link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;700&family=Inter:wght@400;600&display=swap" rel="stylesheet">
    <style>
        :root {
            --accent: #F59E0B;
            --dark: #0B0F19;
            --surface: #111827;
            --card: #1F2937;
            --text: #F3F4F6;
            --gray: #9CA3AF;
        }
        * { margin:0; padding:0; box-sizing:border-box; font-family: 'Inter', sans-serif; }
        body { background: var(--dark); color: var(--text); }
        .header { background: #000; border-bottom: 2px solid var(--accent); padding: 18px 30px; display: flex; justify-content: space-between; align-items: center; }
        .logo { font-family: 'Space Grotesk', sans-serif; font-size: 20px; font-weight: 700; color: #fff; }
        .logo span { color: var(--accent); }
        .container { max-width: 1200px; margin: 40px auto; padding: 0 20px; }
        .hero { text-align: center; margin-bottom: 50px; }
        .hero h1 { font-family: 'Space Grotesk', sans-serif; font-size: clamp(2rem, 3.5vw, 3rem); color: #fff; margin-bottom: 12px; }
        .hero p { color: var(--gray); font-size: 1.1rem; max-width: 750px; margin: 0 auto; }
        .tabs { display: flex; gap: 12px; margin-bottom: 30px; border-bottom: 1px solid var(--card); padding-bottom: 12px; }
        .tab { background: transparent; border: 1px solid var(--card); color: var(--gray); padding: 10px 24px; border-radius: 8px; cursor: pointer; font-weight: 600; }
        .tab.active { background: var(--accent); color: #000; border-color: var(--accent); }
        .grid-machinery { display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 24px; }
        .machine-card { background: var(--surface); border: 1px solid var(--card); border-radius: 12px; overflow: hidden; transition: transform 0.2s; }
        .machine-card:hover { transform: translateY(-5px); border-color: var(--accent); }
        .card-img-placeholder { height: 180px; background: linear-gradient(135deg, #1f2937, #111827); display: flex; align-items: center; justify-content: center; font-size: 50px; border-bottom: 1px solid var(--card); }
        .card-body { padding: 24px; }
        .card-title { font-family: 'Space Grotesk', sans-serif; font-size: 1.3rem; margin-bottom: 8px; color: #fff; }
        .spec-list { list-style: none; margin: 16px 0; font-size: 14px; color: var(--gray); }
        .spec-list li { margin-bottom: 6px; display: flex; justify-content: space-between; border-bottom: 1px solid rgba(255,255,255,0.05); padding-bottom: 4px; }
        .spec-list li strong { color: #fff; }
        .btn-inquire { width: 100%; background: var(--accent); color: #000; border: none; padding: 12px; border-radius: 6px; font-weight: 700; cursor: pointer; }
        .btn-inquire:hover { background: #d97706; }
    </style>
</head>
<body>

<div class="header">
    <div class="logo">УРАЛ<span>МАШ</span>ТЕХ &bull; Алапаевск &bull; Екатеринбург</div>
    <div style="font-size: 13px; color: var(--accent);">⚡ ПРОТОТИП ГЛОБАЛ ПЛЮС | B2B СИСТЕМА ДЛЯ ЗАВОДОВ</div>
</div>

<div class="container">
    <div class="hero">
        <h1>Интеллектуальный Каталог Бурильной Техники &amp; Инструмента</h1>
        <p>Подбор бурильно-крановых машин (БКМ), шнеков и аксиально-поршневой гидравлики под категории грунтов I–VI с расчетом окупаемости.</p>
    </div>

    <div class="tabs">
        <button class="tab active">Бурильно-крановые машины (БКМ)</button>
        <button class="tab">Буровой инструмент &amp; Шнеки (ЗИСТ)</button>
        <button class="tab">Гидромоторы &amp; Насосы (PSM)</button>
    </div>

    <div class="grid-machinery">
        <div class="machine-card">
            <div class="card-img-placeholder">🏗️</div>
            <div class="card-body">
                <div class="card-title">БКМ-317-01 (Шасси ГАЗ-Садко)</div>
                <p style="font-size: 13px; color: var(--gray);">Бурение скважин в немерзлых и мерзлых грунтах, установка опор ЛЭП 0.4–10 кВ.</p>
                <ul class="spec-list">
                    <li>Глубина бурения: <strong>до 3.0 м</strong></li>
                    <li>Диаметр бурения: <strong>0.36 – 0.80 м</strong></li>
                    <li>Грузоподъемность крана: <strong>1.25 т</strong></li>
                    <li>Угол бурения: <strong>62° – 95°</strong></li>
                </ul>
                <button class="btn-inquire" onclick="alert('Технико-коммерческое предложение сформировано!')">Сформировать ТКП (PDF)</button>
            </div>
        </div>

        <div class="machine-card">
            <div class="card-img-placeholder">🚜</div>
            <div class="card-body">
                <div class="card-title">БКМ-515 (Шасси УРАЛ 4320)</div>
                <p style="font-size: 13px; color: var(--gray);">Тяжелая техника повышенной проходимости для энергетики и мостостроения в Сибири и ХМАО.</p>
                <ul class="spec-list">
                    <li>Глубина бурения: <strong>до 5.0 м</strong></li>
                    <li>Диаметр бурения: <strong>0.36 – 1.0 м</strong></li>
                    <li>Грузоподъемность крана: <strong>2.0 т</strong></li>
                    <li>Тип привода: <strong>Гидравлический</strong></li>
                </ul>
                <button class="btn-inquire" onclick="alert('Технико-коммерческое предложение сформировано!')">Сформировать ТКП (PDF)</button>
            </div>
        </div>

        <div class="machine-card">
            <div class="card-img-placeholder">🔩</div>
            <div class="card-body">
                <div class="card-title">Шнеки скальные &amp; Резцы РБМ-35</div>
                <p style="font-size: 13px; color: var(--gray);">Износостойкий инструмент для бурения скальных и вечномерзлых грунтов IV–VI категории.</p>
                <ul class="spec-list">
                    <li>Сталь шнека: <strong>09Г2С (упрочненная)</strong></li>
                    <li>Тип замка: <strong>Шестигранник 55/70 мм</strong></li>
                    <li>Ресурс резцов: <strong>+40% к стандарту</strong></li>
                    <li>Склад: <strong>В наличии (Алапаевск)</strong></li>
                </ul>
                <button class="btn-inquire" onclick="alert('Счет на инструмент забронирован на 3 дня!')">Забронировать со склада</button>
            </div>
        </div>
    </div>
</div>

</body>
</html>
"""

with open(os.path.join(DEMOS_DIR, "machinery-demo", "index.html"), "w", encoding="utf-8") as f:
    f.write(machinery_demo_html)
print("demos/machinery-demo/index.html создан!")

# ------------------------------------------------------------------------------
# 3. ДЕМО 3: ДЕВЕЛОПМЕНТ & ПРЕМИУМ ЖК (Брусника, УГМК-Застройщик, Атом)
# ------------------------------------------------------------------------------
re_demo_html = """<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ЖК «Екатерининская Резиденция» | Премиальный Девелопмент Екатеринбурга</title>
    <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@600;700&family=Montserrat:wght@300;400;500;600&display=swap" rel="stylesheet">
    <style>
        :root {
            --gold: #D4AF37;
            --dark: #0A0C10;
            --surface: #121620;
            --text: #F8FAFC;
        }
        * { margin:0; padding:0; box-sizing:border-box; font-family: 'Montserrat', sans-serif; }
        body { background: var(--dark); color: var(--text); }
        .hero { height: 85vh; background: linear-gradient(180deg, rgba(10,12,16,0.4) 0%, var(--dark) 100%), radial-gradient(circle at center, #1e293b 0%, #0a0c10 100%); display: flex; flex-direction: column; justify-content: center; align-items: center; text-align: center; padding: 20px; position: relative; }
        .hero h1 { font-family: 'Cinzel', serif; font-size: clamp(2.2rem, 5vw, 4.5rem); letter-spacing: 2px; color: #fff; margin-bottom: 12px; }
        .hero h1 span { color: var(--gold); }
        .hero p { font-size: 1.2rem; color: #94a3b8; max-width: 700px; margin-bottom: 30px; letter-spacing: 1px; }
        .container { max-width: 1100px; margin: -50px auto 60px; padding: 0 20px; position: relative; z-index: 10; }
        .filter-panel { background: var(--surface); border: 1px solid rgba(212,175,55,0.3); border-radius: 16px; padding: 30px; box-shadow: 0 25px 50px rgba(0,0,0,0.6); }
        .filter-row { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 20px; margin-bottom: 25px; }
        .filter-group label { display: block; font-size: 11px; text-transform: uppercase; letter-spacing: 2px; color: var(--gold); margin-bottom: 8px; font-weight: 600; }
        .filter-group select { width: 100%; background: #0a0c10; border: 1px solid rgba(255,255,255,0.15); color: #fff; padding: 12px 14px; border-radius: 6px; outline: none; }
        .flats-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 24px; margin-top: 30px; }
        .flat-card { background: #161b26; border-radius: 12px; border: 1px solid rgba(255,255,255,0.08); padding: 24px; transition: 0.3s; }
        .flat-card:hover { border-color: var(--gold); transform: translateY(-4px); }
        .flat-type { font-family: 'Cinzel', serif; font-size: 1.3rem; color: #fff; margin-bottom: 4px; }
        .flat-price { font-size: 1.4rem; color: var(--gold); font-weight: 700; margin: 12px 0; }
        .btn-view { display: block; text-align: center; background: transparent; border: 1px solid var(--gold); color: var(--gold); padding: 10px; border-radius: 6px; text-decoration: none; font-weight: 600; font-size: 13px; transition: 0.2s; }
        .btn-view:hover { background: var(--gold); color: #000; }
    </style>
</head>
<body>

<div class="hero">
    <div style="font-size: 11px; letter-spacing: 5px; color: var(--gold); margin-bottom: 15px;">ЕКАТЕРИНБУРГ &bull; НАБЕРЕЖНАЯ ИСЕТИ</div>
    <h1>Екатерининская <span>Резиденция</span></h1>
    <p>Клубный дом приватного класса с панорамными террасами и сервисом 5-звездочного отеля.</p>
</div>

<div class="container">
    <div class="filter-panel">
        <div class="filter-row">
            <div class="filter-group">
                <label>Количество комнат:</label>
                <select>
                    <option>Все планировки</option>
                    <option>2-комнатные (от 78 м²)</option>
                    <option>3-комнатные (от 112 м²)</option>
                    <option>Пентхаусы (от 185 м²)</option>
                </select>
            </div>
            <div class="filter-group">
                <label>Секция &amp; Этаж:</label>
                <select>
                    <option>Любой этаж</option>
                    <option>4 – 10 этажи (вид на парк)</option>
                    <option>11 – 24 этажи (панорама города)</option>
                    <option>25 – 28 этажи (Skyline)</option>
                </select>
            </div>
            <div class="filter-group">
                <label>Особые опции:</label>
                <select>
                    <option>Терраса / Камин / Мастер-спальня</option>
                    <option>С собственной террасой</option>
                    <option>С окном в ванной комнате</option>
                </select>
            </div>
        </div>

        <div class="flats-grid">
            <div class="flat-card">
                <div class="flat-type">3-комнатная Резиденция (118.4 м²)</div>
                <div style="font-size: 13px; color: #94a3b8;">Секция А &bull; 16 этаж &bull; Окна на 3 стороны</div>
                <div class="flat-price">28 416 000 ₽</div>
                <div style="font-size: 12px; color: #cbd5e1; margin-bottom: 16px;">Ипотека: от 142 000 ₽/мес &bull; Взнос: 20%</div>
                <a href="#" class="btn-view" onclick="alert('Запись на приватный показ зафиксирована!')">Забронировать показ на iPad</a>
            </div>

            <div class="flat-card">
                <div class="flat-type">Пентхаус с Террасой (194.2 м²)</div>
                <div style="font-size: 13px; color: #94a3b8;">Секция Б &bull; 26 этаж &bull; Высота потолков 4.2 м</div>
                <div class="flat-price">54 376 000 ₽</div>
                <div style="font-size: 12px; color: #cbd5e1; margin-bottom: 16px;">Приватный лифт &bull; Выход на персональную кровлю</div>
                <a href="#" class="btn-view" onclick="alert('Запись на приватный показ зафиксирована!')">Забронировать показ на iPad</a>
            </div>

            <div class="flat-card">
                <div class="flat-type">2-комнатная Suite (82.1 м²)</div>
                <div style="font-size: 13px; color: #94a3b8;">Секция А &bull; 9 этаж &bull; Французские балконы</div>
                <div class="flat-price">19 704 000 ₽</div>
                <div style="font-size: 12px; color: #cbd5e1; margin-bottom: 16px;">Мастер-спальня с гардеробной 8 м²</div>
                <a href="#" class="btn-view" onclick="alert('Запись на приватный показ зафиксирована!')">Забронировать показ на iPad</a>
            </div>
        </div>
    </div>
</div>

</body>
</html>
"""

with open(os.path.join(DEMOS_DIR, "real-estate-demo", "index.html"), "w", encoding="utf-8") as f:
    f.write(re_demo_html)
print("demos/real-estate-demo/index.html создан!")

# ------------------------------------------------------------------------------
# 4. ДЕМО 4: ПРЕМИУМ HORECA & ОТЕЛИ (Троекуров, Kitchen, Hyatt)
# ------------------------------------------------------------------------------
horeca_demo_html = """<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ресторан «Дворянское Собрание» | Премиальная Гастрономия</title>
    <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,600;0,700;1,400&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
    <style>
        :root {
            --gold: #C5A059;
            --dark: #0D0F14;
            --surface: #161922;
            --text: #F8FAFC;
        }
        * { margin:0; padding:0; box-sizing:border-box; font-family: 'Inter', sans-serif; }
        body { background: var(--dark); color: var(--text); }
        .hero { height: 75vh; background: radial-gradient(circle at center, #1a1e2b 0%, #0d0f14 100%); display: flex; flex-direction: column; justify-content: center; align-items: center; text-align: center; padding: 20px; }
        .hero h1 { font-family: 'Playfair Display', serif; font-size: clamp(2.4rem, 4.5vw, 4rem); color: var(--gold); margin-bottom: 10px; }
        .hero p { font-size: 1.15rem; color: #94a3b8; font-style: italic; max-width: 600px; margin-bottom: 25px; }
        .container { max-width: 900px; margin: -40px auto 60px; padding: 0 20px; }
        .booking-box { background: var(--surface); border: 1px solid rgba(197,160,89,0.3); border-radius: 16px; padding: 36px; box-shadow: 0 20px 40px rgba(0,0,0,0.5); }
        .form-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 20px; margin-bottom: 25px; }
        .form-group label { display: block; font-size: 12px; text-transform: uppercase; letter-spacing: 1.5px; color: var(--gold); margin-bottom: 8px; font-weight: 600; }
        .form-group select, .form-group input { width: 100%; background: #0d0f14; border: 1px solid rgba(255,255,255,0.15); color: #fff; padding: 12px 14px; border-radius: 8px; outline: none; }
        .btn-reserve { width: 100%; background: var(--gold); color: #000; border: none; padding: 16px; border-radius: 8px; font-weight: 700; font-size: 16px; cursor: pointer; transition: 0.2s; }
        .btn-reserve:hover { background: #e0c07a; }
    </style>
</head>
<body>

<div class="hero">
    <div style="font-size: 11px; letter-spacing: 4px; color: var(--gold); margin-bottom: 12px;">ЕКАТЕРИНБУРГ &bull; ВЫСОКАЯ КУХНЯ</div>
    <h1>Дворянское Собрание</h1>
    <p>Историческая дворянская гастрономия, винный погреб и приватные кабинеты для деловых ужинов.</p>
</div>

<div class="container">
    <div class="booking-box">
        <h2 style="font-family: 'Playfair Display', serif; font-size: 1.6rem; color: #fff; margin-bottom: 6px;">Мгновенное Бронирование VIP-Стола</h2>
        <p style="font-size: 13px; color: #94a3b8; margin-bottom: 24px;">Гарантия столика без звонков хостес. Подтверждение в Telegram за 3 секунды.</p>

        <div class="form-grid">
            <div class="form-group">
                <label>Дата визита:</label>
                <input type="date" value="2026-10-15">
            </div>
            <div class="form-group">
                <label>Время:</label>
                <select>
                    <option>19:00 (Вечерний ужин)</option>
                    <option>20:00 (Живой джаз)</option>
                    <option>21:30 (Поздний ужин)</option>
                    <option>13:00 (Деловой обед)</option>
                </select>
            </div>
            <div class="form-group">
                <label>Количество гостей:</label>
                <select>
                    <option>2 персоны (Романтический стол)</option>
                    <option>4 персоны</option>
                    <option>6–10 персон (Каминный зал)</option>
                    <option>12+ персон (VIP Банкет)</option>
                </select>
            </div>
            <div class="form-group">
                <label>Предпочтение зала:</label>
                <select>
                    <option>У камина XIX века</option>
                    <option>Панорамная терраса</option>
                    <option>Закрытый сигарный кабинет</option>
                </select>
            </div>
        </div>

        <button class="btn-reserve" onclick="alert('Стол зарезервирован! Клиенту в Telegram мгновенно отправлен электронный VIP-билет с геолокацией парковки.')">Зарезервировать Стол с Гарантией</button>
    </div>
</div>

</body>
</html>
"""

with open(os.path.join(DEMOS_DIR, "horeca-demo", "index.html"), "w", encoding="utf-8") as f:
    f.write(horeca_demo_html)
print("demos/horeca-demo/index.html создан!")

# ------------------------------------------------------------------------------
# 5. ДЕМО 5: МЕДИЦИНА & ЭСТЕТИКА (УГМК-Здоровье, Нудельман, Здоровье 365)
# ------------------------------------------------------------------------------
medical_demo_html = """<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Центр Инновационной Медицины & Эстетики | Екатеринбург</title>
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@500;600;700&family=Inter:wght@400;500&display=swap" rel="stylesheet">
    <style>
        :root {
            --primary: #0EA5E9;
            --dark: #0A0F1D;
            --surface: #131B2E;
            --text: #F8FAFC;
            --gray: #94A3B8;
        }
        * { margin:0; padding:0; box-sizing:border-box; font-family: 'Plus Jakarta Sans', sans-serif; }
        body { background: var(--dark); color: var(--text); }
        .header { background: #070B14; border-bottom: 1px solid rgba(255,255,255,0.08); padding: 18px 30px; display: flex; justify-content: space-between; align-items: center; }
        .container { max-width: 1050px; margin: 40px auto; padding: 0 20px; }
        .hero { text-align: center; margin-bottom: 45px; }
        .hero h1 { font-size: clamp(2rem, 3.5vw, 3rem); color: #fff; margin-bottom: 12px; }
        .triage-card { background: var(--surface); border: 1px solid rgba(14,165,233,0.3); border-radius: 16px; padding: 36px; box-shadow: 0 20px 45px rgba(0,0,0,0.4); }
        .step-label { font-size: 12px; text-transform: uppercase; letter-spacing: 2px; color: var(--primary); font-weight: 700; margin-bottom: 12px; }
        .question-title { font-size: 1.4rem; font-weight: 600; color: #fff; margin-bottom: 20px; }
        .options-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 14px; margin-bottom: 25px; }
        .option-btn { background: #0A0F1D; border: 1px solid rgba(255,255,255,0.12); color: #e2e8f0; padding: 16px; border-radius: 10px; text-align: left; cursor: pointer; transition: 0.2s; font-size: 14px; font-weight: 500; }
        .option-btn:hover, .option-btn.selected { border-color: var(--primary); background: rgba(14,165,233,0.1); color: #fff; }
        .btn-confirm { background: var(--primary); color: #000; border: none; padding: 14px 30px; border-radius: 8px; font-weight: 700; font-size: 15px; cursor: pointer; width: 100%; }
    </style>
</head>
<body>

<div class="header">
    <div style="font-weight: 700; font-size: 18px; color: #fff;">МЕДИЦИНСКИЙ ЦЕНТР ЭКСПЕРТНОГО КЛАССА</div>
    <div style="font-size: 12px; background: rgba(14,165,233,0.15); border: 1px solid var(--primary); color: #38bdf8; padding: 4px 12px; border-radius: 20px; font-weight: 600;">AI-ТРИАЖ ДЛЯ КЛИНИК</div>
</div>

<div class="container">
    <div class="hero">
        <h1>Интеллектуальный Подбор Врача &amp; Онлайн-Запись</h1>
        <p style="color: var(--gray); font-size: 1.1rem; max-width: 650px; margin: 0 auto;">Пациент отвечает на 3 вопроса, система определяет профиль специалиста и бронирует время без очередей в регистратуре.</p>
    </div>

    <div class="triage-card">
        <div class="step-label">Шаг 1 из 3: Симптомы и Цель Обращения</div>
        <div class="question-title">Какое направление вас интересует?</div>

        <div class="options-grid">
            <button class="option-btn selected" onclick="selectOpt(this)">🩺 Экспертная диагностика &amp; Чек-ап</button>
            <button class="option-btn" onclick="selectOpt(this)">✨ Лазерная эстетика &amp; Омоложение</button>
            <button class="option-btn" onclick="selectOpt(this)">🦷 Имплантация &amp; Реставрация зубов</button>
            <button class="option-btn" onclick="selectOpt(this)">🔬 Пластическая хирургия &amp; Консультация</button>
        </div>

        <div class="step-label">Шаг 2: Удобное Время</div>
        <div class="question-title">Когда планируете визит?</div>
        <div class="options-grid">
            <button class="option-btn selected" onclick="selectOpt(this)">Сегодня (Срочный прием)</button>
            <button class="option-btn" onclick="selectOpt(this)">Завтра утро (09:00 – 12:00)</button>
            <button class="option-btn" onclick="selectOpt(this)">Выходные дни</button>
            <button class="option-btn" onclick="selectOpt(this)">Онлайн-консультация по видео</button>
        </div>

        <button class="btn-confirm" onclick="alert('Запись зафиксирована! Пациенту мгновенно отправлена памятка о подготовке к приему в WhatsApp.')">Подтвердить Запись и Получить Направление</button>
    </div>
</div>

<script>
    function selectOpt(el) {
        el.parentElement.querySelectorAll('.option-btn').forEach(b => b.classList.remove('selected'));
        el.classList.add('selected');
    }
</script>

</body>
</html>
"""

with open(os.path.join(DEMOS_DIR, "medical-demo", "index.html"), "w", encoding="utf-8") as f:
    f.write(medical_demo_html)
print("demos/medical-demo/index.html создан!")

# ------------------------------------------------------------------------------
# 6. ДЕМО 6: B2B СЕРВИСЫ, ПИЩЕПРОМ & ТУРИЗМ (Черкашин, СМАК, АУЖД, Синячиха Музей)
# ------------------------------------------------------------------------------
service_demo_html = """<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>УралПромСервис | Оптовые Заказы, Туризм & B2B Поставки</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
    <style>
        :root {
            --primary: #6366F1;
            --dark: #0B0E14;
            --surface: #141A26;
            --text: #F8FAFC;
            --gray: #94A3B8;
        }
        * { margin:0; padding:0; box-sizing:border-box; font-family: 'Inter', sans-serif; }
        body { background: var(--dark); color: var(--text); }
        .hero { padding: 60px 20px; text-align: center; background: linear-gradient(180deg, #1e1b4b 0%, var(--dark) 100%); }
        .hero h1 { font-size: clamp(2rem, 3.5vw, 2.8rem); color: #fff; margin-bottom: 10px; }
        .container { max-width: 1000px; margin: 0 auto 50px; padding: 0 20px; }
        .grid-serv { display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 20px; margin-top: 30px; }
        .serv-card { background: var(--surface); border: 1px solid rgba(255,255,255,0.08); border-radius: 12px; padding: 24px; transition: 0.2s; }
        .serv-card:hover { border-color: var(--primary); transform: translateY(-4px); }
        .serv-badge { background: rgba(99,102,241,0.15); color: #818cf8; font-size: 11px; font-weight: 700; padding: 4px 8px; border-radius: 4px; display: inline-block; margin-bottom: 12px; }
        .serv-title { font-size: 1.25rem; font-weight: 700; color: #fff; margin-bottom: 8px; }
        .btn-act { display: inline-block; width: 100%; text-align: center; background: var(--primary); color: #fff; padding: 10px; border-radius: 6px; font-weight: 600; text-decoration: none; margin-top: 16px; font-size: 14px; }
        .btn-act:hover { background: #4f46e5; }
    </style>
</head>
<body>

<div class="hero">
    <div style="font-size: 11px; letter-spacing: 3px; color: #818cf8; margin-bottom: 8px;">ОПТОВЫЕ СЕТИ &bull; ТУРИЗМ &bull; РЕГИОНАЛЬНЫЕ УСЛУГИ</div>
    <h1>Единая Платформа B2B-Заказов и Туризма</h1>
    <p style="color: var(--gray); font-size: 1.1rem; max-width: 650px; margin: 0 auto;">Автоматизация поставок для ритейла и ресторанов (Черкашин, СМАК, Талицы) + онлайн-билеты на АУЖД и Музей Синячихи.</p>
</div>

<div class="container">
    <div class="grid-serv">
        <div class="serv-card">
            <span class="serv-badge">HORECA & РИТЕЙЛ</span>
            <div class="serv-title">Мясная &amp; Молочная Гастрономия</div>
            <p style="color: var(--gray); font-size: 13px;">Прямой заказ деликатесов и свежего фермерского молока для ресторанов и кофеен без посредников.</p>
            <a href="#" class="btn-act" onclick="alert('Оптовый заказ на 450 кг продукции сформирован!')">Открыть Оптовый Заказ</a>
        </div>

        <div class="serv-card">
            <span class="serv-badge">ТУРИЗМ & КУЛЬТУРА</span>
            <div class="serv-title">Ретропоезд АУЖД (Алапаевск)</div>
            <p style="color: var(--gray); font-size: 13px;">Бронирование мест в вагоне узкоколейного поезда, экскурсии, ночевка и питание для групп из Екатеринбурга.</p>
            <a href="#" class="btn-act" onclick="alert('Билеты на ретропоезд забронированы!')">Купить Турпакет Онлайн</a>
        </div>

        <div class="serv-card">
            <span class="serv-badge">МУЗЕЙ-ЗАПОВЕДНИК</span>
            <div class="serv-title">Нижняя Синячиха &bull; Деревянное Зодчество</div>
            <p style="color: var(--gray); font-size: 13px;">Интерактивный цифровой билет, аудиогид по старинным башням и часовням, заказ мастер-классов.</p>
            <a href="#" class="btn-act" onclick="alert('Цифровой аудиогид активирован!')">Включить Аудиогид</a>
        </div>
    </div>
</div>

</body>
</html>
"""

with open(os.path.join(DEMOS_DIR, "service-demo", "index.html"), "w", encoding="utf-8") as f:
    f.write(service_demo_html)
print("demos/service-demo/index.html создан!")

print("\nВсе 6 интерактивных демо успешно созданы!")
