import pyautogui
import cv2
import numpy as np
# from PIL import Image
import time

time.sleep(10)

screenshot = pyautogui.screenshot()
screenshot.save("screenshot1.png")

# Загрузка изображения объекта
template = cv2.imread('object.png')
result = cv2.matchTemplate(screenshot, template, cv2.TM_CCOEFF_NORMED)

# Установка порога
threshold = 0.8
yloc, xloc = np.where(result >= threshold)

# Отрисовка прямоугольников
for (x, y) in zip(xloc, yloc):
    cv2.rectangle(screenshot, (x, y), (x + template.shape[1], y + template.shape[0]), (0, 255, 0), 2)

cv2.imshow('Detected Objects', screenshot)
cv2.waitKey(0)
cv2.destroyAllWindows()












