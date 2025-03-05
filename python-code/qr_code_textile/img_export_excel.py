import os
from openpyxl import load_workbook
from PIL import Image
from io import BytesIO

save_dir = "QR_codes"
debug_dir = "Debugs"
os.makedirs(save_dir, exist_ok=True)
os.makedirs(debug_dir, exist_ok=True)


def extract_images_from_excel(excel_file_path, output_folder):
    wb = load_workbook(excel_file_path, data_only=True)
    ws = wb.active
    image_count = 0
    if hasattr(ws, '_images') and ws._images:
        qr_count = 0
        for idx, image in enumerate(ws._images):
            image_count += 1
            img_data = image._data()  
            img = Image.open(BytesIO(img_data)) 

            if img.size[0] == 166:
                if img.mode == "CMYK":
                    img = img.convert("RGB")
                qr_count += 1
                save_path = os.path.join(save_dir, f"qr_code_{qr_count}.png")  # Путь к файлу
                img.save(save_path)  # Save image
                print(f"Saved - {qr_count}")
    else:
        print("Изображения не найдены.")

    wb.close()
    print(image_count)
# Example usage
excel_file_path = 'qr_code_textile/test6.xlsx'
output_folder = 'output_images'
extract_images_from_excel(excel_file_path, output_folder)