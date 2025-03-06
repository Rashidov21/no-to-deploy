import os
import datetime
import unidecode
from openpyxl import load_workbook
from PIL import Image
from io import BytesIO
from database import create_table, insert_qr_code

def extract_images_from_excel(file_path):
    """ Извлекает QR-коды из Excel и сохраняет их в базу данных """
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
                insert_qr_code(table_name, export_date, save_path, qr_count)
    
    wb.close()
