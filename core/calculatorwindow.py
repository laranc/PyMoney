import tkinter as tk
from tkinter import ttk
from tkinter import Tk
from tkinter import Text
from tkinter import PhotoImage

import tools.datahandler as dh

class calculator_window(tk.Tk):
    def __init__(self, time_data: list[str], time_raw: str) -> None:
        super().__init__()

        # get time
        self.time_data = time_data
        self.time_raw = time_raw

        # get data from json
        self.json_data: list[str] = dh.pull_data(self.time_data[3])

        # set window icon
        # self.win_icon = PhotoImage(file="./icons/")
        # print(self.win_icon) # not working, pyimage 1?
        # self.iconphoto(False, self.win_icon)

        # set initial data
        self.title("Calculator Window")
        self.geometry("600x500")

        # title label
        self.title_label = ttk.Label(
            self, text="Total Savings for" + time_raw)
        self.title_label.grid(row=0, column=4)

        # total income label
        self.total_income_label = ttk.Label(
            self, text=f"Total Income: {self.total_income_calculation()}")
        self.total_income_label.grid(row=2, column=4)

        # total expenses label
        self.total_expenses_label = ttk.Label(
            self, text=f"Total Expenses: {self.total_expenses_calculation()}")
        self.total_expenses_label.grid(row=2, column=6)

        # total savings label
        self.total_savings_label = ttk.Label(
            self, text=f"Total Savings: {self.total_savings_calculation()}")
        self.total_savings_label.grid(row=3, column=5)

        # previous savings label
        self.previous_savings_label = ttk.Label(
            self, text=f"Savings for previous month: {self.previous_savings_calculation()}")
        self.previous_savings_label.grid(row=5, column=4)

        # average income label
        self.average_income_label = ttk.Label(
            self, text=f"Average income: {self.average_income_calculation()}")
        self.average_income_label.grid(row=5, column=5)

        # average expenses label
        self.average_expenses_label = ttk.Label(
            self, text=f"Average expenses: {self.average_expenses_calculation()}")
        self.average_expenses_label.grid(row=5, column=6)

    def total_income_calculation(self) -> str:
        value: int
        total = 0
        for key in self.json_data[5]: # get income from dictionary
            value = int(self.json_data[5][key]) # pills here
            total += value

        return str(total)

    def total_expenses_calculation(self) -> str:
        value: int
        total = 0
        for key in self.json_data[4]:
            value = int(self.json_data[4][key])
            total += value

        return str(total)

    def total_savings_calculation(self) -> str:
        return str(int(self.total_income_calculation()) - int(self.total_expenses_calculation())) # pills here

    def previous_savings_calculation(self) -> str:
        pass

    def average_income_calculation(self) -> str:
        pass

    def average_expenses_calculation(self) -> str:
        pass
