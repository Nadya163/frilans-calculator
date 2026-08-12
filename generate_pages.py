"""
generate_pages.py — генератор страниц сайта «Фриланс-Калькулятор».

Запуск:
    python generate_pages.py

Что генерирует:
    index.html                          — главная (оба блока, режим «на руки»)
    kalkulyator-stavki-v-chas.html      — только часовой калькулятор
    nalog-samozanyatogo-kalkulyator.html — только блок налога, режим «на руки»
    skolko-vzyat-s-zakaza.html          — только блок налога, режим «что выставить»
    stavka-frilansera-v-den-mesyats.html — часовой + строка «в день»
    kalkulyator-dlya-samozanyatogo-it.html — оба блока + блок лимита 2,4 млн
    sitemap.xml
    robots.txt

ВАЖНО перед деплоем:
    1. Замените BASE_URL на купленный домен.
    2. Вставьте код Яндекс.Метрики вместо <!-- YANDEX_METRIKA --> в каждом файле.
"""

import os

BASE_URL  = "https://frilans-calculator.ru" 
SITE_NAME = "Фриланс-Калькулятор"
OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))


PAGES = [
    {
        "slug":     "index",
        "filename": "index.html",
        "nav_label": "Калькулятор",
        "title":    "Калькулятор ставки фрилансера и налога самозанятого 2026",
        "description": (
            "Бесплатный калькулятор для фрилансеров и самозанятых: посчитайте "
            "налог НПД 4% или 6%, сколько получите на руки или что выставить "
            "клиенту. Учитывает вычет 10 000 ₽."
        ),
        "h1":  "Калькулятор ставки фрилансера и налога самозанятого",
        "lead": (
            "Посчитайте, сколько денег останется на руках после налога НПД, "
            "или сколько нужно выставить клиенту, чтобы получить нужную сумму. "
            "Расчёт мгновенный — данные никуда не отправляются."
        ),
        "calc_config": {"mainMode": "net", "showHourly": True, "showLimit": False},
        "show_day_row": False,
        "article": """
<h2>Как считается налог самозанятого в 2026 году</h2>
<p>Самозанятые платят налог на профессиональный доход (НПД) по двум ставкам:
4% — если оплату вносит физлицо, и 6% — если платит юрлицо или ИП.
По действующему закону 422-ФЗ ставки не будут повышены до конца 2028 года.</p>
<h2>Что такое налоговый вычет 10 000 ₽</h2>
<p>При регистрации самозанятому даётся налоговый вычет 10 000 ₽. Пока он
не исчерпан, ставка снижается до 3% (физлица) и 4% (юрлица/ИП).
Включите галочку «Учесть вычет» — калькулятор учтёт его автоматически.</p>
<h2>Лимит дохода самозанятого</h2>
<p>Годовой доход ограничен 2,4 млн ₽. При превышении нужно переходить
на УСН или патент.</p>
""",
    },
    {
        "slug":     "kalkulyator-stavki-v-chas",
        "filename": "kalkulyator-stavki-v-chas.html",
        "nav_label": "Ставка в час",
        "title":    "Калькулятор почасовой ставки фрилансера — сколько брать за час работы",
        "description": (
            "Рассчитайте доход фрилансера по часовой ставке с учётом налога "
            "НПД 4% или 6%. Укажите ставку и часы — узнайте доход в месяц на руки."
        ),
        "h1":  "Калькулятор почасовой ставки фрилансера",
        "lead": (
            "Укажите ставку за час и количество рабочих часов в неделю — "
            "калькулятор покажет, сколько вы заработаете в месяц на руки "
            "с учётом налога самозанятого."
        ),
        "calc_config": {"mainMode": "hidden", "showHourly": True, "showLimit": False},
        "show_day_row": False,
        "article": """
<h2>Как выбрать почасовую ставку</h2>
<p>Ставка за час должна покрывать налог, простои между заказами, отпуск
и непредвиденные расходы. Многие фрилансеры закладывают 20–30% сверху
желаемого чистого дохода — именно для этого и нужен калькулятор.</p>
<h2>Пример расчёта</h2>
<p>При ставке 1500 ₽/час, 25 часах в неделю и работе с физлицами (4%) —
доход в месяц до налога около 162 000 ₽, на руки около 155 500 ₽.
Введите свои цифры выше.</p>
""",
    },
    {
        "slug":     "nalog-samozanyatogo-kalkulyator",
        "filename": "nalog-samozanyatogo-kalkulyator.html",
        "nav_label": "Налог НПД",
        "title":    "Калькулятор налога самозанятого (НПД) 4% и 6% онлайн — 2026",
        "description": (
            "Онлайн-калькулятор налога на профессиональный доход: 4% с физлиц, "
            "6% с юрлиц и ИП. Учитывает налоговый вычет 10 000 ₽. Расчёт в браузере."
        ),
        "h1":  "Калькулятор налога самозанятого — НПД 4% и 6%",
        "lead": (
            "Введите сумму дохода от клиента — калькулятор покажет, "
            "сколько уйдёт на налог НПД и сколько останется на руках. "
            "Данные не покидают ваш браузер."
        ),
        "calc_config": {"mainMode": "net", "showHourly": False, "showLimit": False},
        "show_day_row": False,
        "article": """
<h2>Кто платит 4%, а кто 6%</h2>
<p>Ставка зависит исключительно от типа плательщика: 4% — если оплату
вносит физлицо, 6% — если юрлицо или ИП. Вид деятельности на ставку
не влияет.</p>
<h2>Когда приходит уведомление о налоге</h2>
<p>ФНС присылает уведомление в приложении «Мой налог» до 12 числа следующего
месяца, оплатить нужно до 28 числа. Калькулятор поможет заранее
отложить нужную сумму.</p>
""",
    },
    {
        "slug":     "skolko-vzyat-s-zakaza",
        "filename": "skolko-vzyat-s-zakaza.html",
        "nav_label": "Сумма заказа",
        "title":    "Сколько взять с заказа фрилансеру, чтобы не потерять на налоге",
        "description": (
            "Калькулятор считает, сколько выставить клиенту, чтобы после "
            "уплаты налога НПД получить нужную сумму на руки. Учитывает вычет."
        ),
        "h1":  "Сколько взять с заказа, чтобы получить нужную сумму на руки",
        "lead": (
            "Укажите, сколько хотите получить на руки, — калькулятор "
            "посчитает, какую сумму указать в счёте клиенту с учётом "
            "налога 4% или 6%."
        ),
        "calc_config": {"mainMode": "gross", "showHourly": False, "showLimit": False},
        "show_day_row": False,
        "article": """
<h2>Частая ошибка при выставлении счёта</h2>
<p>Многие фрилансеры выставляют клиенту ровно ту сумму, которую хотят
получить, — и теряют 4–6% на налог. Правильнее закладывать налог
в стоимость сразу. Калькулятор считает нужную сумму за вас.</p>
<h2>Формула без вычета</h2>
<p>Сумма клиенту = желаемый доход ÷ (1 − ставка НПД). При ставке 6%:
хотите 100 000 ₽ — выставляйте 106 383 ₽. Калькулятор считает с точностью
до копейки и учитывает остаток вычета 10 000 ₽.</p>
""",
    },
    {
        "slug":     "stavka-frilansera-v-den-mesyats",
        "filename": "stavka-frilansera-v-den-mesyats.html",
        "nav_label": "В день / в месяц",
        "title":    "Ставка фрилансера в день и в месяц — калькулятор дохода онлайн",
        "description": (
            "Переведите почасовую ставку в доход за рабочий день и за месяц "
            "с учётом налога НПД самозанятого 4% или 6%."
        ),
        "h1":  "Ставка фрилансера в день и в месяц",
        "lead": (
            "Переведите часовую ставку в доход за день и за месяц — "
            "с учётом налога НПД. Введите ставку и часы в неделю, "
            "калькулятор покажет обе суммы."
        ),
        "calc_config": {"mainMode": "hidden", "showHourly": True, "showLimit": False},
        "show_day_row": True,
        "article": """
<h2>Сколько часов в месяце закладывать фрилансеру</h2>
<p>Даже при полной загрузке фрилансер редко продаёт больше 25–30 часов в
неделю: часть времени уходит на поиск заказов, переписку и административные
задачи. Это стоит учитывать при планировании дохода.</p>
<h2>Среднее количество недель в месяце</h2>
<p>Точное значение — 4,33 недели (52 недели ÷ 12 месяцев). Калькулятор
подставляет его по умолчанию, но вы можете изменить на удобное число.</p>
""",
    },
    {
        "slug":     "kalkulyator-dlya-samozanyatogo-it",
        "filename": "kalkulyator-dlya-samozanyatogo-it.html",
        "nav_label": "Для IT-фрилансера",
        "title":    "Калькулятор для самозанятого IT-фрилансера — ставка, налог, лимит дохода",
        "description": (
            "Калькулятор для самозанятых разработчиков и дизайнеров: ставка "
            "НПД 4%/6%, почасовой доход, контроль лимита 2,4 млн ₽ в год."
        ),
        "h1":  "Калькулятор для самозанятого IT-фрилансера",
        "lead": (
            "Разработчики, дизайнеры и другие IT-специалисты на НПД — "
            "посчитайте налог, доход в месяц и следите за лимитом 2,4 млн ₽ "
            "в год. Всё в браузере, без регистрации."
        ),
        "calc_config": {"mainMode": "net", "showHourly": True, "showLimit": True},
        "show_day_row": False,
        "article": """
<h2>Может ли IT-специалист быть самозанятым</h2>
<p>Да — разработка, дизайн, консультации, тестирование и другая IT-работа
подпадают под НПД, если нет трудового договора с текущим заказчиком менее
двух лет назад. Ограничение — доход не выше 2,4 млн ₽ в год.</p>
<h2>Что делать при приближении к лимиту</h2>
<p>При прогнозе выше 2 млн ₽ стоит заранее зарегистрировать ИП и перейти
на УСН или патент — это лучше, чем потерять статус самозанятого в середине
налогового периода.</p>
""",
    },
]

