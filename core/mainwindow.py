# mainwindow.py
# imports
# tkinter
import tkinter as tk
from tkinter import ttk, Tk, PhotoImage

# windows
import core.expensewindow as expwin
import core.incomewindow as incwin
import core.calculatorwindow as clcwin

import tools.datahandler as dh
import tools.user as u

# other
import os.path
import time
import os


class main_window(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        # time data
        self.time_raw = time.strftime(
            "%a, %d %b %Y", time.localtime(time.time()))
        self.time_data = self.time_raw.split()
        # time data indices:
        # day ==> 0
        # date ==> 1
        # month ==> 2
        # year ==> 3

        # get user id
        self.user_details = u.get_user_details()

        self.title("PyMoney --> Main Interface")
        self.geometry("550x300")

        # set icon
        # working_dir = os.path.dirname(__file__)
        # print(f"WORKING DIR: {working_dir}")
        # self.iconphoto(False, PhotoImage(file="../icons/main.png")) WHY. DOESNT. THIS. WORK.

        # title labels
        self.title_label = ttk.Label(
            self, text=f"PyMoney Main Interface",
            font=("Lucidia 30 bold")
        )
        self.title_label.grid(row=0, column=0)

        self.user_label = ttk.Label(
            self, text=f" Logged In As: {self.user_details[1]} {self.user_details[2]}",
            font=("Lucidia 20 bold")
        )
        self.user_label.grid(row=1, column=0)

        # time label
        self.datetime_label = ttk.Label(
            self, text=f"Current Date: {self.time_raw}",
            font=("Lucidia 20 bold")
        )
        self.datetime_label.grid(row=2, column=0)

        # look for json file
        if os.path.exists(f"./json/{self.user_details[0]}.json"):
            print("data validated!")
        else:
            print("data file not present! creating new one!")
            dh.data_init(self.time_data[3], self.time_data[2])

        self.json_data, self.json_obj = dh.pull_data(
            self.time_data[3], self.time_data[2])

        # information labels
        self.current_balance_label = ttk.Label(
            self, text=f"Current Balance: ${self.current_balance_calc()}",
            font=("Roman 20 bold")
        )
        self.current_balance_label.grid(row=3, column=0)

        self.current_expenses_label = ttk.Label(
            self, text=f"Current monthly expenses: ${self.current_expenses_calc()}",
            font=("Roman 20 bold")
        )
        self.current_expenses_label.grid(row=4, column=0)

        # window buttons
        self.expense_window_button = ttk.Button(
            self, text="Expenses", command=self.open_expense_window_EV,
            width=20
        )
        self.expense_window_button.grid(row=5, column=0)  # padx()

        self.income_window_button = ttk.Button(
            self, text="Income", command=self.open_income_window_EV,
            width=20
        )
        self.income_window_button.grid(row=6, column=0)

        self.calculator_window_button = ttk.Button(
            self, text="Calculator", command=self.open_calculator_window_EV,
            width=20
        )
        self.calculator_window_button.grid(row=7, column=0)

        # exit button
        self.exit_button = ttk.Button(
            self, text="Exit", command=lambda: self.destroy(),
            width=20
        )
        self.exit_button.grid(row=8, column=0)

        print(f"MAIN WINDOW GRID: {self.grid_size()}")

    # label functions
    def current_balance_calc(self) -> str:
        try:
            income_value: int
            income_total = 0
            for key in self.json_data[2]:
                income_value = int(self.json_data[2][key])
                income_total += income_value

            expense_value: int
            expense_total = 0
            for key in self.json_data[1]:
                expense_value = int(self.json_data[1][key])
                expense_total += expense_value
            return str(int(income_total) - int(income_total))
        except:
            return "0"

    def current_expenses_calc(self) -> str:
        try:
            value: int
            total = 0
            for key in self.json_data[1]:
                value = int(self.json_data[1][key])
                total += value
            return str(value)
        except:
            return "0"
            # event functions

    def open_expense_window_EV(self) -> None:
        self.expense_window = expwin.expense_window(
            self.time_data, self.time_raw)

    def open_income_window_EV(self) -> None:
        self.income_window = incwin.income_window(
            self.time_data, self.time_raw)

    def open_calculator_window_EV(self) -> None:
        self.calculator_window_button = clcwin.calculator_window(
            self.time_data, self.time_raw)


# if __name__ == '__main__':
#     app = main_window()
#     app.mainloop()


#### OLD FUNCTIONS ####
# pass
# db functions
    # def verify_database(self) -> bool:
    #     if not os.path.exists("user_data.db"):
    #         try:
    #             db.create_database()
    #         except:
    #             raise eh.database_create_error()
    #     else:  # run initial query
    #         print(self.conn)
    #         print(self.cursor)
    #         self.cursor.execute("SELECT * FROM UserData")
    #         dbData = self.cursor.fetchall()
    #         print(dbData)
    #         return True

    # def verify_database_data(self, db_data) -> bool:
    #     if not db_data:  # bool checking here works to determine if list is empty or not
    #         print("Database Empty!")
    #         return False
    #     else:
    #         print("Database full!")
    #         return True
