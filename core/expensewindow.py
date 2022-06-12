# expensewindow.py
import tkinter as tk
from tkinter import CENTER, RIGHT, Y, Tk
from tkinter import ttk
import time


class expense_window(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        # dialog boxes
        global add_expense
        global remove_expense

        # set initial data
        self.title("Expense Window")
        self.geometry("500x600")

        # title label
        self.title_label = ttk.Label(
            self, text="Expense for " + time.strftime("%B", time.localtime(time.time())))
        self.title_label.grid(row=0, column=4)

        # table frame
        expenses_table_frame = ttk.Frame(self)
        expenses_table_frame.pack()

        # table scrollbar
        expenses_table_scroll = ttk.Scrollbar(expenses_table_frame)
        expenses_table_frame.pack(side=RIGHT, fill=Y)

        # savings table
        expenses_table = ttk.Treeview(
            expenses_table_frame, yscrollcommand=expenses_table_scroll)
        expenses_table.pack()

        expenses_table_scroll.config(command=expenses_table.yview)

        # table configs
        expenses_table["columns"] = ("name", "value")
        expenses_table.column("name", anchor=CENTER, width=80)
        expenses_table.column("value", anchor=CENTER, width=80)

        # table headings
        expenses_table.heading("name", text="Name", anchor=CENTER)
        expenses_table.heading("value", text="Value", anchor=CENTER)
