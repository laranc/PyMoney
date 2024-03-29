# expensewindow.py
import tkinter as tk
from tkinter import ttk, Tk, Text, PhotoImage

# database
import tools.datahandler as dh


class expense_window(tk.Tk):
    def __init__(self, time_data: str, time_raw: str) -> None:
        super().__init__()
        # get time
        self.time_data = time_data
        self.time_raw = time_raw

        # set window icon
        # self.win_icon = PhotoImage(file="./icons/expense-icon.png")
        # print(self.win_icon) # not working, pyimage 1?
        # self.iconphoto(False, self.win_icon)

        # set initial data
        self.title("PyMoney --> Expense Window")
        self.geometry("500x300")

        # title label
        self.title_label = ttk.Label(
            self, text="PyMoney Expense Interface",
            font=("Lucidia 20 bold")
        )
        self.title_label.grid(row=0, column=0, columnspan=2)

        # expense label
        self.expense_label = ttk.Label(
            self, text="Expenses for " + self.time_raw,
            font=("Lucidia 20 bold")
        )
        self.expense_label.grid(row=1, column=0, columnspan=2)

        # table frame
        self.expenses_table = ttk.Frame(
            master=self, relief=tk.SOLID, borderwidth=2)
        self.expenses_table.grid(row=2, column=0, rowspan=2)

        self.display_data()

        # add expenses frame
        self.add_expenses_frame = ttk.Frame(
            master=self, relief=tk.SOLID, borderwidth=2)
        self.add_expenses_frame.grid(row=2, column=1)

        # labels
        self.add_expenses_frame.add_expenses_label = ttk.Label(
            self.add_expenses_frame, text="Add Expenses")
        self.add_expenses_frame.add_expenses_label.grid(
            row=0, column=0, columnspan=2)

        self.add_expenses_frame.add_expenses_name_label = ttk.Label(
            self.add_expenses_frame, text="Expense Name")
        self.add_expenses_frame.add_expenses_name_label.grid(row=1, column=0)

        self.add_expenses_frame.add_expenses_value_label = ttk.Label(
            self.add_expenses_frame, text="Expense Value")
        self.add_expenses_frame.add_expenses_value_label.grid(row=2, column=0)

        # text input
        self.add_expenses_frame.add_expenses_name_input = Text(
            self.add_expenses_frame, height=1, width=20)
        self.add_expenses_frame.add_expenses_name_input.grid(row=1, column=1)

        self.add_expenses_frame.add_expenses_value_input = Text(
            self.add_expenses_frame, height=1, width=20)
        self.add_expenses_frame.add_expenses_value_input.grid(row=2, column=1)

        # submit data
        self.add_new_expense_button = ttk.Button(
            self.add_expenses_frame, text="Add New Expense", command=self.add_new_expense_EV)
        self.add_new_expense_button.grid(row=3, column=0, columnspan=2)

        # remove expenses frame
        self.remove_expenses_frame = ttk.Frame(
            master=self, relief=tk.SOLID, borderwidth=2)
        self.remove_expenses_frame.grid(row=3, column=1)

        # labels
        self.remove_expenses_frame.remove_expenses_label = ttk.Label(
            self.remove_expenses_frame, text="Remove Expenses")
        self.remove_expenses_frame.remove_expenses_label.grid(
            row=0, column=0, columnspan=2)
        self.remove_expenses_frame.remove_expenses_name_label = ttk.Label(
            self.remove_expenses_frame, text="Expense Name")
        self.remove_expenses_frame.remove_expenses_name_label.grid(
            row=1, column=0)

        self.remove_expenses_frame.remove_expenses_value_label = ttk.Label(
            self.remove_expenses_frame, text="Expense Value")
        self.remove_expenses_frame.remove_expenses_value_label.grid(
            row=2, column=0)

        # text input
        self.remove_expenses_frame.remove_expenses_name_input = Text(
            self.remove_expenses_frame, height=1, width=20)
        self.remove_expenses_frame.remove_expenses_name_input.grid(
            row=1, column=1)

        self.remove_expenses_frame.remove_expenses_value_input = Text(
            self.remove_expenses_frame, height=1, width=20)
        self.remove_expenses_frame.remove_expenses_value_input.grid(
            row=2, column=1)

        # submit data
        self.remove_expenses_frame.remove_new_expense_button = ttk.Button(
            self.remove_expenses_frame, text="Remove Expense", command=self.remove_expense_EV)
        self.remove_expenses_frame.remove_new_expense_button.grid(
            row=3, column=0, columnspan=2)

    def display_data(self) -> None:
        # get json data
        json_data, json_obj = dh.pull_data(
            self.time_data[3], self.time_data[2])
        del(json_obj)
        print(f"DATA = {json_data}")
        if len(json_data) == 0:  # file empty
            self.expenses_table.expenses_table_name_label = ttk.Label(
                self.expenses_table, text="Name-")
            self.expenses_table.expenses_table_name_label.grid(row=0, column=0)
            self.expenses_table.expenses_table_value_label = ttk.Label(
                self.expenses_table, text="-Value")
            self.expenses_table.expenses_table_value_label.grid(
                row=0, column=1)
        else:  # file is full
            self.expenses_table.destroy()
            self.expenses_table = ttk.Frame(
                master=self, relief=tk.SOLID, borderwidth=2)
            self.expenses_table.grid(row=2, column=0, rowspan=2)
            self.expenses_table.expenses_table_name_label = ttk.Label(
                self.expenses_table, text="Name-")
            self.expenses_table.expenses_table_name_label.grid(row=0, column=0)
            self.expenses_table.expenses_table_value_label = ttk.Label(
                self.expenses_table, text="-Value")
            self.expenses_table.expenses_table_value_label.grid(
                row=0, column=1)
            row = 1
            print(f"JSON DATA: {json_data}")
            for key in json_data[1]:
                name = ttk.Label(self.expenses_table, text=f"{key}")
                name.grid(row=row, column=0)
                value = ttk.Label(self.expenses_table,
                                  text=f"{json_data[1][key]}")
                value.grid(row=row, column=1)
                row += 1

    def add_new_expense_EV(self) -> None:
        #name = self.add_expenses_name_input.get(1.0, tk.END+'-1c')
        name = self.add_expenses_frame.add_expenses_name_input.get(
            1.0, tk.END+'-1c')
        value = self.add_expenses_frame.add_expenses_value_input.get(
            1.0, tk.END+'-1c')
        print(f"EXPENSE NAME: {name}")
        print(f"EXPENSE VALUE: {value}")

        dh.push_data(self.time_data[3],
                     self.time_data[2], "expenses", name, value)
        self.display_data()

    def remove_expense_EV(self) -> None:
        name = self.remove_expenses_frame.remove_expenses_name_input.get(
            1.0, tk.END+'-1c')
        value = self.remove_expenses_frame.remove_expenses_value_input.get(
            1.0, tk.END+'-1c')

        dh.remove_data(
            self.time_data[3], self.time_data[2], "expenses", name, value)
        self.display_data()
