import pandas as pd
import sqlite3
import os


def run():
    print("--- Запуск модуля data_load ---")
    data_path = '/data/dataset.csv'
    db_path = '/db/alerts.db'

    if not os.path.exists(data_path):
        print(f"Помилка: Файл {data_path} не знайдено!")
        return

    print("Читання CSV файлу...")
    df = pd.read_csv(data_path)

    print("Збереження в базу даних SQLite...")
    conn = sqlite3.connect(db_path)
    df.to_sql('alerts', conn, if_exists='replace', index=False)
    conn.close()

    print("Дані успішно завантажено в БД!")


if __name__ == "__main__":
    run()