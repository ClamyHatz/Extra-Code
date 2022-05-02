# p227_starter_one_button_shell.py
import subprocess
import tkinter as tk
import tkinter.messagebox
import tkinter.scrolledtext as tksc
from tkinter import filedialog
from PIL import Image, ImageTk
from tkinter.filedialog import asksaveasfilename

def do_command(command):
    global command_textbox, url_entry

    # If url_entry is blank, use localhost IP address 
    url_val = url_entry.get()
    if (len(url_val) == 0):
        # url_val = "127.0.0.1"
        url_val = "::1"
    
    # use url_val 
    p = subprocess.Popen(command + ' ' + url_val, stdout=subprocess.PIPE, stderr=subprocess.PIPE) #v2
    
    command_textbox.delete(1.0, tk.END)
    command_textbox.insert(tk.END, command + " working....\n")
    command_textbox.update()

    cmd_results, cmd_errors = p.communicate()
    command_textbox.insert(tk.END, cmd_results)
    command_textbox.insert(tk.END, cmd_errors)

def warning():
  tkinter.messagebox.showerror("Error", "Tracer has stopped working")

def mSave():
  filename = asksaveasfilename(defaultextension='.txt',filetypes = (('Text files', '*.txt'),('Python files', '*.py *.pyw'),('All files', '*.*')))
  if filename is None:
    return
  file = open (filename, mode = 'w')
  text_to_save = command_textbox.get("1.0", tk.END)
  
  file.write(text_to_save)
  file.close()

root = tk.Tk()
root.title("Ip Search")
ico = Image.open("D:/CSP/Unit 2/2.2.7/glass.png")
photo = ImageTk.PhotoImage(ico)
root.wm_iconphoto(False, photo)

# creates the frame with label for the text box
Title = tk.Frame(root, pady=10, padx=321, bg="#9CECFF") # change frame color
Title.pack()

url_label = tk.Label(Title, text="Find URL Properties", 
    compound="center",
    anchor="center",
    font=("Arial Black", 12),
    bd=0, 
    relief=tk.FLAT, 
    fg="black",
    bg="#9CECFF")
url_label.pack(side=tk.LEFT)

frame_URL = tk.Frame(root, pady=10, padx=188, bg="#9CECFF") # change frame color
frame_URL.pack()

# decorative label
url_label = tk.Label(frame_URL, text="Enter a URL of interest:   ", 
    compound="center",
    font=("Arial Black", 12),
    bd=0, 
    relief=tk.FLAT, 
    fg="Black",
    bg="#9CECFF")
url_label.pack(side=tk.LEFT)

url_entry= tk.Entry(frame_URL,  font=("Arial Black", 12),) # change font
url_entry.pack(side=tk.LEFT)

frame_btn = tk.Frame(root,  bg="#9CECFF") # change frame color
frame_btn.pack()

# set up button to run the do_command function
ping_btn = tk.Button(frame_btn, text="Check to see if a URL is up and active", command=lambda:do_command("ping"), font=("Arial Black", 10), activebackground = "green", activeforeground = "white", bd = 4, relief=tk.RAISED)
ping_btn.pack()

trace_btn = tk.Button(frame_btn, text="Trace the path to get to the website", command=lambda: [warning(), do_command("tracert")], font=("Arial Black", 10), activebackground = "green", activeforeground = "white", bd=4, relief="raised")
trace_btn.pack()

lookup_btn = tk.Button(frame_btn, text="Check the website's IP adress", command=lambda:do_command("NSlookup"), font=("Arial Black", 10), activebackground = "green", activeforeground = "white", bd=4, relief="raised")
lookup_btn.pack()

save_btn = tk.Button(frame_btn, text="Save", command=lambda:mSave(), font=("Arial Black", 10), activebackground = "green", activeforeground = "white", bd=4, relief="raised")
save_btn.pack()

# Adds an output box to GUI.
command_textbox = tksc.ScrolledText(frame_btn, height=10, width=100)
command_textbox.pack()




root.mainloop()
