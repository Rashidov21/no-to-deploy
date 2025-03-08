import tkinter as tk
from database import delete_qr_code, get_qr_codes
from tkinter import messagebox

scanned_code = ""  # Буфер для сканера
scanning_active = False  # Флаг состояния

def on_key_press(event):
    """Обрабатываем ввод сканера"""
    global scanned_code
    if event.keysym == "Return":
        process_qr_code(scanned_code.strip())  # Обрабатываем
        scanned_code = ""  # Очищаем буфер
    else:
        scanned_code += event.char  # Добавляем символ

def process_qr_code(qr_code):
    """Проверяем и удаляем QR-код"""
    if not qr_code:
        return

    records = get_qr_codes(selected_table.get())  
    for record in records:
        qr_code_path = record[1]
        if qr_code in qr_code_path:  
            delete_qr_code(selected_table.get(), qr_code_path)
            messagebox.showinfo("QR-код найден", f"Удалён QR-код: {qr_code}")
            return

    messagebox.showwarning("Ошибка", "QR-код не найден в базе!")

def toggle_scanning():
    """Включает / выключает сканирование"""
    global scanning_active
    scanning_active = not scanning_active  # Переключаем флаг
    if scanning_active:
        root.bind("<Key>", on_key_press)  # Включаем обработку
        scan_button.config(text="Остановить сканирование", bg="red")
    else:
        root.unbind("<Key>")  # Выключаем обработку
        scan_button.config(text="Сканировать", bg="green")

# Создаем окно
root = tk.Tk()
root.title("Сканер QR-кодов")

# Кнопка "Сканировать"
scan_button = tk.Button(root, text="Сканировать", font=("Arial", 12, "bold"), command=toggle_scanning, bg="green")
scan_button.pack(pady=10)

root.mainloop()
