import webbrowser
import time
import os

url = 'https://www.youtube.com/watch?v=pJlnxbO5N2g'
chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s --incognito'
webbrowser.get(chrome_path)
webbrowser.open(url, new=2, autoraise=True)
time.sleep(5)
os.system("taskkill /im chrome.exe /f")
