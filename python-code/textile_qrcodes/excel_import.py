import os
import datetime
import unidecode
from openpyxl import load_workbook
from PIL import Image
from io import BytesIO
import tkinter as tk

from slugify import slugify

from database import create_table, insert_qr_code,set_total_qr_codes





def extract_images_from_excel(file_path,tk_root):
    """ Извлекает QR-коды из Excel и сохраняет их в базу данных """
    tk_root.update_idletasks()  # Обновляем интерфейс
    wb = load_workbook(file_path, data_only=True)
    ws = wb.active
    file_name = os.path.splitext(os.path.basename(file_path))[0]
    table_name = unidecode.unidecode(file_name.replace(" ", "_"))
    table_name = slugify(table_name).replace("-", "_")
    
    folder_name = f"qr_codes_{unidecode.unidecode(table_name)}"
    save_dir = os.path.join(os.getcwd(), folder_name)
    os.makedirs(save_dir, exist_ok=True)

    # Check table name 

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
                export_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                insert_qr_code(table_name, export_date, save_path, qr_count)
                set_total_qr_codes(table_name, qr_count)
                img.save(save_path)
                
                
    
    wb.close()

    
   


