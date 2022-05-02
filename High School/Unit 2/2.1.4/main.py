##############################################################################
#   a113_TR_simple_window1.py
#   Example soulution: Change its size to 200 by 100 pixels.
##############################################################################
import tkinter as tk
import tkinter.messagebox as mb

def test_my_button():
    frame_auth.tkraise()

def set_authorization(self, user="admin", pw="P4sS30rd"):
    self.username = user
    self.password = pw

def set_authentication(self, user_question="Whats the name of your first Dog?", user_answer="Quade"):
    self.security_question = "Whats the name of your first Dog"
    self.answer = "Quade"

def authenticate(self):
    factor_info = self.ent_auth.get()
    if(factor_info == self.answer):
        # authenticted - create the restricted app 
        self.frame_restrict = tk.Frame(self, bg="green")
        self.title("Welcome to the Restricted Application")
        self.frame_restrict.grid(row=0, column=0, sticky="news")
  
        lbl_msg = tk.Label(self.frame_restrict,text="This is a restricted application.", bg="green")
        lbl_msg.config(font=("Arial", 18))
        lbl_msg.pack(pady=15)

        lbl_auth = tk.Label(self.frame_restrict,text="Contratulations!\nYou have authenticated!", bg="green")
        lbl_auth.pack(pady=30)

        # show this restricted app frame
        self.frame_restrict.tkraise()
    else:
        mb.showinfo("Authentication","We're sorry, but our records do not match your entry.")

def authorize(self):
    student_username = self.ent_username.get()
    student_password = self.ent_password.get()
    if (student_username == self.username and  student_password == self.password):
        # authorized - create authentication frame and widgets
        self.frame_auth = tk.Frame(self, bg="blue")
        self.title("Authenticate")
        self.frame_auth.grid(row=0, column=0, sticky="news")

        self.lbl_auth = tk.Label(self.frame_auth,text=self.security_question + "?", bg="blue")
        self.lbl_auth.pack(pady=5)
        self.ent_auth = tk.Entry(self.frame_auth, show="*", bd=3)
        self.ent_auth.pack(pady=5)

        self.btn_auth = tk.Button(self.frame_auth, text="AUTHENTICATE", command=self.authenticate)
        self.btn_auth.pack(pady=15)
        
        # show this authtication frame
        self.frame_auth.tkraise()

    else:
        mb.showinfo("Login failed","Invalid username and/or password")

root = tk.Tk()
root.wm_geometry("400x300")

frame_login = tk.Frame(root)

frame_auth = tk.Frame(root)

lbl_username = tk.Label(frame_login, text="Username:",font="Courier")
lbl_username.pack(pady = 10, padx = 150)

ent_username = tk.Entry(frame_login, bd=3)
ent_username.pack(pady=5,padx=100)

lbl_password = tk.Label(frame_login,text="Password:",font="Courier")
lbl_password.pack(pady = 10, padx = 150)

ent_username = tk.Entry(frame_login, bd=3, show='*')
ent_username.pack(pady=10, padx=100)

btn_login = tk.Button(frame_login,bd=3,text="Login", command=test_my_button)
btn_login.pack(pady=10, padx=100)

frame_login.grid(row=0,column=0, sticky="news")
frame_auth.grid(row=0,column=0, sticky="news")

frame_login.tkraise()

# main window
oldtitle = root.title()
root.title('Authorization')




root.mainloop()