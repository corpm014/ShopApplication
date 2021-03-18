import tkinter as tk
from tk import *

class AdminPage(tk.Tk):
  def __init__(self):
    
      super().__init__()
      self.geometry('200x200')
      self.BasketTitle = tk.Label(self,text='AdminPage')
      self.BasketTitle.grid(row=5,column=5)
        