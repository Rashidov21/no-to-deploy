import cv2
import numpy as np
import pycaw

# Инициализация библиотеки для управления громкостью
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

# Инициализация OpenCV
cap = cv2.VideoCapture(0)

# Инициализация управления громкостью
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = interface.QueryInterface(IAudioEndpointVolume)

# Получение диапазона громкости
volume_range = volume.GetVolumeRange()
min_vol = volume_range[0]
max_vol = volume_range[1]

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Преобразование изображения в HSV для лучшего обнаружения кожи
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Определение диапазона цвета кожи в HSV
    lower_skin = np.array([0, 20, 70], dtype=np.uint8)
    upper_skin = np.array([20, 255, 255], dtype=np.uint8)

    # Создание маски для кожи
    mask = cv2.inRange(hsv, lower_skin, upper_skin)

    # Нахождение контуров
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Если контуры найдены
    if contours:
        # Нахождение самого большого контура (предполагаем, что это рука)
        max_contour = max(contours, key=cv2.contourArea)

        # Нахождение выпуклой оболочки и дефектов
        hull = cv2.convexHull(max_contour, returnPoints=False)
        defects = cv2.convexityDefects(max_contour, hull)

        if defects is not None:
            for i in range(defects.shape[0]):
                s, e, f, d = defects[i, 0]
                start = tuple(max_contour[s][0])
                end = tuple(max_contour[e][0])
                far = tuple(max_contour[f][0])

                # Определение положения пальца
                # Здесь можно добавить логику для определения положения пальца

                # Пример: Управление громкостью в зависимости от Y-координаты пальца
                y = far[1]
                vol = np.interp(y, [50, 400], [min_vol, max_vol])
                volume.SetMasterVolumeLevel(vol, None)

    # Отображение изображения
    cv2.imshow('Frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()