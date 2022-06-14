# mainwindow.py
# imports
# tkinter
import tkinter as tk
from tkinter import Tk
from tkinter import ttk

# windows
import core.expensewindow as expwin
import core.incomewindow as incwin
import core.loginwindow as logwin
import core.registerwindow as regwin

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
        # windows
        global expense_window
        global income_window
        global login_window
        global register_window

        # db constants
        global conn
        global cursor
        global db_data

        # time data
        global time_raw
        global time_data

        ### DEBUG ###
        #self.purge_database(self.conn, self.cursor) 

         # HUGE PROBLEM # 
        ## THIS MUST BE FIXED ##
        # connect to db
        self.conn = db.connect_to_database("user_data.db")
        print(self.conn)
        self.cursor = db.create_database_cursor(self.conn)
        print(self.cursor)


        # verify database
        self.verify_database()
        # get database data
        self.dbData = self.get_database_data()
        # verify database data
        if self.verify_database_data(self.dbData) is False:
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
        self.time_raw = time.strftime("%a, %d %b %Y", time.localtime(time.time()))
        self.datetime_label = ttk.Label(
            self, text="" + self.time_raw)
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

        # exit button
        self.exit_button = ttk.Button(
            self, text="Exit", command=lambda: self.destroy())
        self.exit_button.grid(row=6, column=4)

        # grid items

        ### free resources ###
        db.disconnect_from_database(self.conn, self.cursor)

    ### DEBUG ###
    def purge_database(self, conn, cursor) -> None:
        cursor.execute("""
            DELETE FROM UserData;
        """)
        conn.commit()
        print("DEBUG:: Database Purged!!")

    # setup time system
    def configure_time_system(self) -> None:
        self.time_data = self.time_raw.split()
        day = self.time_data[0]
        date = self.time_data[1]
        month = self.time_data[2]
        year = self.time_data[3]

        # look for json file
        if not os.path.exists(f"./json/{year}.json"):
            print("data file not present! creating new one!")
            dh.create_datafile(year) # by which case we need to push new data
        else:
            print("data validated!") # by which case we need to pull the data

        print(self.time_data)

    # db functions
    def verify_database(self) -> bool:
        if not os.path.exists("user_data.db"):
            try:
                db.create_database()
            except:
                raise eh.database_create_error()
        else:  # run initial query
            print(self.conn)
            print(self.cursor)
            self.cursor.execute("SELECT * FROM UserData")
            dbData = self.cursor.fetchall()
            print(dbData)
            return True

    def get_database_data(self) -> list:
        try:
            self.cursor.execute("SELECT * FROM UserData")
            dbData = self.cursor.fetchall()
            return dbData
        except:
            raise eh.database_query_dailed()

    def verify_database_data(self, db_data) -> bool:
        if not db_data:  # bool checking here works to determine if list is empty or not
            print("Database Empty!")
            return False
        else:
            print("Database full!")
            return True

    # user creation
    def create_new_user(self):
        self.register_window = regwin.register_window()        
        pass  # window execution

    # user login
    def login_user(self):
        self.login_window = logwin.login_window()
        pass

    # event functions
    def open_expense_window_EV(self) -> None:
        self.expense_window = expwin.expense_window(self.time_data, self.time_raw)

    def open_income_window_EV(self) -> None:
        self.income_window = incwin.income_window()


if __name__ == '__main__':
    app = main_window()
    app.mainloop()
