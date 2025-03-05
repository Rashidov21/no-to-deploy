import os
import sqlite3
import cv2
import tkinter as tk
from tkinter import filedialog, ttk, messagebox
from openpyxl import load_workbook
from pyzbar.pyzbar import decode
from PIL import Image, ImageTk
from io import BytesIO

# Создание базы данных
DB_FILE = "qr_codes.db"
conn = sqlite3.connect(DB_FILE)
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS qr_codes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    table_name TEXT,
    qr_code TEXT UNIQUE,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
)
""")
conn.commit()

# Функция для загрузки QR-кодов из Excel
def import_excel():
    file_path = filedialog.askopenfilename(filetypes=[("Excel Files", "*.xlsx")])
    if not file_path:
        return
    
    wb = load_workbook(file_path)
    ws = wb.active
    table_name = os.path.basename(file_path)
    
    qr_codes = set()
    for img in ws._images:
        img_data = img._data()
        image = Image.open(BytesIO(img_data))
        decoded_objects = decode(image)
        for obj in decoded_objects:
            qr_codes.add(obj.data.decode("utf-8"))
    
    if qr_codes:
        cursor.executemany("INSERT OR IGNORE INTO qr_codes (table_name, qr_code) VALUES (?, ?)",
                           [(table_name, qr) for qr in qr_codes])
        conn.commit()
        messagebox.showinfo("Успешно", f"Импортировано {len(qr_codes)} QR-кодов из {table_name}")
        update_table(table_name)
    else:
        messagebox.showwarning("Ошибка", "QR-коды не найдены в файле!")

# Функция для отображения QR-кодов в Tkinter
def update_table(table_name):
    tree.delete(*tree.get_children())
    cursor.execute("SELECT qr_code FROM qr_codes WHERE table_name = ?", (table_name,))
    for row in cursor.fetchall():
        tree.insert("", "end", values=row)

# Функция для сканирования QR-кода через веб-камеру
def scan_qr():
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        decoded_objects = decode(frame)
        for obj in decoded_objects:
            qr_code = obj.data.decode("utf-8")
            cursor.execute("DELETE FROM qr_codes WHERE qr_code = ?", (qr_code,))
            conn.commit()
            update_table(selected_table.get())
            messagebox.showinfo("QR-код найден", f"Удалён QR-код: {qr_code}")
        cv2.imshow("QR Scanner", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

# Создание графического интерфейса
tk_root = tk.Tk()
tk_root.title("QR Code Manager")
tk_root.geometry("600x400")

top_frame = tk.Frame(tk_root)
top_frame.pack(pady=10)

btn_import = tk.Button(top_frame, text="📂 Импорт Excel", command=import_excel)
btn_import.pack(side=tk.LEFT, padx=5)

btn_scan = tk.Button(top_frame, text="📷 Сканировать QR", command=scan_qr)
btn_scan.pack(side=tk.LEFT, padx=5)

selected_table = tk.StringVar()

tree = ttk.Treeview(tk_root, columns=("QR-код",), show="headings")
tree.heading("QR-код", text="QR-код")
tree.pack(expand=True, fill=tk.BOTH)

tk_root.mainloop()
