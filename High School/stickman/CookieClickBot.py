from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

time.sleep(2)

def click (x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while keyboard.is_pressed('q') == False:
        
    pic = pyautogui.screenshot(region=(250,450,100,100))

    width, hieght = pic.size

    for x in range(0,width,5):
        for y in range(0,hieght,5):

            r,g,b = pic.getpixel((x,y))

            if (r in range(195,200)):
                click(x+250, y+450)
                time.sleep(0.05)
                break

    pic = pyautogui.screenshot(region=(1825,210,50,850))

    width, hieght = pic.size

    for x in range(0,width,5): #(startpoint, MaxPoint, upBy)
        for y in range(0,hieght,5):

            r,g,b = pic.getpixel((x,y))

            if (r in range(130,160)):
                click(x+1825, y+210)
                time.sleep(0.05)
                break