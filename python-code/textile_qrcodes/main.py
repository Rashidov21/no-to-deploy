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

def update_table(table_name,tree):
    """Обновление таблицы и счетчиков"""
    tree.delete(*tree.get_children())  # Очистка старых данных

    conn = connect_db()
    cursor = conn.cursor()
    data = cursor.execute(f"SELECT export_date, qr_code_path, qr_number FROM {table_name}")
    qr_codes = data.fetchall()
    conn.close()

    for row in qr_codes:
        tree.insert("", "end", values=row)


def add_tab(table_name):
    """Добавляет новую вкладку с таблицей QR-кодов"""
    style = ttk.Style()
    style.configure("TNotebook.Tab", 
                font=("Arial", 10, "bold"),  # Шрифт вкладок
                padding=[10, 5],  # Отступы внутри вкладки
                background="#D3D3D3",  # Цвет фона вкладки
                foreground="black",  # Цвет текста вкладки
                borderwidth=2,
                case="uppercase")  # Граница вкладок

    style.map("TNotebook.Tab", background=[("selected", "#4CAF50")])
    
    tab = ttk.Frame(tab_control)
    tab_control.add(tab, text=table_name)
    tab_control.pack(expand=True, fill=tk.BOTH)
    tab_control.select(tab)
    selected_table.set(table_name)

    # Создаем фрейм для таблицы и скроллбаров
    tab_frame = ttk.Frame(tab)
    tab_frame.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

    # Создаем Treeview
    style = ttk.Style()
    style.configure("Treeview.Heading", font=("Arial", 10, "bold"), background="lightgray", foreground="black", relief="raised", padding=(5, 5))
    style.configure("Treeview", rowheight=25)
    style.map("Treeview", background=[("selected", "#347083")])
    
    
    style = ttk.Style()

    # Общий стиль таблицы
    style.configure("Treeview", 
                    font=("Arial", 10),  # Шрифт строк
                    rowheight=25,         # Высота строк
                    background="white", 
                    foreground="black", 
                    fieldbackground="white",
                    borderwidth=1)

    style.map("Treeview",
          background=[("alternate", "#f2f2f2")])

    # Выделенная строка
    style.map("Treeview",background=[("alternate", "#232323")])
    style.map("Treeview",
            background=[("hover", "#0078D7")],
          foreground=[("hover", "white")])
    # Подсветка строки при наведении
    style.map("Treeview", 
            background=[("selected", "#292929")],  # Цвет выделенной строки
            foreground=[("selected", "#ffffff")])  # Цвет текста в выделенной строке
    tree = ttk.Treeview(tab_frame, columns=("Дата экспорта", "QR-код", "Номер"), show="headings", selectmode="browse")


    # Заголовки
    tree.heading("Дата экспорта", text="Дата экспорта")
    tree.heading("QR-код", text="QR-код")
    tree.heading("Номер", text="Номер")
    # Настройка колонок (центрирование)
    tree.column("Дата экспорта", anchor="center", width=150)
    tree.column("QR-код", anchor="center", width=200)
    tree.column("Номер", anchor="center", width=100)

    # **Добавляем вертикальный скроллбар**
    vsb = ttk.Scrollbar(
        tab_frame, 
        orient="vertical", 
        command=tree.yview,
        cursor="hand2")
    tree.configure(yscrollcommand=vsb.set)

    # **Добавляем горизонтальный скроллбар**
    hsb = ttk.Scrollbar(tab_frame, orient="horizontal", command=tree.xview,cursor="hand2")
    tree.configure(xscrollcommand=hsb.set)

    # Размещаем виджеты в фрейме
    tree.grid(row=0, column=0, sticky="nsew")
    vsb.grid(row=0, column=1, sticky="ns")  # Вертикальный скроллбар справа
    hsb.grid(row=1, column=0, sticky="ew")  # Горизонтальный скроллбар снизу

    # Устанавливаем, чтобы Treeview растягивался при изменении размера вкладки
    tab_frame.columnconfigure(0, weight=1)
    tab_frame.rowconfigure(0, weight=1)

    # **Сохраняем Treeview в словаре**
    tree_views[table_name] = tree

    # Загружаем данные в таблицу
    update_table(table_name, tree)


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
tree_views = {}
def on_tab_change(event):
    """Вызывается при переключении вкладки. Загружает данные из выбранной таблицы."""
    selected_tab = tab_control.tab(tab_control.select(), "text")
    print(selected_tab)
    selected_table.set(selected_tab)

    # Получаем Treeview из активной вкладки
    if selected_tab in tree_views:
        tree = tree_views[selected_tab]  # Получаем Treeview для текущей вкладки
        update_table(selected_tab, tree)

    tab_control.bind("<<NotebookTabChanged>>", on_tab_change)


def load_existing_tables():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    
    for table in tables:
      
        table_name = table[0]
        if table_name != "sqlite_sequence":  # Исключаем системную таблицу
            add_tab(table_name)


 

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



# tab_frame = tk.Frame(tk_root, height=200)  # Устанавливаем фиксированную высоту
# tab_frame.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)

# style = ttk.Style()
# style.configure("TNotebook.Tab", 
#                 font=("Arial", 10, "bold"),  # Шрифт вкладок
#                 padding=[10, 5],  # Отступы внутри вкладки
#                 background="#D3D3D3",  # Цвет фона вкладки
#                 foreground="black",  # Цвет текста вкладки
#                 borderwidth=2)  # Граница вкладок

# style.map("TNotebook.Tab", background=[("selected", "#4CAF50")])
# Вкладки таблиц    
tab_control = ttk.Notebook(tk_root, style="TNotebook")
tab_control.pack(expand=True, fill=tk.BOTH,side=tk.TOP,padx=10,pady=10)
tab_control.bind("<<NotebookTabChanged>>", on_tab_change)


# Загрузка существующих таблиц
load_existing_tables()

tk_root.mainloop()
