from tkinter import *
import tkinter as tk

def openShop():
    print("hi")

def openAdmin():
    print("bye")

  
class Homepage(tk.Tk):
    def __init__(self):
        super().__init__()
        self.welcome = tk.Label(self, text='Welcome to homepage')
        self.welcome.grid(row=1, column=1)
        self.space1 = tk.Label(self, text=' ')
        self.space1.grid(row=2, column=1)
        self.shop_btn = tk.Button(self, text='Shop Page',command=openShop)
        self.shop_btn.grid(row=3, column=1)
        self.admin_btn = tk.Button(self, text='Admin',command=openAdmin)
        self.admin_btn.grid(row=3,column=2)


