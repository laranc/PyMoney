# addexpensewindow.py
import tkinter as tk
from tkinter import Tk, Text
from tkinter import ttk

class add_expense_window(tk.Tk):
    def __init__(self, time_data: list[str] = None, time_raw: str = None) -> None:
        super().__init__()

        # set initial data
        self.title("Add Expense")
        self.geometry("300x200")

        # get time
        self.time_data = time_data
        self.time_raw = time_raw

        # title label
        self.title_label = ttk.Label(self, text="Add expenses")
        self.title_label.grid(row=0, column=3)

        # labels
        self.name_label = ttk.Label(self, text="Expense Name")
        self.name_label.grid(row=4, column=4)

        self.value_label = ttk.Label(self, text="Expense Value")
        self.value_label.grid(row=5, column=4)

        # text input
        self.name_input = Text(self, height=1, width=20)
        self.name_input.grid(row=4, column=5)

        self.value_input = Text(self, height=1, width=20)
        self.value_input.grid(row=5, column=5)





        