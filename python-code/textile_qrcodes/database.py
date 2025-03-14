import os
import sqlite3

DB_FILE = "qr_codes.db"

def connect_db():
    """ Устанавливает соединение с базой данных """
    return sqlite3.connect(DB_FILE)

def create_table(table_name):
    """ Создаёт таблицу для хранения QR-кодов """
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(f"""
    CREATE TABLE IF NOT EXISTS {table_name} (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        export_date TEXT,
        qr_code_path TEXT,
        qr_number INTEGER,
        total_qr_codes INTEGER DEFAULT 0
    )
    """)
    conn.commit()
    conn.close()

def insert_qr_code(table_name, export_date, qr_code_path, qr_number):
    """ Вставляет новый QR-код в таблицу """
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(f"""
        INSERT INTO {table_name} (export_date, qr_code_path, qr_number) VALUES (?, ?, ?)
    """, (export_date, qr_code_path, qr_number))
    conn.commit()
    conn.close()

def set_total_qr_codes(table_name, total_qr_codes):
    """ Устанавливает общее количество QR-кодов в таблице """
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(f"""
        UPDATE {table_name} SET total_qr_codes = ?
    """, (total_qr_codes,))
    conn.commit()
    conn.close()

def get_total_qr_codes(table_name):
    """ Получает общее количество QR-кодов в таблице """
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(f"SELECT total_qr_codes FROM {table_name}")
    total_qr_codes = cursor.fetchone()[0]
    conn.close()
    return total_qr_codes

def get_qr_codes(table_name):
    """ Получает все QR-коды из таблицы """
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(f"PRAGMA table_info({table_name})")

    cursor.execute(f"SELECT export_date, qr_code_path, qr_number FROM {table_name}")
    qr_codes = cursor.fetchall()
    conn.close()
    return qr_codes

def delete_qr_code(table_name, qr_code_path):
    """ Удаляет QR-код из базы данных """
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(f"DELETE FROM {table_name} WHERE qr_code_path = ?", (qr_code_path,))
    conn.commit()
    # Удаление файла с диска
    if os.path.exists(qr_code_path):  
        os.remove(qr_code_path)  # Удаляем файл
        print(f"Файл {qr_code_path} удалён.")
    else:
        print(f"Файл {qr_code_path} не найден.")
    conn.close()


def delete_table(table_name):
    """Удаляет указанную таблицу из базы данных."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    
    try:
        cursor.execute(f"DROP TABLE IF EXISTS {table_name}")
        conn.commit()
        print(f"Таблица {table_name} удалена.")
        
    except Exception as e:
        print(f"Ошибка при удалении таблицы {table_name}: {e}")
    finally:
        conn.close()
        
        


def get_all_tables():
    """Возвращает список всех таблиц"""
    con = connect_db()
    cur = con.cursor()
    cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name != 'sqlite_sequence';")
    tables = cur.fetchall()
    con.close()
    return tables