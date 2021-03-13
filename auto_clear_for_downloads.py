import time
import pyautogui

i = 0

pyautogui.hotkey('win', '2')
pyautogui.hotkey('ctrl', 'j')
pyautogui.moveTo(1351, 315)


while i < 20:
    pyautogui.click()
    time.sleep(0.1)
    i += 1
