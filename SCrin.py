import pyautogui
import cv2
import numpy as np
from PIL import Image
import time

def capture_and_process(interval, duration):
      end_time = time.time() + duration
      count = 1

      while time.time() < end_time:
           # Захват изображения
         screenshot = pyautogui.screenshot()
           
           # Обработка (например, преобразование в черно-белое)
         screenshot = screenshot.convert("L")
           
           # Сохранение изображения
         screenshot.save(f"screenshot_{count}.png")
         count += 1
           
           # Ожидание
         time.sleep(interval)

   # Запуск функции: захват каждый 5 секунд в течение 1 минуты
capture_and_process(interval=5, duration=60)












