# mainwindow.py
import tkinter as tk
from tkinter import Tk
from tkinter import ttk
from tkinter.messagebox import showinfo

import sqlite3

class MainWindow(tk.Tk):
    def __init__(self) -> None:
        super().__init__()

        self.title("PyMoney")
        self.geometry('400x500')

        self.buttonPlus = ttk.Button(self, text="Expenses")
        self.buttonPlus.grid(row=1, column=1) # padx()

    def numButtonPressed_EV(self):
        oldValue = self.equationLabel.value
        self.equationLabel.config(text=f"{str(oldValue) + str('1')}")


if __name__ == '__main__':
    app = MainWindow()
    app.mainloop()
