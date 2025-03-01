import os
import cv2
import numpy as np
from openpyxl import load_workbook
from PIL import Image
from io import BytesIO

save_dir = "QR_codes"
os.makedirs(save_dir, exist_ok=True)

def is_qr_code(image):
    img_array = np.array(image.convert("L")) 
    detector = cv2.QRCodeDetector()
    data, _, _ = detector.detectAndDecode(img_array)
    return bool(data)  # QR code out


def extract_images_from_excel(excel_file_path, output_folder):
    wb = load_workbook(excel_file_path, data_only=True)
    ws = wb.active
    if hasattr(ws, '_images') and ws._images:
        qr_count = 0
        for idx, image in enumerate(ws._images):
            img_data = image._data()  
            img = Image.open(BytesIO(img_data))  
            if img.mode == "CMYK":
                img = img.convert("RGB")
            if is_qr_code(img):
                qr_count += 1
                save_path = os.path.join(save_dir, f"qr_code_{qr_count}.png")  # Путь к файлу
                img.save(save_path)  # Save image
                print(f"Saved - {qr_count}")
    else:
        print("Изображения не найдены.")

    wb.close()

# Example usage
excel_file_path = 'qr_code_textile/data.xlsx'
output_folder = 'output_images'
extract_images_from_excel(excel_file_path, output_folder)