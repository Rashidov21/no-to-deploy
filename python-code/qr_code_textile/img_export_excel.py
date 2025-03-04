import os
import cv2
import numpy as np
from openpyxl import load_workbook
from PIL import Image,ImageEnhance
from io import BytesIO

save_dir = "QR_codes"
debug_dir = "Debugs"
os.makedirs(save_dir, exist_ok=True)
os.makedirs(debug_dir, exist_ok=True)

def is_qr_code(image, idx):
    img = image.convert("L")  # Переводим в оттенки серого
    enhancer = ImageEnhance.Contrast(img)
    img = enhancer.enhance(3.0)  # Увеличиваем контрастность
    debug_path = os.path.join(debug_dir, f"debug_{idx}.png")
    # img.save(debug_path)
    # print(f"Промежуточное изображение сохранено: {debug_path}")
    img_array = np.array(img)
    detector = cv2.QRCodeDetector()
    data, bbox, _ = detector.detectAndDecode(img_array)
    # print(f"Изображение {idx}: Data = {data}, BoundingBox = {bbox}")
    
    return bool(data)  # Если data не пустое — это QR-код


def extract_images_from_excel(excel_file_path, output_folder):
    wb = load_workbook(excel_file_path, data_only=True)
    ws = wb.active
    if hasattr(ws, '_images') and ws._images:
        qr_count = 0
        for idx, image in enumerate(ws._images):
            img_data = image._data()  
            img = Image.open(BytesIO(img_data)) 
            print(img.size)
            if img.size[0] == 166:
                if img.mode == "CMYK":
                    img = img.convert("RGB")
                qr_count += 1
                save_path = os.path.join(save_dir, f"qr_code_{qr_count}.png")  # Путь к файлу
                img.save(save_path)  # Save image
                # print(f"Saved - {qr_count}")
    else:
        print("Изображения не найдены.")

    wb.close()

# Example usage
excel_file_path = 'qr_code_textile/test3.xlsx'
output_folder = 'output_images'
extract_images_from_excel(excel_file_path, output_folder)