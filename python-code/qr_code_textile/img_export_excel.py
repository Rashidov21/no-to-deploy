from openpyxl import load_workbook

def extract_images_from_excel(excel_file_path, output_folder):
    # Load the Excel workbook
    workbook = load_workbook(excel_file_path, data_only=True)

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