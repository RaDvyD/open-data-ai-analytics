import pandas as pd
import sqlite3
import os


def run():
    print("--- Запуск модуля data_quality ---")
    db_path = '/db/alerts.db'

    if not os.path.exists(db_path):
        print("Помилка: База даних не знайдена. Перевірте, чи відпрацював data_load!")
        return

    # Читаємо дані зі спільної бази SQLite
    conn = sqlite3.connect(db_path)
    df = pd.read_sql('SELECT * FROM alerts', conn)
    conn.close()

    # Рахуємо пропуски та дублікати
    missing_values = df.isnull().sum().sum()
    duplicates = df.duplicated().sum()

    report = f"""Звіт перевірки якості даних:
----------------------------
Загальна кількість записів: {len(df)}
Кількість пропусків: {missing_values}
Кількість дублікатів: {duplicates}
"""

    # Зберігаємо звіт у спільну папку reports
    os.makedirs('/reports', exist_ok=True)
    with open('/reports/quality_report.txt', 'w', encoding='utf-8') as f:
        f.write(report)

    print("Звіт про якість успішно збережено у /reports/quality_report.txt")


if __name__ == "__main__":
    run()