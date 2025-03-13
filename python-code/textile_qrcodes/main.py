import uuid
import os
import re
import shutil
import cv2
import socket
import sys
import unidecode
import zxingcpp
import tkinter as tk
from tkinter import filedialog, ttk, messagebox
from PIL import Image, ImageTk
import dotenv
from slugify import slugify
from database import delete_qr_code, get_qr_codes
from database import get_qr_codes, delete_table,connect_db,get_total_qr_codes,get_all_tables
from excel_import import extract_images_from_excel
from check_pc_id import get_windows_uuid


tk_root = tk.Tk()
tk_root.title("QR Code Manager")
tk_root.geometry("1000x600")
icon_path = "icon.ico"  
icon_image = Image.open(icon_path)
icon_photo = ImageTk.PhotoImage(icon_image)
tk_root.wm_iconphoto(True, icon_photo)
tk_root.call("wm","iconphoto", tk_root, icon_photo)


# Панель управления
control_frame = tk.Frame(tk_root)
control_frame.pack(side=tk.TOP, fill=tk.X,anchor='n', pady=1)

tree_views = {}
 
selected_table = tk.StringVar()
# Счетчики
imported_count = tk.StringVar(value="Импортировано QR-кодов: 0")
remaining_count = tk.StringVar(value="Осталось QR-кодов: 0")


def update_qr_counts(table_name):
    """Обновляет количество импортированных и оставшихся QR-кодов"""
    records = get_qr_codes(table_name)  # Получаем список QR-кодов из базы
    total_qr = get_total_qr_codes(table_name)  # Количество QR-кодов в таблице
    imported_count.set(f"Импортировано QR-кодов: {total_qr}")
    remaining_count.set(f"Осталось QR-кодов: {len(records)}")


