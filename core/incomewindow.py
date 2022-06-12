# savingswindow.py
import tkinter as tk
from tkinter import CENTER, RIGHT, Y, Tk
from tkinter import ttk
import time


class income_window(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        # dialog boxes
        global add_income
        global remove_income

        # set initial data
        self.title("Income Window")
        self.geometry("500x600")

        # title label
        self.title_label = ttk.Label(
            self, text="Savings for " + time.strftime("%B", time.localtime(time.time())))
        self.title_label.grid(row=0, column=4)

        # table frame
        income_table_frame = ttk.Frame(self)
        income_table_frame.pack()

        # table scrollbar
        income_table_scroll = ttk.Scrollbar(income_table_frame)
        income_table_frame.pack(side=RIGHT, fill=Y)

        # savings table
        income_table = ttk.Treeview(
            income_table_frame, yscrollcommand=income_table_scroll)
        income_table.pack()

        income_table_scroll.config(command=income_table.yview)

        # table configs
        income_table["columns"] = ("name", "value")
        income_table.column("name", anchor=CENTER, width=80)
        income_table.column("value", anchor=CENTER, width=80)

        # table headings
        income_table.heading("name", text="Name", anchor=CENTER)
        income_table.heading("value", text="Value", anchor=CENTER)