SECURITY_BADGE = """      <p class="security-badge">🔒 Расчёт в браузере — данные никуда не отправляются</p>"""

MAIN_CALC_BLOCK = """\
      <div class="calc-card" id="calc-main">
        <div class="mode-toggle">
          <button type="button" id="modeNet">Сколько получу на руки</button>
          <button type="button" id="modeGross">Сколько выставить клиенту</button>
        </div>

        <div class="field-row">
          <div class="field">
            <label id="amountLabel" for="amount">Сумма от клиента, ₽</label>
            <input type="number" id="amount" min="0" step="100" value="50000">
          </div>
          <div class="field">
            <label for="clientType">Кто платит</label>
            <select id="clientType">
              <option value="fl">Физлицо (4%)</option>
              <option value="ul">Юрлицо / ИП (6%)</option>
            </select>
          </div>
        </div>

        <label class="checkbox-row">
          <input type="checkbox" id="useDeduction">
          Учесть налоговый вычет 10 000 ₽ (снижает ставку до его исчерпания)
        </label>
        <div class="field-row" id="deductionRow" style="display:none;">
          <div class="field">
            <label for="deductionRemaining">Остаток вычета, ₽</label>
            <input type="number" id="deductionRemaining" min="0" step="100" value="10000">
          </div>
        </div>

        <div class="result">
          <div class="result-row main">
            <span class="label" id="resultMainLabel">Получите на руки</span>
            <span class="value" id="resultMain">—</span>
          </div>
          <div class="result-row tax">
            <span class="label">Налог НПД</span>
            <span class="value" id="resultTax">—</span>
          </div>
          <div class="result-row">
            <span class="label">Ставка</span>
            <span class="value" id="resultRate">—</span>
          </div>
          <div class="result-row" id="resultDeductionRow" style="display:none;">
            <span class="label">Остаток вычета после расчёта</span>
            <span class="value" id="resultDeductionLeft">—</span>
          </div>
        </div>
{security}
      </div>"""

