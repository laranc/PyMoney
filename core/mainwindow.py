# mainwindow.py
# imports
# tkinter
import tkinter as tk
from tkinter import ttk, Tk

# windows
import core.expensewindow as expwin
import core.incomewindow as incwin
import loginwindow as logwin
import core.registerwindow as regwin
import core.calculatorwindow as clcwin

import tools.database as db
import tools.datahandler as dh
import tools.errorhandler as eh
import tools.user as u

# other
import sqlite3 as sql
import os.path
import time


class main_window(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        # time data
        self.time_raw = time.strftime(
            "%a, %d %b %Y", time.localtime(time.time()))
        self.time_data = self.time_raw.split()
        # time data split:
        # day ==> 0
        # date ==> 1
        # month ==> 2
        # year ==> 3

        # get user id
        self.user_id = u.get_user_id()

        self.title("PyMoney")
        self.geometry("800x600")

        # title label
        self.title_label = ttk.Label(self, text="PyMoney")
        self.title_label.grid(row=0, column=4)

        # time label
        self.datetime_label = ttk.Label(
            self, text="" + self.time_raw)
        self.datetime_label.grid(row=0, column=5)

        # look for json file
        if os.path.exists(f"./json/{self.time_data[3]}.json"):
            print("data validated!")
        else:
            print("data file not present! creating new one!")
            dh.data_init(self.time_data[3], self.time_data[2], u.get_user_id())

        # window buttons
        self.expense_window_button = ttk.Button(
            self, text="Expenses", command=self.open_expense_window_EV)
        self.expense_window_button.grid(row=4, column=4)  # padx()

        self.income_window_button = ttk.Button(
            self, text="Income", command=self.open_income_window_EV)
        self.income_window_button.grid(row=5, column=4)

        self.calculator_window_button = ttk.Button(
            self, text="Calculator", command=self.open_calculator_window_EV)
        self.calculator_window_button.grid(row=6, column=4)

        # exit button
        self.exit_button = ttk.Button(
            self, text="Exit", command=lambda: self.destroy())
        self.exit_button.grid(row=7, column=4)

    # event functions
    def open_expense_window_EV(self) -> None:
        self.expense_window = expwin.expense_window(
            self.time_data, self.time_raw, self.user_id)

    def open_income_window_EV(self) -> None:
        self.income_window = incwin.income_window(
            self.time_data, self.time_raw, self.user_id)

    def open_calculator_window_EV(self) -> None:
        self.calculator_window_button = clcwin.calculator_window(
            self.time_data, self.time_raw, self.user_id)


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
