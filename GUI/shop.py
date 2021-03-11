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
        


