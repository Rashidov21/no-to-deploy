import tkinter as tk
from tkinter import ttk

# Создание главного окна
root = tk.Tk()
root.title("Переключение вкладок через прокручиваемые кнопки")
root.geometry("800x600")

# Создаём Notebook (вкладки)
tab_control = ttk.Notebook(root)
tab_control.pack(expand=True, fill="both")

# Список вкладок
tabs = {}

# Создаём 10 вкладок (для примера)
tab_names = [f"Вкладка {i+1}" for i in range(10)]

for name in tab_names:
    tab = ttk.Frame(tab_control)
    tab_control.add(tab, text=name)
    tabs[name] = tab

    # Добавляем текст в каждую вкладку для наглядности
    label = ttk.Label(tab, text=f"Содержимое {name}")
    label.pack(pady=20)

# 📌 Контейнер для кнопок (скроллируемый)
button_frame = tk.Frame(root)
button_frame.pack(fill="x", side="bottom")

# Создаём Canvas для прокрутки
canvas = tk.Canvas(button_frame, height=40, highlightthickness=0)
canvas.pack(side="left", fill="both", expand=True)

# Frame внутри Canvas для хранения кнопок
scroll_frame = tk.Frame(canvas)
canvas.create_window((0, 0), window=scroll_frame, anchor="nw")

# Функция переключения вкладки
def switch_tab(tab_name):
    tab_control.select(tabs[tab_name])

# Функция прокрутки кнопок
def scroll_canvas(delta):
    canvas.xview_scroll(delta, "units")

# Добавляем кнопки для вкладок
buttons = []
for name in tab_names:
    btn = tk.Button(scroll_frame, text=name, command=lambda n=name: switch_tab(n))
    btn.pack(side="left", padx=5, pady=5)
    buttons.append(btn)

# Обновление размеров Canvas после добавления кнопок
def update_scroll_region():
    canvas.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))

root.after(100, update_scroll_region)

# 📌 Прокрутка мышкой (Shift + колесо)
canvas.bind("<Shift-MouseWheel>", lambda event: scroll_canvas(-1 if event.delta > 0 else 1))

# 📌 Кнопки для скролла влево/вправо
btn_left = tk.Button(button_frame, text="⬅", command=lambda: scroll_canvas(-2))
btn_left.pack(side="left", padx=5)

btn_right = tk.Button(button_frame, text="➡", command=lambda: scroll_canvas(2))
btn_right.pack(side="right", padx=5)

# Запуск приложения
root.mainloop()
