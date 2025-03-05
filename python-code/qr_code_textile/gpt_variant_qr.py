import os
import sqlite3
import cv2
import tkinter as tk
from tkinter import filedialog, ttk, messagebox
from openpyxl import load_workbook
from pyzbar.pyzbar import decode
from PIL import Image, ImageTk
from io import BytesIO
import datetime
import unidecode

# Создание базы данных
DB_FILE = "qr_codes.db"
conn = sqlite3.connect(DB_FILE)
cursor = conn.cursor()

scanned_count = 0  # Переменная для хранения количества сканированных QR-кодов

selected_table = tk.StringVar()

def create_table(table_name):
    cursor.execute(f"""
    CREATE TABLE IF NOT EXISTS {table_name} (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        export_date TEXT,
        qr_code_path TEXT,
        qr_number INTEGER
    )
    """)
    conn.commit()

def extract_images_from_excel(file_path):
    wb = load_workbook(file_path, data_only=True)
    ws = wb.active
    file_name = os.path.splitext(os.path.basename(file_path))[0]
    folder_name = f"QR_Code_{unidecode.unidecode(file_name)}"
    save_dir = os.path.join(os.getcwd(), folder_name)
    os.makedirs(save_dir, exist_ok=True)
    table_name = unidecode.unidecode(file_name.replace(" ", "_"))
    create_table(table_name)
    
    qr_count = 0
    if hasattr(ws, '_images') and ws._images:
        for idx, image in enumerate(ws._images):
            img_data = image._data()
            img = Image.open(BytesIO(img_data))

            if img.size[0] == 166:
                if img.mode == "CMYK":
                    img = img.convert("RGB")
                qr_count += 1
                save_path = os.path.join(save_dir, f"qr_code_{qr_count}.png")
                img.save(save_path)
                export_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                cursor.execute(f"INSERT INTO {table_name} (export_date, qr_code_path, qr_number) VALUES (?, ?, ?)",
                               (export_date, save_path, qr_count))
    
    conn.commit()
    wb.close()

def import_excel():
    file_paths = filedialog.askopenfilenames(filetypes=[["Excel Files", "*.xlsx"]])
    if not file_paths:
        return
    
    for file_path in file_paths:
        extract_images_from_excel(file_path)
        table_name = os.path.splitext(os.path.basename(file_path))[0]
        table_name = unidecode.unidecode(table_name.replace(" ", "_"))
        update_table(table_name)
        add_tab(table_name)

def update_table(table_name):
    tree.delete(*tree.get_children())
    cursor.execute(f"SELECT export_date, qr_code_path, qr_number FROM {table_name}")
    qr_codes = cursor.fetchall()
    for row in qr_codes:
        tree.insert("", "end", values=row)
    count_label.config(text=f"Осталось QR-кодов: {len(qr_codes)}")
    scanned_label.config(text=f"Сканировано QR-кодов: {scanned_count}")

def scan_qr():
    global scanned_count
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        decoded_objects = decode(frame)
        for obj in decoded_objects:
            qr_code = obj.data.decode("utf-8")
            table_name = selected_table.get()
            cursor.execute(f"DELETE FROM {table_name} WHERE qr_code_path = ?", (qr_code,))
            conn.commit()
            scanned_count += 1
            update_table(table_name)
            messagebox.showinfo("QR-код найден", f"Удалён QR-код: {qr_code}")
        cv2.imshow("QR Scanner", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

def add_tab(table_name):
    tab = ttk.Frame(tab_control)
    tab_control.add(tab, text=table_name)
    tab_control.pack(expand=True, fill=tk.BOTH)
    tab_control.select(tab)
    selected_table.set(table_name)
    update_table(table_name)

def delete_table():
    table_name = selected_table.get()
    if table_name:
        cursor.execute(f"DROP TABLE IF EXISTS {table_name}")
        conn.commit()
        for tab in tab_control.tabs():
            if tab_control.tab(tab, "text") == table_name:
                tab_control.forget(tab)
                break
        messagebox.showinfo("Удалено", f"Таблица {table_name} удалена")

tk_root = tk.Tk()
tk_root.title("QR Code Manager")
tk_root.geometry("800x600")

# Верхняя панель с кнопками
control_frame = tk.Frame(tk_root)
control_frame.pack(side=tk.TOP, fill=tk.X, pady=10)

btn_scan = tk.Button(control_frame, text="📷 Сканировать QR", command=scan_qr)
btn_scan.pack(side=tk.LEFT, padx=5)

btn_import = tk.Button(control_frame, text="📂 Импорт Excel", command=import_excel)
btn_import.pack(side=tk.LEFT, padx=5)

btn_delete = tk.Button(control_frame, text="❌ Удалить таблицу", command=delete_table)
btn_delete.pack(side=tk.LEFT, padx=5)

# Панель счетчиков
count_label = tk.Label(control_frame, text="Осталось QR-кодов: 0")
count_label.pack(side=tk.LEFT, padx=10)

scanned_label = tk.Label(control_frame, text="Сканировано QR-кодов: 0")
scanned_label.pack(side=tk.LEFT, padx=10)

# Вкладки таблиц
tab_control = ttk.Notebook(tk_root)
tab_control.pack(expand=True, fill=tk.BOTH)

# Таблица QR-кодов
tree = ttk.Treeview(tk_root, columns=("Дата экспорта", "QR-код", "Номер"), show="headings")
tree.heading("Дата экспорта", text="Дата экспорта")
tree.heading("QR-код", text="QR-код")
tree.heading("Номер", text="Номер")
tree.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

tk_root.mainloop()
