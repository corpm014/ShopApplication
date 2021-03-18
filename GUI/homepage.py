from tkinter import *
import tkinter as tk
from GUI.login import LoginApp
from GUI.signup import SignUpApp
from GUI.admin import AdminPage
from GUI.shop import ShopPage
from GUI.Settings import Settings

  
class Homepage(tk.Tk):
    def __init__(self, userManager, database):
        self.userManager = userManager
        self.database = database

        super().__init__()
        self.welcome = tk.Label(self, text='Welcome to the homepage')
        self.welcome
        self.welcome.grid(row=1, column=1)
        self.space1 = tk.Label(self, text=' ')
        self.space1.grid(row=2, column=1)
        self.space2 = tk.Label(self, text=' ')
        self.space2.grid(row=1, column=4)
        self.shop_btn = tk.Button(self, text='Shop Page',command=self.openShop)
        self.shop_btn.grid(row=3, column=1)
        self.admin_btn = tk.Button(self, text='Admin',command=self.openAdmin)
        self.admin_btn.grid(row=3,column=3)
        self.settings = tk.Button(self, text='Settings',command=self.settings)
        self.settings.grid(row=3,column=5)
        self.login_btn = tk.Button(self, text= 'Login', command=self.login)
        self.login_btn.grid(row=4,column=3)
        self.signup_btn = tk.Button(self,text='Signup', command=self.signup)
        self.signup_btn.grid(row=4,column=1)
        self.basket_btn = tk.Button(self,text='Basket', command=self.basket)
        self.basket_btn.grid(row=4,columm=5)
        
    
    def openShop(self):
        print("Shop opened")
        shop = ShopPage()
        shop.mainloop()
    
    def closeShop(self):
        print("Shop closed")
    
    def openAdmin(self):
        print("Admin opened")
        admin = AdminPage()
        admin.mainloop()
        
    def settings(self):
        print("Settings opened")
        settings = Settings()
        settings.mainloop()
        #signupForm = SignupApp(userManager..... )
    
    def login(self):
        print("Login opened")
        loginForm = LoginApp(userManager=self.userManager, database=self.database)
        loginForm.mainloop()

    def signup(self):
        print("Signup opened")
        signUpForm = SignUpApp(userManager=self.userManager, database=self.database)
        signUpForm.mainloop()

    def basket(self):
        basket = Basket()
        basket.mainloop()
        print("Basket opened")
