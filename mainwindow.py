# mainwindow.py
import tkinter as tk
from tkinter import Tk
from tkinter import ttk

#windows
import expensewindow as expwin
import savingswindow as savwin
class MainWindow(tk.Tk):
    def __init__(self) -> None:
        super().__init__()

        self.title("PyMoney")
        self.geometry("800x600")

        self.buttonPlus = ttk.Button(self, text="Expenses", command=self.OpenExpenseWindow_EV)
        self.buttonPlus.grid(row=1, column=1) # padx()

        global expenseWindow
        global savingWindow

    def OpenExpenseWindow_EV(self):
        self.expenseWindow = expwin.ExpenseWindow()

    def OpenSavingsWindow_EV(self):
        self.savingsWindow = savwin.SavingsWindow()

if __name__ == '__main__':
    app = MainWindow()
    app.mainloop()
