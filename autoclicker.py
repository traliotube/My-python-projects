import pyautogui
import time

notime = int(input("How many times should i Click: "))
sleep = int(input("How much Delay (in seconds): "))

time.sleep(5)

i = 0
while i < notime:
    pyautogui.click()
    time.sleep(sleep)
    i += 1
