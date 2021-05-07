import tkinter as tk
from tkinter import ttk, font
from data_container import DataContainer

class DataFrame(tk.LabelFrame):
    def __init__(self, parent, showRegister):
        super().__init__()

        self.dataContainer = DataContainer(self)
        self.dataContainer.grid(row=0, column=0, padx=25, pady=(25,0), sticky='NSEW')

        self.registerButton = tk.Button(self, text='REGISTRO', bg='#ffbf45', font=font.Font(family='Helvetica', size='12', weight='bold'), command=showRegister)
        self.registerButton.grid(row=1, column=0, padx=25, pady=10, sticky='NSEW')