import pyautogui
import time

time.sleep(10)
x, y =pyautogui.position()
print(f"マウスの位置: X{x}, Y{y}")

import pyautogui
import time

def auto_click(x, y, interval=6):
    while True:
        pyautogui.rightClick(x, y)
        time.sleep(interval)
          
auto_click(,) 
