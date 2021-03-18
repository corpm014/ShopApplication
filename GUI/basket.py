from tkinter import *
import tkinter as tk

class Basket(tk.Tk):
    def __init__(self):
      
      super().__init__()
      self.geometry('200x200')
      self.BasketTitle = tk.Label(self,text='Basket')
      self.BasketTitle.grid(row=5,column=5)
        