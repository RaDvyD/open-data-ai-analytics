import pandas as pd
import sqlite3
import json
import os


def run():
    print("--- Запуск модуля research ---")
    db_path = '/db/alerts.db'
    if not os.path.exists(db_path):
        print("Помилка: БД не знайдена.")
        return

    conn = sqlite3.connect(db_path)
    df = pd.read_sql('SELECT * FROM alerts', conn)
    conn.close()

    # Збираємо базову статистику
    stats = {
        "total_rows": len(df),
        "columns": list(df.columns),
        "unique_values_per_column": {col: int(df[col].nunique()) for col in df.columns}
    }

    os.makedirs('/reports', exist_ok=True)
    with open('/reports/research_report.json', 'w', encoding='utf-8') as f:
        json.dump(stats, f, ensure_ascii=False, indent=4)

    print("Звіт дослідження збережено у /reports/research_report.json")


if __name__ == "__main__":
    run()