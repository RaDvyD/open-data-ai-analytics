from flask import Flask, send_from_directory, render_template_string
import os
import json

app = Flask(__name__)

# Простий HTML-шаблон для красивого відображення
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Аналіз повітряних тривог</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 40px; background-color: #f9f9f9;}
        .container { max-width: 900px; margin: auto; background: white; padding: 30px; box-shadow: 0 0 10px rgba(0,0,0,0.1); border-radius: 8px;}
        h1, h2 { color: #333; }
        pre { background: #f4f4f4; padding: 15px; border-radius: 5px; white-space: pre-wrap;}
        img { max-width: 100%; height: auto; border: 1px solid #ccc; margin-top: 10px; border-radius: 4px;}
    </style>
</head>
<body>
    <div class="container">
        <h1>Аналіз відкритих даних (Повітряні тривоги)</h1>
        <p><strong>Виконав:</strong> Семенов Олександр Володимирович</p>

        <h2>1. Перевірка якості даних</h2>
        <pre>{{ quality }}</pre>

        <h2>2. Дослідження даних (Базова статистика)</h2>
        <pre>{{ research }}</pre>

        <h2>3. Візуалізація</h2>
        <h3>Кількість тривог по областях</h3>
        <img src="/reports/plot1_oblasts.png" alt="Графік 1">

        <h3>Розподіл тривалості тривог</h3>
        <img src="/reports/plot2_duration.png" alt="Графік 2">
    </div>
</body>
</html>
"""


@app.route('/')
def index():
    # Читаємо звіт про якість
    quality_text = "Звіт не знайдено..."
    if os.path.exists('/reports/quality_report.txt'):
        with open('/reports/quality_report.txt', 'r', encoding='utf-8') as f:
            quality_text = f.read()

    # Читаємо дослідження
    research_text = "Звіт не знайдено..."
    if os.path.exists('/reports/research_report.json'):
        with open('/reports/research_report.json', 'r', encoding='utf-8') as f:
            research_text = json.dumps(json.load(f), indent=4, ensure_ascii=False)

    return render_template_string(HTML_TEMPLATE, quality=quality_text, research=research_text)


# Спеціальний шлях, щоб Flask міг віддавати картинки з папки /reports
@app.route('/reports/<filename>')
def serve_report(filename):
    return send_from_directory('/reports', filename)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)