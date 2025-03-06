import cv2
from pyzbar.pyzbar import decode
from database import delete_qr_code, get_qr_codes
import tkinter.messagebox as messagebox

def scan_qr(selected_table, update_callback):
    """ Запускает камеру и сканирует QR-коды """
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        decoded_objects = decode(frame)
        for obj in decoded_objects:
            qr_code = obj.data.decode("utf-8")
            records = get_qr_codes(selected_table)

            for record in records:
                qr_code_path = record[1]
                if qr_code in qr_code_path:  
                    delete_qr_code(selected_table, qr_code_path)
                    update_callback()
                    messagebox.showinfo("QR-код найден", f"Удалён QR-код: {qr_code}")
                    break  

        cv2.imshow("QR Scanner", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
