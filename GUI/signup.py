import tkinter as tk
from tkinter import *
# for the sign up could you also add email as well?

class SignUpApp(tk.Tk):
    def __init__(self, userManager, database):
        self.userManager = userManager
        self.database = database

        super().__init__()
        self.l0 = Label(self,text = "Signup")
        self.l0.grid(row=3,column=5)

        self.usernamel=tk.Label(self, text="Username/Email Address")
        self.usernamel.grid(row=2,column=0)

        self.username=tk.Entry(self)
        self.username.grid(row=2,column=3,columnspan=10)

        self.passwordl=tk.Label(self, text="Password ")
        self.passwordl.grid(row=3,column=0)

        self.password=tk.Entry(self)
        self.password.grid(row=3,column=3,columnspan=10)

        self.signup_btn = tk.Button(self,text='Create Account')
        self.signup_btn.grid(row=4,column=3)
      
      
def signup(self):
  pass

