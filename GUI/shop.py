import tkinter as tk 
from tkinter import*


def login():
  if username.get() == 't'and password.get() =='t':
    enter()

class ShopPage(tk.Tk):
    def __init__(self):

        super().__init__()
        self.geometry('200x200')
        self.ShopTitle = tk.Label(self,text='Shop')
        self.ShopTitle.grid(row=5,column=5)

        self.buy_btn1 = tk.Button(self,text='Item1',command=self.buy1)
        self.buy_btn1.grid(row=2,column=1)

        self.buy_btn2 = tk.Button(self,text='Item2',command=self.buy2)
        self.buy_btn2.grid(row=3,column=1)

        self.buy_btn3 = tk.Button(self,text='Item3',command=self.buy3)
        self.buy_btn3.grid(row=4,column=1)

        

    def buy1(self):
        print('one')

    def buy2(self):
        print("two")
        
    def buy3(self):
        print("three")

    

