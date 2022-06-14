# expensewindow.py
import tkinter as tk
from tkinter import Tk
from tkinter import ttk
from tkinter import PhotoImage

import tools.datahandler as dh

class expense_window(tk.Tk):
    def __init__(self, time_data: list[str], time_raw: str) -> None:
        super().__init__()
    
        # get time
        self.time_data = time_data
        self.time_raw = time_raw

        # dialog boxes
        global add_expense
        global remove_expense

        # set window icon
        self.win_icon = PhotoImage(file='./icons/expense-icon.png')
        print(self.win_icon) # not working, pyimage 1?
        self.iconphoto(False, self.win_icon)


        # set initial data
        self.title("Expense Window")
        self.geometry("500x600")

        # title label
        self.title_label = ttk.Label(
            self, text="Expense for " + self.time_raw)
        self.title_label.grid(row=0, column=4)

        # get json data
        dh.pull_data(self.time_data[3])

        # table frame
        expenses_table_frame = ttk.Frame(
            master=self,
            relief=tk.SOLID,
            borderwidth=2)

        for x in range(2):
            for y in range(2):
                label = ttk.Label(self, text="daasdasdasd")
                label.grid(row=x, column=y)

        expenses_table_frame.grid(row=6, column=5)
        expenses_table = ttk.Label(self, text="Placeholder")
        expenses_table.grid(row=0, column=1)

        # # table scrollbar
        # expenses_table_scroll = ttk.Scrollbar(expenses_table_frame)
        # expenses_table_frame.pack(side=RIGHT, fill=Y)

        # # savings table
        # expenses_table = ttk.Treeview(
        #     expenses_table_frame, yscrollcommand=expenses_table_scroll)
        # expenses_table.pack()

        # expenses_table_scroll.config(command=expenses_table.yview)

        # # table configs
        # expenses_table["columns"] = ("name", "value")

        # # table columns
        # expenses_table.column("#0", width=0, stretch=NO)
        # expenses_table.column("name", anchor=CENTER, width=80)
        # expenses_table.column("value", anchor=CENTER, width=80)

        # # table headings
        # expenses_table.heading("#0", text="", anchor=CENTER)
        # expenses_table.heading("name", text="Name", anchor=CENTER)
        # expenses_table.heading("value", text="Value", anchor=CENTER)