def show_loading_window(tk_root):
    """Создает окно загрузки"""
    loading_window = tk.Toplevel(tk_root)
    loading_window.title("Загрузка...")
    loading_window.geometry("300x100")  # Размер окна
    loading_window.resizable(False, False)  # Запрещаем изменение размеров
    icon_path = "icon.ico"  
    icon_image = Image.open(icon_path)
    icon_photo = ImageTk.PhotoImage(icon_image)
    loading_window.iconphoto(False, icon_photo)
    # Размещаем окно по центру экрана
    x = tk_root.winfo_x() + (tk_root.winfo_width() // 2) - 150
    y = tk_root.winfo_y() + (tk_root.winfo_height() // 2) - 50
    loading_window.geometry(f"+{x}+{y}")
    label = ttk.Label(loading_window, text="⏳ Идет экспорт, подождите...", font=("Arial", 12, "bold"))
    label.pack(expand=True)

    loading_window.grab_set()  # Блокируем основное окно
    tk_root.update_idletasks()


def close_all_toplevels():
    for window in tk_root.winfo_children():  # Перебираем все окна
        if isinstance(window, tk.Toplevel):  # Проверяем, является ли оно Toplevel
            window.destroy()


def import_excel():
    file_paths = filedialog.askopenfilenames(filetypes=[["Excel Files", "*.xlsx"]])
    if not file_paths:
        return
    for file_path in file_paths:
        table_name = os.path.splitext(os.path.basename(file_path))[0]
        table_name = unidecode.unidecode(table_name.replace(" ", "_"))
        table_name = slugify(table_name).replace("-", "_")
        cursor = connect_db().cursor()
        # Проверяем, есть ли такая таблица в базе
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?", (table_name,))
        if cursor.fetchone():
            messagebox.showwarning("Предупреждение", f"Файл {file_path} уже был импортирован!")
            continue  # Пропускаем этот файл
        show_loading_window(tk_root)
        extract_images_from_excel(file_path,tk_root)
        close_all_toplevels()
        tk_root.update_idletasks()
        messagebox.showinfo("Экспорт завершен", "QR-коды успешно экспортированы!")
        add_tab(table_name)

def update_table(table_name,tree):
    """Обновление таблицы и счетчиков"""
    tree.delete(*tree.get_children())  # Очистка старых данных
    conn = connect_db()
    cursor = conn.cursor()
    data = cursor.execute(f"SELECT qr_number, export_date, qr_code_path  FROM {table_name}")
    qr_codes = data.fetchall()
    for row in qr_codes:
        row = [row[0],row[1],"/".join(row[2].split("\\")[-2:])]
        tree.insert("", "end", values=row)
     # Обновляем счётчики
    update_qr_counts(table_name)
    conn.close()

# Notebook (Вкладки) внутри `tabs_frame`
tab_control = ttk.Notebook(tk_root)
tab_control.pack(fill=tk.X, expand=False)
style = ttk.Style()
style.layout("TNotebook.Tab", [])
tab_control.configure(style="TNotebook")
def add_tab(table_name):
    """Добавляет новую вкладку с таблицей QR-кодов""" 
    style = ttk.Style()
    style.configure("TNotebook.Tab", 
                font=("Arial", 11, "bold"),  # Шрифт вкладок
                padding=[10, 5],  # Отступы внутри вкладки
                background="white",  # Цвет фона вкладки
                foreground="black",  # Цвет текста вкладки
                borderwidth=2,
                case="uppercase")  # Граница вкладок

    style.map("TNotebook.Tab", background=[("selected", "#292929")])
    tab = ttk.Frame(tab_control)
    tab_control.add(tab, text=table_name)
    tab_control.pack(expand=True, fill=tk.BOTH)
    tab_control.select(tab)
    selected_table.set(table_name)
    # Создаем фрейм для таблицы и скроллбаров
    tab_frame = ttk.Frame(tab)
    tab_frame.pack(expand=True, fill=tk.BOTH, padx=10, pady=0)
    # Создаем Treeview

    style.configure("Treeview.Heading", font=("Arial", 10, "bold"), background="lightgray", foreground="black", relief="raised", padding=(5, 5))
    style.configure("Treeview", rowheight=25)
    style.map("Treeview", background=[("selected", "#347083")])
    # Общий стиль таблицы
    style.configure("Treeview", 
                    font=("Arial", 10),  # Шрифт строк
                    rowheight=25,         # Высота строк
                    background="white", 
                    foreground="black", 
                    fieldbackground="white",
                    borderwidth=2)
    # Подсветка строки при наведении
    style.map("Treeview", 
            background=[("selected", "#292929")],  # Цвет выделенной строки
            foreground=[("selected", "#ffffff")])  # Цвет текста в выделенной строке
    tree = ttk.Treeview(tab_frame, columns=("Номер","Дата экспорта", "QR-код"), show="headings")
    # Заголовки
    tree.heading("Номер", text="Номер")
    tree.heading("Дата экспорта", text="Дата экспорта")
    tree.heading("QR-код", text="QR-код")
    # Настройка колонок (центрирование)
    tree.column("Номер", anchor="center", width=100)
    tree.column("Дата экспорта", anchor="center", width=100)
    tree.column("QR-код", anchor="center", width=300)
    
    style.configure("Treeview.Heading", font=("Arial", 12, "bold"), background="#292929", foreground="black")
    # **Добавляем вертикальный скроллбар**
    vsb = ttk.Scrollbar(
        tab_frame, 
        orient="vertical", 
        command=tree.yview,
        cursor="hand2")
    tree.configure(yscrollcommand=vsb.set)
    # Размещаем виджеты в фрейме
    tree.grid(row=0, column=0, sticky="nsew")
    vsb.grid(row=0, column=1, sticky="ns")  # Вертикальный скроллбар справа
    # Устанавливаем, чтобы Treeview растягивался при изменении размера вкладки
    tab_frame.columnconfigure(0, weight=1)
    tab_frame.rowconfigure(0, weight=1)
    # **Сохраняем Treeview в словаре**
    tree_views[table_name] = tree
    # Загружаем данные в таблицу
    update_table(table_name, tree)


def select_last_tab():
    tab_count = len(tab_control.tabs())  # Получаем список всех вкладок
    if tab_count > 0:
        tab_control.select(tab_count - 1)

def remove_selected_table():
    """Удаление выбранной таблицы"""
    selected_table_name = selected_table.get().strip()
    selected_tab_id = tab_control.select()
    selected_table_name = tab_control.tab(selected_tab_id, "text")  # Имя таблицы

    if not selected_table_name:
        return  
    if selected_table_name not in tree_views:
        return  
    tree = tree_views[selected_table_name]  # Получаем дерево для этой таблицы
    # Обновляем данные в таблице

    if not selected_table_name:
        messagebox.showwarning("Ошибка", "Не выбрана таблица для удаления")
        return  

    if selected_table_name not in tree_views:
        messagebox.showwarning("Ошибка", f"Таблица '{selected_table_name}' не найдена")
        return  

    tree = tree_views[selected_table_name] 
    confirm = messagebox.askyesno("Подтверждение", f"Вы уверены, что хотите удалить таблицу '{selected_table_name}'?")
    if selected_table_name and confirm:
        delete_table(selected_table_name)
        for tab in tab_control.tabs():
            if tab_control.tab(tab, "text") == selected_table_name:
                tab_control.forget(tab)
                break
        else:
            selected_table.set("")  # Сбрасываем выбранную таблицу
            tree.delete(*tree.get_children())  # Очищаем таблицу
            messagebox.showinfo("Внимание", "Все таблицы удалены!")
            not_data_frame = ttk.Frame(tab_control)
            not_data_frame.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)
            label = ttk.Label(not_data_frame, text="❌ Таблицы не найдены", font=("Arial", 12, "bold"))
            label.pack(expand=True)
            
        folder_name = f"qr_codes_{selected_table_name}"
        folder_path = os.path.join(os.getcwd(), folder_name)
         # Удаление папки с файлами QR-кодов
        if os.path.exists(folder_path):
            shutil.rmtree(folder_path)  # Удаляет папку и все её файлы

        messagebox.showinfo("Удалено", f"Таблица '{selected_table_name}' и её папка удалены.")
        selected_tab = tab_control.tab(tab_control.select(), "text")
        selected_table.set(selected_tab)
  

def on_tab_select(event):
    """ Обработчик переключения вкладок """
    selected_table_name = selected_table.get().strip()
    selected_tab_id = tab_control.select()
    selected_table_name = tab_control.tab(selected_tab_id, "text")  # Имя таблицы

    if not selected_table_name:
        return  
    if selected_table_name not in tree_views:
        return  
    tree = tree_views[selected_table_name]  # Получаем дерево для этой таблицы
    # Обновляем данные в таблице
    update_table(selected_table_name, tree)
 

def on_tab_change(event):
    """Вызывается при переключении вкладки. Загружает данные из выбранной таблицы."""
    selected_tab = tab_control.tab(tab_control.select(), "text")
    selected_table.set(selected_tab)

    # Получаем Treeview из активной вкладки
    if selected_tab in tree_views:
        tree = tree_views[selected_tab]  # Получаем Treeview для текущей вкладки
        update_table(selected_tab, tree)

    tab_control.bind("<<NotebookTabChanged>>", on_tab_change)


def load_existing_tables():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name != 'sqlite_sequence';")
    tables = cursor.fetchall()
    conn.close()
    if not tables:
        messagebox.showwarning("Предупреждение", "Таблицы не найдены!")
    else:
        for table in tables:
            table_name = table[0]
            add_tab(table_name)



# 🔹 Верхний фрейм (для вкладок и кнопок)
buttons_frame = ttk.Frame(tk_root,width=tk_root.winfo_width())
buttons_frame.pack(side=tk.TOP, fill=tk.X)

# 🔹 Canvas (чтобы делать прокрутку вкладок)
canvas = tk.Canvas(buttons_frame, height=30)
canvas.pack(fill=tk.X, expand=True, pady=0)

# Фрейм внутри Canvas (держит вкладки)
button_list_frame = ttk.Frame(canvas)
canvas.create_window((0, 0), window=button_list_frame,anchor="center")

for name in get_all_tables():
    btn = tk.Button(
        button_list_frame,
        relief="flat",
        cursor="hand2", 
        text=name[0], 
        command=lambda n=name[0]: switch_tab(n),
        font=("Arial", 10, "bold"),
        bg="white",
        fg="#292929",
        padx=5,
        pady=5,
        anchor="center"
    )
    btn.pack(side="left", fill=tk.X, padx=5)

# Функция переключения вкладки
def switch_tab(tab_name):
    tabs = tab_control.tabs()
    for tab in tabs:
        if tab_control.tab(tab, "text") == tab_name:
            tab_control.select(tab)

# Функция прокрутки кнопок
def scroll_canvas(delta):
    canvas.xview_scroll(delta, "units")

def update_scroll_region(event=None):
    """Обновляет область прокрутки"""
    canvas.configure(scrollregion=canvas.bbox("all"))
    
def on_mouse_wheel(event):
    """Прокрутка вкладок колесиком мыши"""
    if event.delta > 0:
        canvas.xview_scroll(-2, "units")  # Прокрутка влево
    else:
        canvas.xview_scroll(2, "units")  # Прокрутка вправо
canvas.bind("<Configure>", update_scroll_region)
canvas.bind_all("<MouseWheel>", on_mouse_wheel)

tk_root.after(100, update_scroll_region)
canvas.bind("<Shift-MouseWheel>", lambda event: scroll_canvas(-1 if event.delta > 0 else 1))



def decode_with_zxing(image_path):
    """Попытка распознавания QR-кода через ZXing"""
    if not os.path.exists(image_path):
        return None

    image = cv2.imread(image_path)
    if image is None:
        return None
    
    result = zxingcpp.read_barcodes(image)

    if result:
        for barcode in result:
            decoded_qr_clean = barcode.bytes.decode("utf-8").strip()
            return decoded_qr_clean
    return None


def clean_qr_data(qr_code):
    """Очищает текст QR-кода от лишних символов"""
    return re.sub(r"[\x00-\x1F\x7F]", "", qr_code).strip()

def check_qr_in_folder(table_name, scanned_qr):
    """Проверяет, есть ли отсканированный QR-код в папке с изображениями"""
    records = get_qr_codes(table_name)  # Получаем пути к изображениям из БД
    
    for record in records:
        qr_code_path = record[1]  # Путь к файлу QR-кода

        if not os.path.exists(qr_code_path):  # Пропускаем, если файла нет
            # print(f"⚠️ Файл {qr_code_path} не найден, пропускаем.")
            continue
     
        decoded_qr = decode_with_zxing(qr_code_path)

        if decoded_qr is None:
            # print(f"❌ Ошибка: QR-код не распознан в {qr_code_path}")
            continue

        # Преобразуем в строку и чистим от пробелов
        scanned_qr_clean = clean_qr_data(scanned_qr)
        decoded_qr_clean = clean_qr_data(decoded_qr)
     
        if scanned_qr_clean[:20] == decoded_qr_clean[:20]:
            if scanned_qr_clean == decoded_qr_clean:
                # print("✅ Совпадение найдено! Удаляем код.")
                # Удаляем из базы
                try:
                    delete_qr_code(table_name, qr_code_path)
                except Exception as e: 
                    print(e)
                return True
            
    
    return False  # Если QR-код не найден

def on_qr_scanned(event=None):
    """Функция вызывается при сканировании QR-кода"""
    scanned_qr  = qr_entry.get().strip()  # Получаем введённый код
    qr_entry.delete(0, tk.END)  # Очищаем поле

    if not scanned_qr :
        return
    selected_tab_id = tab_control.select()
    table_name = tab_control.tab(selected_tab_id, "text")
    if check_qr_in_folder(table_name, scanned_qr):
        messagebox.showinfo("🔎 QR-код найден !", f"✅ Удалён QR-код: {scanned_qr}")
    else:
        messagebox.showerror("❌ Ошибка","🔎 QR-код не найден !")
    
    update_qr_counts(table_name)
        

def start_qr_scanner():
    qr_entry.focus_set()
    qr_entry.bind("<Return>", on_qr_scanned)


# Кнопки
btn_scan = tk.Button(
    control_frame, 
    text="📷 Сканировать QR", 
    command=start_qr_scanner,
    bg="#292929",          
    fg="#ffffff",
    font=("Arial", 12, "bold"), 
    relief="flat",
    justify="center", 
    cursor="hand2", 
    padx=3,            
    pady=1)

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

qr_label = tk.Label(control_frame, text="Введите QR-код:", font=("Arial", 10))
qr_label.pack(side=tk.TOP, pady=2)
qr_entry = tk.Entry(control_frame, font=("Arial", 10))
qr_entry.pack(side=tk.TOP, pady=10)




    
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
tab_control = ttk.Notebook(tk_root, style="TNotebook")
tab_control.pack(expand=True, fill=tk.BOTH,side=tk.TOP,padx=10,pady=10)
tab_control.bind("<<NotebookTabChanged>>", on_tab_change)
tab_control.bind("<<NotebookTabChanged>>", on_tab_select)


def show_alert_window():
    """Показывает окно предупреждения"""
    messagebox.askokcancel("❌ Доступ запрещён!","Вы не являетесь авторизованным пользователем!\nПриложение будет закрыто.")
    tk_root.quit()
com1 = "34444335-3633-3434-5453-533436334435"
com2 = "33E663D7-5963-BDEF-0A7B-3860778E2490"
me = "03000200-0400-0500-0006-000700080009"
    
if get_windows_uuid() == me:
    load_existing_tables()
    tk_root.mainloop()

else:
    show_alert_window()