import time
import random
import webbrowser
import keyboard
import os

url = 'https://youtu.be/fkSI7usVNXA'
chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s -incognito'

def opentab():
    webbrowser.get(chrome_path).open(url, new=1)
    numb = random.randint(6, 10)
    time.sleep(numb)

if keyboard.is_pressed('p') != True:

    amount = 0

    while (amount < 100):

        print('amount')

        os.system("start \"\" https://google.com")
        
        opentab()
        opentab()
        opentab()
        opentab()
        opentab()
        opentab()
        opentab()
        opentab()
        opentab()
        opentab()
        
        time.sleep(775)

        os.system("taskkill /im chrome.exe /f")

        os.system("start \"\" https://google.com")

        numb = random.randint(34, 67)
        time.sleep(numb)

        amount += 1