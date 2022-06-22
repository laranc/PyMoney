# mainwindow.py
# imports
# tkinter
import tkinter as tk
from tkinter import ttk, Tk

# windows
import core.expensewindow as expwin
import core.incomewindow as incwin
import core.loginwindow as logwin
import core.registerwindow as regwin
import core.calculatorwindow as clcwin

import tools.database as db
import tools.datahandler as dh
import tools.errorhandler as eh

# other
import sqlite3 as sql
import os.path
import time


class main_window(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        # db constants
        global conn
        global cursor
        global db_data

        # time data
        global time_raw
        global time_data

        # user
        global user_id

        ### DEBUG ###
        #self.purge_database(self.conn, self.cursor)

        # HUGE PROBLEM #
        ## THIS MUST BE FIXED ##
        # connect to db
        conn = db.connect_to_database("user_data.db") # create database
        print(conn)
        cursor = db.create_database_cursor(conn)
        print(cursor)

        # # verify database
        # self.verify_database()
        # get database data
        db_data = db.get_database_data(cursor)
        # verify database data
        if not db_data:
            self.create_new_user()  # delay mainwindow creation as much as possible!!!
        else:
            self.login_user()

    
        self.title("PyMoney")
        self.geometry("800x600")

        # title label
        self.title_label = ttk.Label(self, text="PyMoney")
        self.title_label.grid(row=0, column=4)

        # time label
        # get current time
        time_raw = time.strftime(
            "%a, %d %b %Y", time.localtime(time.time()))
        self.datetime_label = ttk.Label(
            self, text="" + time_raw)
        self.datetime_label.grid(row=0, column=5)

        # run time configuration
        self.configure_time_system()

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

        ### free resources ###
        db.disconnect_from_database(conn, cursor)

    ### DEBUG ###
    def purge_database(self, conn, cursor) -> None:
        cursor.execute("""
            DELETE FROM UserData;
        """)
        conn.commit()
        print("DEBUG:: Database Purged!!")

    # setup time system
    def configure_time_system(self) -> None:
        time_data = time_raw.split()
        day = time_data[0]
        date = time_data[1]
        month = time_data[2]
        year = time_data[3]

        # look for json file
        if not os.path.exists(f"./json/{year}.json"):
            print("data file not present! creating new one!")
            dh.create_datafile(year)  # by which case we need to push new data
        else:
            print("data validated!")  # by which case we need to pull the data

        print(time_data)

    # user creation
    def create_new_user(self):
        self.register_window = regwin.register_window() # window execution

    # user login
    def login_user(self):
        self.login_window = logwin.login_window()

    # event functions
    def open_expense_window_EV(self) -> None:
        self.expense_window = expwin.expense_window(
            time_data, time_raw)

    def open_income_window_EV(self) -> None:
        self.income_window = incwin.income_window(
            time_data, time_raw)

    def open_calculator_window_EV(self) -> None:
        self.calculator_window_button = clcwin.calculator_window(
            time_data, time_raw)


if __name__ == '__main__':
    app = main_window()
    app.mainloop()


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