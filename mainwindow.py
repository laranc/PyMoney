# mainwindow.py
# imports
# tkinter
import tkinter as tk
from tkinter import Tk
from tkinter import ttk

# windows
import core.expensewindow as expwin
import core.savingswindow as savwin
import core.loginwindow as logwin
import core.registerwindow as regwin

# db creator
import tools.database as db

# other
import sqlite3 as sql
import tools.errorhandler as eh
import os.path

class main_window(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        # windows
        global expense_window
        global saving_window
        global login_window
        global register_window
        
        # db constants
        global conn
        global cursor
        global db_data

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
            self.create_new_user() # delay mainwindow creation as much as possible!!!
        else: 
            self.login_user()


        self.title("PyMoney")
        self.geometry("800x600")

        self.expense_window_button = ttk.Button(self, text="Expenses", command=self.open_expense_window_EV)
        self.expense_window_button.grid(row=1, column=1) # padx()

    # db functions
    def verify_database(self) -> bool:
        if not os.path.exists("user_data.db"):
            try:
                db.create_database()
            except:
                raise eh.database_create_error()
        else: # run initial query
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
        if not db_data: # bool checking here works to determine if list is empty or not
            print("Database Empty!")
            return False
        else:
            print("Database full!")
            return True
    
    # user creation
    def create_new_user(self):
        self.register_window = regwin.register_window()
        pass

    # user login
    def login_user(self):
        self.login_window = logwin.login_window()
        pass

            
    # event functions
    def open_expense_window_EV(self) -> None:
        self.expense_window = expwin.expense_window()

    def open_savings_window_EV(self) -> None:
        self.savingsW_wndow = savwin.savings_window()

if __name__ == '__main__':
    app = main_window()
    app.mainloop()
