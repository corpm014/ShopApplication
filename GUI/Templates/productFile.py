import tkinter as tk

class ProductTemplate(tk.Frame):
    def __init__(self, productName, productID, productImageLocation):
        self.productName = productName
        self.productID = productID
        self.productImageLocation = productImageLocation
    