HOURLY_HEADER = """\
      <h2 class="section-title" id="hourly-title">{title}</h2>
      <p class="section-sub" id="hourly-sub">{sub}</p>"""

def hourly_block(show_day_row):
    day_row_html = ""
    if show_day_row:
        day_row_html = """
          <div class="result-row">
            <span class="label">На руки за 8-часовой день</span>
            <span class="value" id="hourlyDay">—</span>
          </div>"""
    return """\
      <div class="calc-card" id="calc-hourly">
        <div class="field-row">
          <div class="field">
            <label for="hourlyRate">Ставка, ₽ / час</label>
            <input type="number" id="hourlyRate" min="0" step="50" value="1200">
          </div>
          <div class="field">
            <label for="hoursPerWeek">Часов в неделю</label>
            <input type="number" id="hoursPerWeek" min="0" step="1" value="25">
          </div>
        </div>
        <div class="field-row">
          <div class="field">
            <label for="weeksPerMonth">Недель в месяце</label>
            <input type="number" id="weeksPerMonth" min="0" step="0.01" value="4.33">
          </div>
          <div class="field">
            <label for="clientTypeHourly">Кто платит</label>
            <select id="clientTypeHourly">
              <option value="fl">Физлицо (4%)</option>
              <option value="ul">Юрлицо / ИП (6%)</option>
            </select>
          </div>
        </div>

        <label class="checkbox-row">
          <input type="checkbox" id="useDeductionHourly">
          Учесть налоговый вычет 10 000 ₽
        </label>
        <div class="field-row" id="deductionRowHourly" style="display:none;">
          <div class="field">
            <label for="deductionRemainingHourly">Остаток вычета, ₽</label>
            <input type="number" id="deductionRemainingHourly" min="0" step="100" value="10000">
          </div>
        </div>

        <div class="result">
          <div class="result-row">
            <span class="label">Доход в месяц до налога</span>
            <span class="value" id="hourlyGross">—</span>
          </div>
          <div class="result-row tax">
            <span class="label">Налог НПД</span>
            <span class="value" id="hourlyTax">—</span>
          </div>
          <div class="result-row main">
            <span class="label">На руки в месяц</span>
            <span class="value" id="hourlyNet">—</span>
          </div>{day_row}
        </div>
{security}
      </div>""".format(
        day_row=day_row_html,
        security=SECURITY_BADGE
    )

