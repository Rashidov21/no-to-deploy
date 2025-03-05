# В этом примере кода показано, как читать QR-код в Python.
import aspose.barcode as barcode

# Загрузить изображение QR-кода
reader = barcode.barcoderecognition.BarCodeReader("QR_codes/qr_code_1.png")

# Чтение QR-кодов
recognized_results = reader.read_bar_codes()

# Показать результаты
for x in recognized_results:
    # print("Code Text: " + x.code_text)
    # print("Type: " + x.code_type_name)
    print(type(x.code_text))
    print(x.code_bytes)
