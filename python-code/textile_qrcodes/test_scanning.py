import pyperclip
import time
import threading
import tkinter as tk
from tkinter import messagebox

scanning = False  # Флаг работы сканера

def scan_qr():
    """ Запускает отслеживание буфера обмена """
    global scanning
    scanning = True
    last_clipboard = ""
    
    while scanning:
        qr_code = pyperclip.paste().strip()
        if qr_code and qr_code != last_clipboard:
            last_clipboard = qr_code
            messagebox.showinfo("QR-код", f"Сканирован: {qr_code}")
        time.sleep(1)  # Ожидание

def start_scanning():
    """ Запускает поток для сканирования """
    global scanning
    if not scanning:
        threading.Thread(target=scan_qr, daemon=True).start()

def stop_scanning():
    """ Останавливает сканирование """
    global scanning
    scanning = False

# Интерфейс
root = tk.Tk()
root.title("QR-сканер F27")

btn_start = tk.Button(root, text="Начать сканирование", command=start_scanning)
btn_start.pack(pady=10)

btn_stop = tk.Button(root, text="Остановить", command=stop_scanning)
btn_stop.pack(pady=10)

root.mainloop()
