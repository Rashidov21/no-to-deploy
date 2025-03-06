import os
import unidecode
import tkinter as tk
from tkinter import filedialog, ttk, messagebox
from PIL import Image, ImageTk
from database import get_qr_codes, delete_table,connect_db
from excel_import import extract_images_from_excel
from qr_scanner import scan_qr


def import_excel():
    file_paths = filedialog.askopenfilenames(filetypes=[["Excel Files", "*.xlsx"]])
    if not file_paths:
        return
    for file_path in file_paths:
        table_name = os.path.splitext(os.path.basename(file_path))[0]
        table_name = unidecode.unidecode(table_name.replace(" ", "_"))
        cursor = connect_db().cursor()
        # Проверяем, есть ли такая таблица в базе
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?", (table_name,))
        if cursor.fetchone():
            messagebox.showwarning("Предупреждение", f"Файл {file_path} уже был импортирован!")
            continue  # Пропускаем этот файл
        extract_images_from_excel(file_path)
        add_tab(os.path.splitext(os.path.basename(file_path))[0])

def update_table(table_name):
    """Обновление таблицы и счетчиков"""
    tree.delete(*tree.get_children())
    qr_codes = get_qr_codes(table_name)
    for row in qr_codes:
        tree.insert("", "end", values=row)
    
    imported_count.set(f"Импортировано QR-кодов: {len(qr_codes)}")
    remaining_count.set(f"Осталось QR-кодов: {len(qr_codes)}")


def add_tab(table_name):
    """Добавление новой вкладки"""
    tab = ttk.Frame(tab_control)
    tab_control.add(tab, text=table_name)
    tab_control.pack(expand=True, fill=tk.BOTH)
    tab_control.select(tab)
    selected_table.set(table_name)
    update_table(table_name)

def remove_selected_table():
    """Удаление выбранной таблицы"""
    table_name = selected_table.get()
    if table_name:
        delete_table(table_name)
        for tab in tab_control.tabs():
            if tab_control.tab(tab, "text") == table_name:
                tab_control.forget(tab)
                break
        messagebox.showinfo("Удалено", f"Таблица {table_name} удалена")
        selected_table.set("")
        update_table("")

def on_tab_change(event):
    """Обработчик смены вкладки"""
    selected_tab = tab_control.tab(tab_control.select(), "text")
    selected_table.set(selected_tab)
    update_table(selected_tab)




tk_root = tk.Tk()
tk_root.title("QR Code Manager")
tk_root.geometry("800x600")

icon_path = "icon.ico"  
icon_image = Image.open(icon_path)
icon_photo = ImageTk.PhotoImage(icon_image)
tk_root.iconphoto(False, icon_photo)


selected_table = tk.StringVar()
# Панель управления
control_frame = tk.Frame(tk_root)
control_frame.pack(side=tk.TOP, fill=tk.X,anchor='n', pady=1)

# Кнопки
btn_scan = tk.Button(
    control_frame, 
    text="📷 Сканировать QR", 
    command=lambda: scan_qr(selected_table.get(), lambda: update_table(selected_table.get())),
    bg="#292929",          
    fg="#ffffff",
    font=("Arial", 12, "bold"), 
    relief="flat",
    justify="center", 
    cursor="hand2", 
    padx=3,            
    pady=1 
    )
btn_scan.pack(side=tk.LEFT, padx=5)

btn_import = tk.Button(
    control_frame, 
    text="📂 Импорт Excel", 
    command=import_excel,
    bg="#292985",          
    fg="#ffffff",
    font=("Arial", 12, "bold"), 
    relief="flat",
    justify="center", 
    cursor="hand2", 
    padx=3,            
    pady=1 )
btn_import.pack(side=tk.LEFT, padx=5)

btn_delete = tk.Button(
    control_frame, 
    text="❌ Удалить таблицу", 
    command=remove_selected_table,
        bg="#862929",          
    fg="#ffffff",
    font=("Arial", 12, "bold"), 
    relief="flat",
    justify="center", 
    cursor="hand2", 
    padx=3,            
    pady=1)
btn_delete.pack(side=tk.LEFT, padx=5)
count_frame = tk.Frame(control_frame)
count_frame.pack(side=tk.LEFT, padx=10)
# Счетчики
imported_count = tk.StringVar(value="Импортировано QR-кодов: 0")
remaining_count = tk.StringVar(value="Осталось QR-кодов: 0")

label_imported = tk.Label(
    count_frame, 
    textvariable=imported_count,
    font=("Arial", 10, "bold"),
    fg="#292929")
label_imported.grid(row=0, column=0, sticky="w")


label_remaining = tk.Label(
    count_frame, 
    textvariable=remaining_count,
    font=("Arial", 10, "bold"),
    fg="#292929")
label_remaining.grid(row=1, column=0, sticky="w")


# Вкладки таблиц
tab_control = ttk.Notebook(tk_root)
tab_control.pack(expand=True, fill=tk.BOTH,side=tk.TOP, padx=10, pady=10)
tab_control.bind("<<NotebookTabChanged>>", on_tab_change)

# Таблица QR-кодов
tree = ttk.Treeview(tk_root, columns=("Дата экспорта", "QR-код", "Номер"), show="headings")
tree.heading("Дата экспорта", text="Дата экспорта")
tree.heading("QR-код", text="QR-код")
tree.heading("Номер", text="Номер")
tree.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

tk_root.mainloop()
