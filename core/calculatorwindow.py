import tkinter as tk
from tkinter import ttk, Tk, Text, PhotoImage

# database
import tools.datahandler as dh


class calculator_window(tk.Tk):
    def __init__(self, time_data: list[str], time_raw: str) -> None:
        super().__init__()

        # get time
        self.time_data = time_data
        self.time_raw = time_raw

        # get data from json
        json_data: list[str] = dh.pull_data[self.time_data[3]]

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
            self, text=f"Total Income: {self.total_income_calculation(json_data)}")
        self.total_income_label.grid(row=2, column=4)

        # total expenses label
        self.total_expenses_label = ttk.Label(
            self, text=f"Total Expenses: {self.total_expenses_calculation(json_data)}")
        self.total_expenses_label.grid(row=2, column=6)

        # total savings label
        self.total_savings_label = ttk.Label(
            self, text=f"Total Savings: {self.total_savings_calculation()}")
        self.total_savings_label.grid(row=3, column=5)

        # previous savings label
        self.previous_savings_label = ttk.Label(
            self, text=f"Savings for previous month: {self.previous_savings_calculation(json_data)}")
        self.previous_savings_label.grid(row=5, column=4)

        # average income label
        self.average_income_label = ttk.Label(
            self, text=f"Average income: {self.average_income_calculation(json_data)}")
        self.average_income_label.grid(row=5, column=5)

        # average expenses labek
        self.average_expenses_label = ttk.Label(
            self, text=f"Average expenses: {self.average_expenses_calculation(json_data)}")
        self.average_expenses_label.grid(row=5, column=6)

    def total_income_calculation(self, data: list[str]) -> int:
        value: int
        total = 0
        for key in data[5]:
            value = data[5].get(key)
            total += value

        return total

    def total_expenses_calculation(self, data: list[str]) -> int:
        value: int
        total = 0
        for key in data[4]:
            value = data[4].get(key)
            total += value

        return total

    def total_savings_calculation(self) -> int:
        return self.total_income_calculation() - self.total_expenses_calculation()

    def previous_savings_calculation(self, data: list[str]) -> int:
        pass

    def average_income_calculation(self, data: list[str]) -> int:
        pass

    def average_expenses_calculation(self, data: list[str]) -> int:
        pass