LIMIT_BLOCK = """\
      <div id="limit-block" style="display:none;">
        <h2 class="section-title">Контроль лимита дохода</h2>
        <p class="section-sub">Самозанятый не может зарабатывать больше 2 400 000 ₽ в год.</p>
        <div class="calc-card">
          <div class="limit-bar-wrap">
            <div class="limit-bar-track">
              <div class="limit-bar-fill" id="limitBar" style="width:0%;"></div>
            </div>
          </div>
          <p class="hint" id="limitLabel">Введите данные в калькуляторе выше</p>
        </div>
      </div>"""

HTML_TEMPLATE = """\
<!doctype html>
<html lang="ru">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{description}">
<link rel="canonical" href="{canonical}">
<meta property="og:type" content="website">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:url" content="{canonical}">
<link rel="icon" type="image/svg+xml" href="./favicon.svg">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Manrope:wght@700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="./assets/style.css">
<script>window.CALC_CONFIG = {calc_config_json};</script>
</head>
<body>
<!-- YANDEX_METRIKA -->

<header class="site-header">
  <div class="container">
    <a href="./index.html" class="brand">
      <img src="./favicon.svg" alt="{site_name}">
      <span>{site_name}</span>
    </a>
    <nav class="site-nav">
{nav_links}
    </nav>
  </div>
</header>

<main>
  <section class="hero container">
    <h1>{h1}</h1>
    <p class="lead">{lead}</p>
  </section>

  <div class="container">

{main_block}

{hourly_header}

{hourly_calc}

{limit_block}

    <article class="article">
{article}
    </article>

    <div class="related">
      <h2>Другие расчёты</h2>
      <ul>
{related_links}
      </ul>
    </div>

  </div>
</main>

<footer class="site-footer">
  <div class="container">
    {site_name} · расчёт носит справочный характер и не является налоговой консультацией
  </div>
</footer>

<script src="./assets/tool.js"></script>
</body>
</html>
"""

