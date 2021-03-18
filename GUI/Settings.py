import tkinter as tk 
from tkinter import*

class Settings(tk.Tk):
    def __init__(self):
        # make it so you have to sign in first

      if login:
          super().__init__()
          self.geometry('200x200')
          self.welcome = tk.Label(self,text='Settings page')
          self.welcome.grid(row=1,column=1)
          self.delete_btn = tk.Button(self,text='Delete Account') 
          self.delete_btn.grid(row=2,column=1)
          self.change_btn = tk.Button(self,text='Change Username')
          self.change_btn.grid(row=3,column=1)

      else:

          print("Please Login")
