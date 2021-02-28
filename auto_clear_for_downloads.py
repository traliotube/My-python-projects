import time
import pyautogui

i = 0

pyautogui.hotkey('alt', 'tab')
pyautogui.moveTo(1351, 315)


while i < 10:
    pyautogui.click()
    time.sleep(0.1)
    i += 1

pyautogui.hotkey('alt', 'tab')
