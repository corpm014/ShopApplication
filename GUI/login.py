from tkinter import *
import tkinter as tk

def login():
  pass

class LoginApp(tk.Tk):
    def __init__(self, userManager, database):
        self.userManager = userManager
        self.database = database

        super().__init__()
        self.l0 = tk.Label( self, text = " Login to Shop!")
        self.l0.grid(row=0,column=4)
        self.space = tk.Label( self, text = " " )
        self.space.grid(row=1,column=2)

        self.usernamel=tk.Label(self, text="Username/Email Address")
        self.usernamel.grid(row=2,column=0)

        self.username=tk.Entry(self)
        self.username.grid(row=2,column=3,columnspan=10)

        self.passwordl=tk.Label(self, text="Password ")
        self.passwordl.grid(row=3,column=0)

        self.password=tk.Entry(self,show="*")
        self.password.grid(row=3,column=3,columnspan=10)

        self.login_btn=tk.Button(self,text="Login",command=self.login)
        self.login_btn.grid(row=4,column=3)
        self.clear_btn=tk.Button(self,text="Clear",command=self.clear_form)
        self.clear_btn.grid(row=1,column=1)
        
        self.l1 = tk.Label(self, text = " " )
        self.l1.grid(row=6,column=3)
    
    def login(self):
        password = str(self.password.get())
        username = str(self.username.get())

        requestedPw = self.database.getPassword(username=username)
        if requestedPw is None:
            print("Cannot login if user does not exist")
            return
        
        loggedIn = self.userManager.login(password=password, databasePassword=requestedPw)
        if loggedIn:
            print("User logged in")
        else:
            print("User not logged in")

    # if username.get() == 'u'and password.get() =='p':
        # print('logged in')
        

        

