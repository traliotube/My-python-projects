import pyautogui
import time

time.sleep(5)

i = 0
while i < 20:
    pyautogui.hotkey('ctrl', 'shift', 'n')
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'enter')
    time.sleep(8)
    pyautogui.hotkey('ctrl', 'w')
    time.sleep(1)
    i += 1
