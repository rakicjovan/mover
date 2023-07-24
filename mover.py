import win32api
import time
import pyautogui


def getIdleTime():
    return (win32api.GetTickCount() - win32api.GetLastInputInfo()) / 1000.0


def moveMouse():
    while(getIdleTime() > 240):
        pyautogui.press('shift')
    return 0

while (True):
    if (getIdleTime() > 240):
        moveMouse()
    time.sleep(30)


