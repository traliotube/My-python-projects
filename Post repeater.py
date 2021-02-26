import pyautogui
import time

time.sleep(5)

i = 0
while i < 15:
    pyautogui.hotkey('ctrl', 'shift', 'n')
    time.sleep(1)
    pyautogui.typewrite(
        "https://medium.com/@bunnypranav/4-best-discord-bots-8297ffd6532a")
    pyautogui.hotkey('ctrl', 'enter')
    time.sleep(8)
    pyautogui.hotkey('ctrl', 'w')
    time.sleep(1)
    i += 1
