import tkinter as tk 
from tkinter import*

def login():
  if username.get() == 't'and password.get() =='t':
    enter()

class ShopPage(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('200x200')
        self.ShopTitle = tk.Label(self,text='lmkm')
        self.ShopTitle.grid(row=1,column=1)
        self.buy_btn1 = tk.Button(self,text='Buy',command=self.buy1)

    def buy1(self):
        print('falskdjflkj')


