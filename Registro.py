import tkinter as tk
from tkinter import font, ttk
from main_frame import MainFrame
from data_frame import DataFrame


class Registro(tk.Tk):
    def __init__(self):
        super().__init__()

        self.winfo_toplevel().title("Registro Torneo")
        self.resizable(0, 0)

        self.dataFrame = DataFrame(self, lambda: self.showFrame('register'))
        self.dataFrame.grid(row=0, column=0, sticky='NSEW')

        self.mainFrame = MainFrame(self, lambda: self.showFrame('data'))
        self.mainFrame.grid(row=0, column=0, sticky='NSEW')

        self.frames = dict()
        self.frames['register'] = self.mainFrame
        self.frames['data'] = self.dataFrame

    def showFrame(self, frame):
        toShow = self.frames[frame]
        toShow.tkraise()


app = Registro()
app.mainloop()
