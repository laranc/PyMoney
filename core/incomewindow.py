# savingswindow.py
import json
import tkinter as tk
from tkinter import ttk, Tk, Text, PhotoImage
from tkinter.tix import COLUMN

# database
import tools.datahandler as dh


class income_window(tk.Tk):
    def __init__(self, time_data: str, time_raw: str) -> None:
        super().__init__()
        # get time
        self.time_data = time_data
        self.time_raw = time_raw

        # set window icon
        # self.win_icon = PhotoImage(file="./icons/income-icon.png")
        # print(self.win_icon) # not working, pyimage 1?
        # self.iconphoto(False, self.win_icon)

        # set initial data
        self.title("PyMoney --> Income Window")
        self.geometry("500x300")

        # title label
        self.title_label = ttk.Label(
            self, text="PyMoney Income Interface",
            font=("Lucidia 20 bold")
        )
        self.title_label.grid(row=0, column=0, columnspan=2)

        # income label
        self.income_label = ttk.Label(
            self, text="Income for " + self.time_raw,
            font="Lucidia 20 bold")
        self.income_label.grid(row=1, column=0, columnspan=2)

        # table frame
        self.income_table = ttk.Frame(
            master=self, relief=tk.SOLID, borderwidth=2)
        self.income_table.grid(row=2, column=0, rowspan=2)

        self.display_data()

        # add income frame
        self.add_income_frame = ttk.Frame(
            master=self, relief=tk.SOLID, borderwidth=2)
        self.add_income_frame.grid(row=2, column=1)

        # labels
        self.add_income_frame.add_income_label = ttk.Label(
            self.add_income_frame, text="Add Income")
        self.add_income_frame.add_income_label.grid(
            row=0, column=0, columnspan=2)

        self.add_income_frame.add_income_name_label = ttk.Label(
            self.add_income_frame, text="Income Name")
        self.add_income_frame.add_income_name_label.grid(row=1, column=0)

        self.add_income_frame.add_income_value_label = ttk.Label(
            self.add_income_frame, text="Income Value")
        self.add_income_frame.add_income_value_label.grid(row=2, column=0)

        # text input
        self.add_income_frame.add_income_name_input = Text(
            self.add_income_frame, height=1, width=20)
        self.add_income_frame.add_income_name_input.grid(row=1, column=1)

        self.add_income_frame.add_income_value_input = Text(
            self.add_income_frame, height=1, width=20)
        self.add_income_frame.add_income_value_input.grid(row=2, column=1)

        # submit data
        self.add_income_frame.add_new_income_button = ttk.Button(
            self.add_income_frame, text="Add New Income", command=self.add_new_income_EV)
        self.add_income_frame.add_new_income_button.grid(
            row=3, column=0, columnspan=2)

        # remove income frame
        self.remove_income_frame = ttk.Frame(
            master=self, relief=tk.SOLID, borderwidth=2)
        self.remove_income_frame.grid(row=3, column=1)

        # labels
        self.remove_income_frame.remove_income_label = ttk.Label(
            self.remove_income_frame, text="Remove Income")
        self.remove_income_frame.remove_income_label.grid(
            row=0, column=0, columnspan=2)

        self.remove_income_frame.remove_income_name_label = ttk.Label(
            self.remove_income_frame, text="Income Name")
        self.remove_income_frame.remove_income_name_label.grid(
            row=1, column=0)

        self.remove_income_frame.remove_income_value_label = ttk.Label(
            self.remove_income_frame, text="Income Value")
        self.remove_income_frame.remove_income_value_label.grid(
            row=2, column=0)

        # text input
        self.remove_income_frame.remove_income_name_input = Text(
            self.remove_income_frame, height=1, width=20)
        self.remove_income_frame.remove_income_name_input.grid(
            row=1, column=1)

        self.remove_income_frame.remove_income_value_input = Text(
            self.remove_income_frame, height=1, width=20)
        self.remove_income_frame.remove_income_value_input.grid(
            row=2, column=1)

        # submit data
        self.remove_income_frame.remove_new_income_button = ttk.Button(
            self.remove_income_frame, text="Remove Income", command=self.remove_income_EV)
        self.remove_income_frame.remove_new_income_button.grid(
            row=3, column=0, columnspan=2)

    def display_data(self) -> None:
        # get json data
        json_data, json_obj = dh.pull_data(
            self.time_data[3], self.time_data[2])
        del(json_obj)
        print(f"DATA = {json_data}")
        if len(json_data) == 0:  # file empty
            self.income_table.income_table_name_label = ttk.Label(
                self.income_table, text="Name-")
            self.income_table.income_table_name_label.grid(row=0, column=0)
            self.income_table.income_table_value_label = ttk.Label(
                self.income_table, text="-Value")
            self.income_table.income_table_value_label.grid(row=0, column=1)
        else:  # file is full
            self.income_table.destroy()
            self.income_table = ttk.Frame(
                master=self, relief=tk.SOLID, borderwidth=2)
            self.income_table.grid(row=2, column=0, rowspan=2)
            self.income_table.income_table_name_label = ttk.Label(
                self.income_table, text="Name-")
            self.income_table.income_table_name_label.grid(row=0, column=0)
            self.income_table.income_table_value_label = ttk.Label(
                self.income_table, text="-Value")
            self.income_table.income_table_value_label.grid(row=0, column=1)
            row = 1
            print(f"JSON DATA {json_data}")
            for key in json_data[2]:
                name = ttk.Label(self.income_table, text=f"{key}")
                name.grid(row=row, column=0)
                value = ttk.Label(self.income_table,
                                  text=f"{json_data[2][key]}")
                value.grid(row=row, column=1)
                row += 1

    def add_new_income_EV(self) -> None:
        name = self.add_income_frame.add_income_name_input.get(
            1.0, tk.END+'-1c')
        value = self.add_income_frame.add_income_value_input.get(
            1.0, tk.END+'-1c')

        dh.push_data(self.time_data[3],
                     self.time_data[2], "incomes", name, value)
        self.display_data()

    def remove_income_EV(self) -> None:
        name = self.remove_income_frame.remove_income_name_input.get(
            1.0, tk.END+'-1c')
        value = self.remove_income_frame.remove_income_value_input.get(
            1.0, tk.END+'-1c')

        dh.remove_data(self.time_data[3],
                       self.time_data[2], "incomes", name, value)
        self.display_data()
