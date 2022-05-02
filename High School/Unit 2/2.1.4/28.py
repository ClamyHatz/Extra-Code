import tkinter as tk
from tkinter.constants import ANCHOR

root = tk.Tk()
root.wm_geometry("500x400")
frame_yell = tk.Frame(root, bg="yellow", width=175, height=200)

frame_red = tk.Frame(root, bg="red", width=325, height=200)

frame_green = tk.Frame(root, bg="green2", width=175, height=200)

frame_blue = tk.Frame(root, bg="blue", width=325, height=200)

frame_blue.grid(row=0,column=0)
frame_green.grid(row=0,column=1)
frame_red.grid(row=1,column=0)
frame_yell.grid(row=1,column=1)

root.mainloop()