import json

def page_url(page):
    if page["slug"] == "index":
        return BASE_URL + "/"
    return BASE_URL + "/" + page["filename"]

def build_nav(current_slug):
    lines = []
    for p in PAGES:
        attr = ' class="active"' if p["slug"] == current_slug else ""
        lines.append(f'      <a href="./{p["filename"]}"{attr}>{p["nav_label"]}</a>')
    return "\n".join(lines)

def build_related(current_slug):
    lines = []
    for p in PAGES:
        if p["slug"] == current_slug:
            continue
        lines.append(f'        <li><a href="./{p["filename"]}">{p["title"]}</a></li>')
    return "\n".join(lines)

def generate():
    for page in PAGES:
        cfg    = page["calc_config"]
        is_hidden_main  = cfg.get("mainMode") == "hidden"
        is_hourly       = cfg.get("showHourly", True)
        is_limit        = cfg.get("showLimit", False)
        has_day_row     = page.get("show_day_row", False)

        main_html = ""
        if not is_hidden_main:
            main_html = MAIN_CALC_BLOCK.format(security="\n" + SECURITY_BADGE)

        hourly_hdr = ""
        if is_hourly:
            if is_hidden_main:
                title_txt = "Расчёт дохода по часовой ставке"
                sub_txt   = "Укажите ставку и часы — получите доход в месяц на руки."
            else:
                title_txt = "Часовая ставка → доход в месяц"
                sub_txt   = "Переведите ставку за час в доход за месяц с учётом налога."
            hourly_hdr = HOURLY_HEADER.format(title=title_txt, sub=sub_txt)

        hourly_html = ""
        if is_hourly:
            hourly_html = hourly_block(has_day_row)

        limit_html = LIMIT_BLOCK if is_limit else ""

        html = HTML_TEMPLATE.format(
            title=page["title"],
            description=page["description"],
            canonical=page_url(page),
            site_name=SITE_NAME,
            calc_config_json=json.dumps(cfg, ensure_ascii=False),
            nav_links=build_nav(page["slug"]),
            h1=page["h1"],
            lead=page["lead"],
            main_block=main_html,
            hourly_header=hourly_hdr,
            hourly_calc=hourly_html,
            limit_block=limit_html,
            article=page["article"].strip(),
            related_links=build_related(page["slug"]),
        )

        out = os.path.join(OUTPUT_DIR, page["filename"])
        with open(out, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"OK  {page['filename']}")

def generate_sitemap():
    lines = ['<?xml version="1.0" encoding="UTF-8"?>',
             '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for p in PAGES:
        lines += ["  <url>", f"    <loc>{page_url(p)}</loc>", "  </url>"]
    lines.append("</urlset>")
    out = os.path.join(OUTPUT_DIR, "sitemap.xml")
    with open(out, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print("OK  sitemap.xml")

def generate_robots():
    out = os.path.join(OUTPUT_DIR, "robots.txt")
    with open(out, "w", encoding="utf-8") as f:
        f.write(f"User-agent: *\nAllow: /\n\nSitemap: {BASE_URL}/sitemap.xml\n")
    print("OK  robots.txt")

if __name__ == "__main__":
    generate()
    generate_sitemap()
    generate_robots()
    print("\nГотово. Не забудьте:")
    print("1. Заменить BASE_URL на купленный домен и перезапустить генерацию.")
    print("2. Вставить код Яндекс.Метрики вместо <!-- YANDEX_METRIKA --> в каждом файле.")
