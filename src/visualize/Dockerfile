# Спробуємо з легким образом. Якщо виникнуть проблеми з matplotlib,
# змініть на FROM python:3.12-bookworm
FROM python:3.12-slim

WORKDIR /app

# Копіюємо залежності
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копіюємо код модуля
COPY app.py .

# Запуск
CMD ["python", "app.py"]