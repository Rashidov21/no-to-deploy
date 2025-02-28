import os
import pandas as pd
import qrcode
from PIL import Image
import sqlite3
from tkinter import Tk, Button, filedialog, messagebox, Label, Frame, ttk, Text, Scrollbar, END
from tkinter import simpledialog

# Ma'lumotlar bazasini yaratish
def create_database():
    conn = sqlite3.connect('products.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS products
                 (id INTEGER PRIMARY KEY, table_name TEXT, qr_code TEXT, size TEXT, arrival_time TEXT)''')
    conn.commit()
    conn.close()

# Excel faylini yuklash va ma'lumotlarni qayta ishlash
def import_excel():
    file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx")])
    if file_path:
        table_name = simpledialog.askstring("Jadval nomi", "Iltimos, jadval uchun nom kiriting:")
        if table_name:
            df = pd.read_excel(file_path)
            for index, row in df.iterrows():
                qr_code = row['QR Code']
                size = row['Size']
                arrival_time = row['Arrival Time']
                save_qr_code(qr_code, size, arrival_time)
                save_to_database(table_name, qr_code, size, arrival_time)
            messagebox.showinfo("Success", f"{table_name} jadvali muvaffaqiyatli yuklandi!")
            update_table_list()
            show_table_data(table_name)

# QR kodni generatsiya qilish va saqlash
def save_qr_code(qr_code, size, arrival_time):
    img = qrcode.make(qr_code)
    folder_path = os.path.join("QR_Codes", size, arrival_time)
    os.makedirs(folder_path, exist_ok=True)
    img.save(os.path.join(folder_path, f"{qr_code}.png"))

# Ma'lumotlarni bazaga saqlash
def save_to_database(table_name, qr_code, size, arrival_time):
    conn = sqlite3.connect('products.db')
    c = conn.cursor()
    c.execute("INSERT INTO products (table_name, qr_code, size, arrival_time) VALUES (?, ?, ?, ?)",
              (table_name, qr_code, size, arrival_time))
    conn.commit()
    conn.close()

# QR kodni o'qish va bazadan o'chirish
def read_qr_code():
    qr_code = simpledialog.askstring("QR Kodni kiriting", "Iltimos, QR kodni kiriting:")
    if qr_code:
        conn = sqlite3.connect('products.db')
        c = conn.cursor()
        c.execute("DELETE FROM products WHERE qr_code=?", (qr_code,))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", f"QR kod {qr_code} muvaffaqiyatli o'chirildi!")
        update_active_table()

# Jadval ma'lumotlarini ko'rsatish
def show_table_data(table_name):
    conn = sqlite3.connect('products.db')
    c = conn.cursor()
    c.execute("SELECT qr_code, size, arrival_time FROM products WHERE table_name=?", (table_name,))
    rows = c.fetchall()
    conn.close()

    for row in tree.get_children():
        tree.delete(row)
    for row in rows:
        tree.insert("", END, values=row)

    update_count_label(table_name)

# Jadval ro'yxatini yangilash
def update_table_list():
    conn = sqlite3.connect('products.db')
    c = conn.cursor()
    c.execute("SELECT DISTINCT table_name FROM products")
    tables = c.fetchall()
    conn.close()

    for tab in notebook.tabs():
        notebook.forget(tab)

    for table in tables:
        table_name = table[0]
        frame = Frame(notebook)
        notebook.add(frame, text=table_name)
        show_table_data(table_name)

# Aktiv jadvaldagi QR kodlar sonini yangilash
def update_count_label(table_name):
    conn = sqlite3.connect('products.db')
    c = conn.cursor()
    c.execute("SELECT COUNT(*) FROM products WHERE table_name=?", (table_name,))
    count = c.fetchone()[0]
    conn.close()
    count_label.config(text=f"{table_name} jadvalida {count} ta QR kod qolgan.")

# Jadvalni o'chirish
def delete_table():
    table_name = notebook.tab(notebook.select(), "text")
    if table_name:
        conn = sqlite3.connect('products.db')
        c = conn.cursor()
        c.execute("DELETE FROM products WHERE table_name=?", (table_name,))
        conn.commit()
        conn.close()
        update_table_list()
        messagebox.showinfo("Success", f"{table_name} jadvali muvaffaqiyatli o'chirildi!")

# GUI yaratish
def create_gui():
    global notebook, tree, count_label

    root = Tk()
    root.title("Trikotaj Mahsulotlari Boshqaruvi")

    # Jadval ro'yxati uchun notebook
    notebook = ttk.Notebook(root)
    notebook.pack(fill="both", expand=True)

    # QR kodlar jadvali
    columns = ("QR Code", "Size", "Arrival Time")
    tree = ttk.Treeview(notebook, columns=columns, show="headings")
    for col in columns:
        tree.heading(col, text=col)
    tree.pack(fill="both", expand=True)

    # QR kodlar soni
    count_label = Label(root, text="", font=("Arial", 12))
    count_label.pack(pady=10)

    # Tugmalar
    Button(root, text="Excel Faylini Yuklash", command=import_excel).pack(side="left", padx=10, pady=10)
    Button(root, text="QR Kodni O'qish", command=read_qr_code).pack(side="left", padx=10, pady=10)
    Button(root, text="Jadvalni O'chirish", command=delete_table).pack(side="right", padx=10, pady=10)

    root.mainloop()

if __name__ == "__main__":
    create_database()
    create_gui()