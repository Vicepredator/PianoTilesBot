from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api
import win32con


def doClick(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


def checkColor():
    if pyautogui.pixel(400, 400)[0] == 0:
        doClick(400, 400)
    if pyautogui.pixel(480, 400)[0] == 0:
        doClick(480, 400)
    if pyautogui.pixel(550, 400)[0] == 0:
        doClick(550, 400)
    if pyautogui.pixel(620, 400)[0] == 0:
        doClick(620, 400)


while 1:
    while keyboard.is_pressed('w') == False:
        print('Waiting')
    while keyboard.is_pressed('q') == False:
        try:
            checkColor()
        except:
            checkColor()
