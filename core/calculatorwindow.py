import tools.datahandler as dh
import tkinter as tk
from tkinter import ttk, Tk, Text, PhotoImage


class calculator_window(tk.Tk):
    def __init__(self, time_data: str, time_raw: str) -> None:
        super().__init__()
        # get time
        self.time_data = time_data
        self.time_raw = time_raw
        self.month_lookup = {
            "Jan": 1,
            "Feb": 2,
            "Mar": 3,
            "Apr": 4,
            "May": 5,
            "Jun": 6,
            "Jul": 7,
            "Aug": 8,
            "Sep": 9,
            "Oct": 10,
            "Nov": 11,
            "Dec": 12
        }

        # get data from json
        self.json_data, self.json_obj = dh.pull_data(
            self.time_data[3], self.time_data[2])

        # set window icon
        # self.win_icon = PhotoImage(file="./icons/")
        # print(self.win_icon) # not working, pyimage 1?
        # self.iconphoto(False, self.win_icon)

        # set initial data
        self.title("PyMoney --> Calculator Window")
        self.geometry("550x300")
        #self.iconphoto(False, PhotoImage(file="../icons/main.png"))

        # title label

        self.title_label = ttk.Label(
            self, text="PyMoney Calculator Interface",
            font=("Lucida 20 bold")
        )
        self.title_label.grid(row=0, column=1)

        # savings labelf
        self.savings_label = ttk.Label(
            self, text="Total Savings for" + self.time_raw,
            font=("Lucidia 20 bold")
        )
        self.title_label.grid(row=1, column=1)

        # total income label
        self.total_income_label = ttk.Label(
            self, text=f"Total Income: ${self.total_income_calculation()}",
            font=("Lucidia 20 bold")
        )
        self.total_income_label.grid(row=2, column=1)

        # total expenses label
        self.total_expenses_label = ttk.Label(
            self, text=f"Total Expenses: ${self.total_expenses_calculation()}",
            font=("Lucidia 20 bold")
        )
        self.total_expenses_label.grid(row=3, column=1)

        # total savings label
        self.total_savings_label = ttk.Label(
            self, text=f"Total Savings: ${self.total_savings_calculation()}",
            font=("Lucidia 20 bold")
        )
        self.total_savings_label.grid(row=4, column=1)

        # previous savings label
        self.previous_savings_label = ttk.Label(
            self, text=f"Savings for previous month: ${self.previous_savings_calculation()}",
            font=("Lucidia 20 bold")
        )
        self.previous_savings_label.grid(row=5, column=1)

        # previous expenses label
        self.previous_expenses_label = ttk.Label(
            self, text=f"Expenses for previous month: ${self.previous_expenses_calculation()}",
            font=("Lucidia 20 bold")
        )
        self.previous_expenses_label.grid(row=6, column=1)

        # average income label
        self.average_income_label = ttk.Label(
            self, text=f"Average income: ${self.average_income_calculation()}",
            font=("Lucidia 20 bold")
        )
        self.average_income_label.grid(row=7, column=1)

        # average expenses label
        self.average_expenses_label = ttk.Label(
            self, text=f"Average expenses: ${self.average_expenses_calculation()}",
            font=("Lucidia 20 bold")
        )
        self.average_expenses_label.grid(row=8, column=1)

    def total_income_calculation(self) -> str:
        try:
            value: int
            total = 0
            for key in self.json_data[2]:  # get income from dictionary
                value = int(self.json_data[2][key])  # pills here
                total += value
            return str(total)
        except:
            return "0"

    def total_expenses_calculation(self) -> str:
        try:
            value: int
            total = 0
            for key in self.json_data[1]:
                value = int(self.json_data[1][key])
                total += value
            return str(total)
        except:
            return "0"

    def total_savings_calculation(self) -> str:
        # pills here
        try:
            return str(int(self.total_income_calculation()) - int(self.total_expenses_calculation()))
        except:
            return "0"

    def get_prev_data(self, current_year: str, current_month: str) -> list[str]:
        year = current_year
        prev_month_num: int
        prev_month_name: str

        if (self.month_lookup[current_month] - 1) == 0:
            year = str(int(year) - 1)
            prev_month_num = 12
            prev_month_name = "Dec"
        else:
            prev_month_num = self.month_lookup[current_month] - 1
            for key, value in self.month_lookup.items():
                if value == prev_month_num:
                    prev_month_name = key

        json_data_prev, json_obj = dh.pull_data(year, prev_month_name)
        del(json_obj)

        if len(json_data_prev) == 0:
            print("Previous month data not found")
            return []
        else:
            print("Previous month data found")
            return json_data_prev

    def previous_savings_calculation(self) -> str:
        try:
            json_data_prev = self.get_prev_data(
                self.time_data[3], self.time_data[2])

            if len(json_data_prev) == 0:
                return "0"
            else:
                value: int
                total = 0
                for key in json_data_prev[2]:
                    value = int(json_data_prev[2][key])
                    total += value
                return str(total)
        except:
            return "0"

    def previous_expenses_calculation(self) -> str:
        try:
            json_data_prev = self.get_prev_data(
                self.time_data[3], self.time_data[2])

            if len(json_data_prev) == 0:
                return "0"
            else:
                value: int
                total = 0
                for key in json_data_prev[1]:
                    value = int(json_data_prev[1][key])
                    total += value
                return str(total)
        except:
            return "0"

    def average_income_calculation(self) -> str:
        try:
            month_name = self.time_data[2]
            month_num = self.month_lookup[month_name]
            year = self.time_data[3]
            json_data = self.get_prev_data(year, month_name)
            total = 0
            count = 0
            while True:
                if len(json_data) == 0:
                    break

                for key in json_data[2]:
                    value = int(json_data[2][key])
                    total += value

                count += 1

                if (self.month_lookup[month_name] - 1) == 0:
                    year = str(int(year) - 1)
                    month_num = 12
                    month_name = "Dec"
                else:
                    month_num = self.month_lookup[month_name] - 1
                    for key, value in self.month_lookup.items():
                        if value == month_num:
                            month_name = key

                json_data = self.get_prev_data(year, month_name)

            average = total / count
            return str(round(average, 2))
        except:
            return "0"

    def average_expenses_calculation(self) -> str:
        try:
            month_name = self.time_data[2]
            month_num = self.month_lookup[month_name]
            year = self.time_data[3]
            json_data = self.get_prev_data(year, month_name)
            total = 0
            count = 0
            while True:
                if len(json_data) == 0:
                    break

                for key in json_data[1]:
                    value = int(json_data[1][key])
                    total += value

                count += 1

                if (self.month_lookup[month_name] - 1) == 0:
                    year = str(int(year) - 1)
                    month_num = 12
                    month_name = "Dec"
                else:
                    month_num = self.month_lookup[month_name] - 1
                    for key, value in self.month_lookup.items():
                        if value == month_num:
                            month_name = key

                json_data = self.get_prev_data(year, month_name)

            average = total / count
            return str(round(average, 2))
        except:
            return "0"
