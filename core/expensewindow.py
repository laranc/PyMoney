# expensewindow.py
import tkinter as tk
from tkinter import ttk, Tk, Text, PhotoImage

# database
import tools.datahandler as dh


class expense_window(tk.Tk):
    def __init__(self, time_data: list[str], time_raw: str) -> None:
        super().__init__()

        # get time
        self.time_data = time_data
        self.time_raw = time_raw

        # set window icon
        # self.win_icon = PhotoImage(file="./icons/expense-icon.png")
        # print(self.win_icon) # not working, pyimage 1?
        # self.iconphoto(False, self.win_icon)

        # set initial data
        self.title("Expense Window")
        self.geometry("500x600")

        # title label
        self.title_label = ttk.Label(
            self, text="Expenses for " + self.time_raw)
        self.title_label.grid(row=0, column=0)

        # table frame
        self.expenses_table = ttk.Frame(
            master=self, relief=tk.SOLID, borderwidth=2)
        self.expenses_table.grid(row=6, column=1)

        self.expense_table_name_label = ttk.Label(
            self.expenses_table, text="Name")
        self.expense_table_name_label.grid(row=0, column=0)

        self.expense_table_value_label = ttk.Label(
            self.expenses_table, text="Value")
        self.expense_table_value_label.grid(row=0, column=1)

        self.display_data()

        # add expenses frame
        add_expenses_frame = ttk.Frame(
            master=self, relief=tk.SOLID, borderwidth=2)
        add_expenses_frame.grid(row=10, column=1)

        # labels
        self.add_expenses_name_label = ttk.Label(
            add_expenses_frame, text="Expense Name")
        self.add_expenses_name_label.grid(row=4, column=4)

        self.add_expenses_value_label = ttk.Label(
            add_expenses_frame, text="Expense Value")
        self.add_expenses_value_label.grid(row=5, column=4)

        # text input
        self.add_expenses_name_input = Text(
            add_expenses_frame, height=1, width=20)
        self.add_expenses_name_input.grid(row=4, column=5)

        self.add_expenses_value_input = Text(
            add_expenses_frame, height=1, width=20)
        self.add_expenses_value_input.grid(row=5, column=5)

        # submit data
        self.add_new_expense_button = ttk.Button(
            self, text="Add New Expense", command=self.add_new_expense_EV)
        self.add_new_expense_button.grid(row=11, column=1)

        # remove expenses frame
        remove_expenses_frame = ttk.Frame(
            master=self, relief=tk.SOLID, borderwidth=2)
        remove_expenses_frame.grid(row=10, column=4)

        self.remove_expenses_name_label = ttk.Label(
            add_expenses_frame, text="Expense Name")
        self.remove_expenses_name_label.grid(row=4, column=4)

        self.remove_expenses_value_label = ttk.Label(
            add_expenses_frame, text="Expense Value")
        self.remove_expenses_value_label.grid(row=5, column=4)

        # text input
        self.remove_expenses_name_input = Text(
            add_expenses_frame, height=1, width=20)
        self.remove_expenses_name_input.grid(row=4, column=5)

        self.remove_expenses_value_input = Text(
            add_expenses_frame, height=1, width=20)
        self.remove_expenses_value_input.grid(row=5, column=5)

        # submit data
        self.remove_new_expense_button = ttk.Button(
            self, text="Remove Expense", command=self.remove_expense_EV)
        self.remove_new_expense_button.grid(row=11, column=4)

    def display_data(self) -> None:
        # get json data

        json_data: list[str] = dh.pull_data(self.time_data[3])
        print(f"DATA = {json_data}")
        if len(json_data) == 0:  # file empty
            pass
        else:  # file is full
            row = 1
            for key in json_data[4]:
                name = ttk.Label(self.expenses_table, text=f"{key}")
                name.grid(row=row, column=0)
                value = ttk.Label(self.expenses_table,
                                  text=f"{json_data[4][key]}")
                value.grid(row=row, column=1)
                row += 1

    def add_new_expense_EV(self) -> None:
        #name = self.add_expenses_name_input.get(1.0, tk.END+'-1c')
        name = self.add_expenses_name_input.get(1.0, tk.END+'-1c')
        value = self.add_expenses_value_input.get(1.0, tk.END+'-1c')
        print(f"EXPENSE NAME: {name}")
        print(f"EXPENSE VALUE: {value}")

        dh.push_data(self.time_data[3], "expenses", name, value)
        self.display_data()

    def remove_expense_EV(self) -> None:
        name = self.remove_expenses_name_input.get(1.0, tk.END+'-1c')
        value = self.remove_expenses_value_input.get(1.0, tk.END+'-1c')

        dh.remove_data(self.time_data[3], "expenses", name, value)
        self.display_data()
