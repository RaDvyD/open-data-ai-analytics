import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
import os
from datetime import datetime


def run():
    print("--- Запуск модуля visualize ---")
    db_path = '/db/alerts.db'
    if not os.path.exists(db_path):
        print("Помилка: БД не знайдена. Перевірте data_load!")
        return

    # 1. Підключення до БД та зчитування даних
    try:
        conn = sqlite3.connect(db_path)
        df = pd.read_sql('SELECT * FROM alerts', conn)
        conn.close()
    except Exception as e:
        print(f"Помилка при читанні з БД: {e}")
        return

    if df.empty:
        print("Таблиця 'alerts' порожня.")
        return

    # Створення папки для звітів, якщо її немає
    os.makedirs('/reports', exist_ok=True)

    # 2. Попередня обробка даних
    # Перетворення стовпців часу на datetime
    try:
        df['started_at'] = pd.to_datetime(df['started_at'])
        df['finished_at'] = pd.to_datetime(df['finished_at'])
    except Exception as e:
        print(f"Помилка при перетворенні дат: {e}.")

    # 3. Побудова графіків

    # --- Графік 1: Кількість тривог по областях ---
    # Фільтруємо null значення (<null>)
    df_oblasts = df[df['oblast'].notna() & (df['oblast'] != '<null>')]
    oblast_counts = df_oblasts['oblast'].value_counts()

    # Виберемо ТОП-10 областей для кращої читабельності
    oblast_counts_top = oblast_counts.head(10)

    print("Будуємо графік 1: Кількість тривог по областях...")
    plt.figure(figsize=(12, 8))
    oblast_counts_top.plot(kind='barh', color='skyblue')
    plt.title('ТОП-10 областей за кількістю повітряних тривог')
    plt.xlabel('Кількість тривог')
    plt.ylabel('Область')
    plt.gca().invert_yaxis()  # Щоб ТОП був зверху
    plt.tight_layout()
    plt.savefig('/reports/plot1_oblasts.png')
    plt.close()

    # --- Графік 2: Розподіл тривалості тривог (у хвилинах) ---
    # Перевіримо, чи успішно перетворено дати
    if df['started_at'].notna().any() and df['finished_at'].notna().any():
        print("Розраховуємо тривалість тривог та будуємо графік 2...")
        df['duration'] = (df['finished_at'] - df['started_at']).dt.total_seconds() / 60

        # Відфільтруємо аномалії (наприклад, тривалість > 0 і менше 1 тижня)
        df_duration = df[(df['duration'] > 0) & (df['duration'] < 10080)]

        plt.figure(figsize=(12, 8))
        # Створення гістограми з bins=50
        df_duration['duration'].hist(bins=50, color='lightgreen', edgecolor='black')
        plt.title('Розподіл тривалості повітряних тривог')
        plt.xlabel('Тривалість (хвилини)')
        plt.ylabel('Кількість тривог')
        plt.tight_layout()
        plt.savefig('/reports/plot2_duration.png')
        plt.close()
    else:
        print("Стовпці часу порожні, графік тривалості не побудовано.")

    print("Графіки успішно збережено у /reports/plot1_oblasts.png та /reports/plot2_duration.png")


if __name__ == "__main__":
    run()