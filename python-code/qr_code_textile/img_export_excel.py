import os
import cv2
import numpy as np
from openpyxl import load_workbook
from PIL import Image
from io import BytesIO

save_dir = "QR_codes"
os.makedirs(save_dir, exist_ok=True)

def is_qr_code(image):
    # Преобразуем изображение в массив numpy
    img_array = np.array(image.convert("L"))  # Переводим в градации серого
    detector = cv2.QRCodeDetector()
    data, _, _ = detector.detectAndDecode(img_array)
    return bool(data)  # Если data не пустое — это QR-код


def extract_images_from_excel(excel_file_path, output_folder):
    # Load the Excel workbook
    wb = load_workbook(excel_file_path, data_only=True)
    ws = wb.active
    if hasattr(ws, '_images') and ws._images:
        qr_count = 0
        for idx, image in enumerate(ws._images):
            img_data = image._data()  # Получаем бинарные данные
            img = Image.open(BytesIO(img_data))  # Открываем как изображение
            if img.mode == "CMYK":
                img = img.convert("RGB")
            if is_qr_code(img):
                qr_count += 1
                save_path = os.path.join(save_dir, f"qr_code_{qr_count}.png")  # Путь к файлу
                img.save(save_path)  # Сохраняем в новую папку
                print(f"Saved - {qr_count}")
    else:
        print("Изображения не найдены.")

    # for sheet_name in workbook.sheetnames:
    #     sheet = workbook[sheet_name]
    #     print(sheet._drawing)
    #     # Iterate over all drawings in the sheet
    #     for drawing_id, drawing in enumerate(sheet._drawing, start=1):
    #         if isinstance(drawing, openpyxl.drawing.image.Image):
    #             # Extract the image data
    #             image_data = drawing.image

    #             # Save the image to the output folder
    #             image_filename = f"{sheet_name}_image_{drawing_id}.png"
    #             image_path = f"{output_folder}/{image_filename}"
    #             image_data.save(image_path)

    #             print(f"Image extracted: {image_path}")

# Example usage
excel_file_path = 'qr_code_textile/data.xlsx'
output_folder = 'output_images'
extract_images_from_excel(excel_file_path, output_folder)