import tkinter as tk
from tkinter import ttk

class RegisterFailed(tk.Tk):
    def __init__(self):
        super().__init__()

        self.resizable(0,0)

        label = tk.Label(self, text='Por favor complete todos los campos\n para registrarse.')
        label.grid(row=0, column=0, padx=15, pady=15, sticky='NSEW')

        button = ttk.Button(self, text='OK', command=self.destroy)
        button.grid(row=1, column=0, padx=15, pady=15, sticky='EW')