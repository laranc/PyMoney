# expensewindow.py
import tkinter as tk
from tkinter import Tk
from tkinter import ttk

class ExpenseWindow(tk.Tk):
    def __init__(self) -> None:
        super().__init__()

        # set initial data
        self.title("Expense Window")
        self.geometry("500x600")
        