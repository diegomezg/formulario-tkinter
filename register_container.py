import tkinter as tk
from tkinter import ttk, font


class RegisterContainer(tk.LabelFrame):
    def __init__(self, parent):
        super().__init__(parent, labelanchor='n', text='Ficha de registro para participantes', font=font.Font(family='Helvetica', size='12', weight='bold'))

        fontStyle = font.Font(family='Helvetica', size='10', weight='bold')
        fontStyle2 = font.Font(family='Helvetica', size='10')

        padx = 50

        fornameLabel = tk.Label(self, text="Nombre: ", font=fontStyle)
        fornameLabel.grid(row=0, column=0, padx=padx, pady=10, sticky='EW')
        self.fornameEntry = ttk.Entry(self, font=fontStyle2)
        self.fornameEntry.grid(row=0, column=1, columnspan=3, padx=padx, pady=10, sticky='EW')

        surnameLabel = tk.Label(self, text="Apellido: ", font=fontStyle)
        surnameLabel.grid(row=1, column=0, padx=padx, pady=10, sticky='EW')
        self.surnameEntry = ttk.Entry(self, font=fontStyle2)
        self.surnameEntry.grid(row=1, column=1, columnspan=3, padx=padx, pady=10, sticky='EW')
        
        curpLabel = tk.Label(self, text='CURP: ', font=fontStyle)
        curpLabel.grid(row=2, column=0, padx=padx, pady=10, sticky='EW')
        self.curpEntry = ttk.Entry(self, font=fontStyle2)
        self.curpEntry.grid(row=2, column=1, columnspan=3, padx=padx, pady=10, sticky='EW')

        sexLabel = tk.Label(self, text='Sexo: ', font=fontStyle)
        sexLabel.grid(row=3, column=0, padx=padx, pady=10, sticky='EW')
        self.sexValue = tk.StringVar(self)
        self.sexValue.set('M')
        mRadiobutton = ttk.Radiobutton(self, text='Masculino', value='M', variable=self.sexValue)
        mRadiobutton.grid(row=3, column=1, padx=padx, pady=10, sticky='EW')
        fRadiobutton = ttk.Radiobutton(self, text='Femenino', value='F', variable=self.sexValue)
        fRadiobutton.grid(row=3, column=3, padx=(10,50), pady=10, sticky='EW')

        stateLabel = tk.Label(self, text='Estado: ', font=fontStyle)
        stateLabel.grid(row=4, column=0, padx=padx, pady=10, sticky='EW')
        self.stateEntry = ttk.Entry(self, font=fontStyle2)
        self.stateEntry.grid(row=4, column=1, padx=padx, pady=10, sticky='EW')

        cityLabel = tk.Label(self, text='Ciudad: ', font=fontStyle)
        cityLabel.grid(row=4, column=2, padx=padx, pady=10, sticky='EW')
        self.cityEntry = ttk.Entry(self, font=fontStyle2)
        self.cityEntry.grid(row=4, column=3, padx=padx, pady=10, sticky='EW')

        blockLabel = tk.Label(self, text='Colonia: ', font=fontStyle)
        blockLabel.grid(row=6, column=0, padx=padx, pady=10, sticky='EW')
        self.blockEntry = ttk.Entry(self, font=fontStyle2)
        self.blockEntry.grid(row=6, column=1, columnspan=3, padx=padx, pady=10, sticky='EW')

        streetLabel = tk.Label(self, text='Calle: ', font=fontStyle)
        streetLabel.grid(row=7, column=0, padx=padx, pady=10, sticky='EW')
        self.streetEntry = ttk.Entry(self, font=fontStyle2)
        self.streetEntry.grid(row=7, column=1, columnspan=3, padx=padx, pady=10, sticky='EW')

        numberLabel = tk.Label(self, text='Número: ', font=fontStyle)
        numberLabel.grid(row=8, column=0, padx=padx, pady=10, sticky='EW')
        self.numberEntry = ttk.Entry(self, font=fontStyle2)
        self.numberEntry.grid(row=8, column=1, padx=padx, pady=10, sticky='EW')

        zipLabel = tk.Label(self, text='C.P: ', font=fontStyle)
        zipLabel.grid(row=8, column=2, padx=padx, pady=10, sticky='EW')
        self.zipEntry = ttk.Entry(self, font=fontStyle2)
        self.zipEntry.grid(row=8, column=3, padx=padx, pady=10, sticky='EW')

        studentLabel = tk.Label(self, text='Estudiante: ', font=fontStyle)
        studentLabel.grid(row=9, column=0, padx=padx, pady=10, sticky='EW')
        self.studentValue = tk.StringVar(self)
        self.studentValue.set('S')
        sRadioButton = ttk.Radiobutton(self, text='Sí', value='S', variable=self.studentValue)
        sRadioButton.grid(row=9, column=1, padx=padx, pady=10, sticky='EW')
        sRadioButton.bind('<Button-1>', self.__setSchool)
        nRadioButton = ttk.Radiobutton(self, text='No', value='N', variable=self.studentValue)
        nRadioButton.grid(row=9, column=3, padx=padx, pady=10, sticky='EW')
        nRadioButton.bind('<Button-1>', self.__clearSchool)

        schoolLabel = tk.Label(self, text='Escuela: ', font=fontStyle)
        schoolLabel.grid(row=10, column=0, padx=padx, pady=10, sticky='EW')
        self.schoolEntry = ttk.Entry(self, font=fontStyle2)
        self.schoolEntry.grid(row=10, column=1, padx=padx, pady=10, sticky='EW')

        categoryLabel = tk.Label(self, text='Categoría: ', font=fontStyle)
        categoryLabel.grid(row=10, column=2, padx=padx, pady=10, sticky='EW')
        self.categoryCombobox = ttk.Combobox(self, values=['', 'Infantil', 'Aficionados', 'Avanzado', 'Libre'], state='readonly')
        self.categoryCombobox.grid(row=10, column=3, padx=padx, pady=10, sticky='EW')
        self.categoryCombobox.bind('<<ComboboxSelected>>', self.__adjustCost)

        self.costLabel = tk.Label(self, text='Costo de inscripción: $0.00', font=fontStyle)
        self.costLabel.grid(row=11, column=0, columnspan=5, padx=padx, pady=10, sticky='EW')

    def data(self):
        data = [self.fornameEntry.get(), self.surnameEntry.get(), self.curpEntry.get(), self.sexValue.get(), self.stateEntry.get(), self.cityEntry.get(),
                self.blockEntry.get(), self.streetEntry.get(), self.numberEntry.get(), self.zipEntry.get(), self.studentValue.get(), self.schoolEntry.get(), self.categoryCombobox.get()]
        return data

    def clear(self):
        self.fornameEntry.delete(0, tk.END)
        self.surnameEntry.delete(0, tk.END)
        self.curpEntry.delete(0, tk.END)
        self.sexValue.set('M')
        self.stateEntry.delete(0, tk.END)
        self.cityEntry.delete(0, tk.END)
        self.blockEntry.delete(0, tk.END)
        self.streetEntry.delete(0, tk.END)
        self.numberEntry.delete(0, tk.END)
        self.zipEntry.delete(0, tk.END)
        self.studentValue.set('S')
        self.schoolEntry.config(state=tk.NORMAL)
        self.schoolEntry.delete(0, tk.END)
        self.categoryCombobox.current([0])

    def __setSchool(self, event):
        self.schoolEntry.config(state=tk.NORMAL)
        self.schoolEntry.delete(0, tk.END)

    def __clearSchool(self, event):
        self.schoolEntry.delete(0, tk.END)
        self.schoolEntry.insert(0, '-')
        self.schoolEntry.config(state=tk.DISABLED)

    def __adjustCost(self, event):
        if self.categoryCombobox.get() == 'Infantil':
            cost = 'Costo de inscripción: $29.95'
        elif self.categoryCombobox.get() == 'Aficionados':
            cost = 'Costo de inscripción: $58.99'
        elif self.categoryCombobox.get() == 'Avanzado':
            cost = 'Costo de inscripción: $89.85'
        else:
            cost = 'Costo de inscripción: $49.95'
        self.costLabel.config(text=cost)