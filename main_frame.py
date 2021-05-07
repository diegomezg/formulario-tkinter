import tkinter as tk
from tkinter import ttk, font
from register_container import RegisterContainer
from register_successful import RegisterSuccessful
from register_failed import RegisterFailed
from file_generator import FileGenerator


class MainFrame(tk.Frame):
    def __init__(self, parent, showData):
        super().__init__(parent)
        self.register = parent.dataFrame.dataContainer

        self.registerContainer = RegisterContainer(self)
        self.registerContainer.grid(row=0, column=0, columnspan=2, padx=25, pady=(25,0))#, sticky='NSEW')

        self.registerButton = tk.Button(self, text='REGISTRARSE', bg='#4a5fff', font=font.Font(family='Helvetica', size='12', weight='bold'), command=self.validateInfo)
        self.registerButton.grid(row=1, column=0, padx=25, pady=10, sticky='NSEW')  

        self.dataButton = tk.Button(self, text='PARTICIPANTES', bg='#ffbf45', font=font.Font(family='Helvetica', size='12', weight='bold'), command=showData)
        self.dataButton.grid(row=1, column=1, padx=25, pady=10, sticky='NSEW')

    def validateInfo(self):
        if all(self.registerContainer.data()):
            self.register.addParticipant(self.registerContainer.data())
            FileGenerator.createTicket(len(self.register.participants), self.registerContainer.data())
            self.registerContainer.clear()
            success = RegisterSuccessful(self)
            success.mainloop()
        else:
            failed = RegisterFailed()
            failed.mainloop()      