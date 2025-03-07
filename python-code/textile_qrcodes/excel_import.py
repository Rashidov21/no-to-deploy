import os
import datetime
import unidecode
from openpyxl import load_workbook
from PIL import Image
from io import BytesIO
import tkinter as tk
from tkinter import ttk,messagebox
from database import create_table, insert_qr_code


def show_loading_window(tk_root):
    """Создает окно загрузки"""
    loading_window = tk.Toplevel(tk_root)
    loading_window.title("Загрузка...")
    loading_window.geometry("300x100")  # Размер окна
    loading_window.resizable(False, False)  # Запрещаем изменение размеров

    # Размещаем окно по центру экрана
    x = tk_root.winfo_x() + (tk_root.winfo_width() // 2) - 150
    y = tk_root.winfo_y() + (tk_root.winfo_height() // 2) - 50
    loading_window.geometry(f"+{x}+{y}")

    label = ttk.Label(loading_window, text="⏳ Идет экспорт, подождите...", font=("Arial", 12, "bold"))
    label.pack(expand=True)

    loading_window.grab_set()  # Блокируем основное окно
    tk_root.update_idletasks()


def extract_images_from_excel(file_path,tk_root):

    loading_window = show_loading_window(tk_root)
    
    """ Извлекает QR-коды из Excel и сохраняет их в базу данных """
    
    # loading_label = ttk.Label(tk_root, text="⏳ Идет экспорт, пожалуйста, подождите...", font=("Arial", 12, "bold"))
    # loading_label.pack(pady=10)
    tk_root.update_idletasks()  # Обновляем интерфейс
    wb = load_workbook(file_path, data_only=True)
    ws = wb.active
    file_name = os.path.splitext(os.path.basename(file_path))[0]
    
    folder_name = f"qr_codes_{unidecode.unidecode(file_name)}"
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
                insert_qr_code(table_name, export_date, save_path, qr_count)
    
    wb.close()

    loading_window.destroy()  # Закрываем окно загрузки
    tk_root.config(cursor="")  # Возвращаем обычный курсор
    tk_root.update_idletasks()
    messagebox.showinfo("Экспорт завершен", "QR-коды успешно экспортированы!")


