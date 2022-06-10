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

class MainWindow(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        # windows
        global expenseWindow
        global savingWindow
        global loginWindow
        global registerwindow
        
        # db constants
        global conn
        global cursor
        global dbData

        # connect to db
        self.conn = db.connectToDatabase("user_data.db")
        print(self.conn)
        self.cursor = db.createDatabaseCursor(self.conn)
        print(self.cursor)

        # verify database
        self.verifyDatabase()
        # get database data
        self.dbData = self.getDatabaseData()
        # verify database data
        if self.verifyDatabaseData(self.dbData) is False:
            self.createNewUser() # delay mainwindow creation as much as possible!!!
        else: 
            self.loginUser()


        self.title("PyMoney")
        self.geometry("800x600")

        self.expenseWindowButton = ttk.Button(self, text="Expenses", command=self.OpenExpenseWindow_EV)
        self.expenseWindowButton.grid(row=1, column=1) # padx()

    # db functions
    def verifyDatabase(self) -> bool:
        if not os.path.exists("user_data.db"):
            try:
                db.createDatabase()
            except:
                raise eh.databaseCreateError()
        else: # run initial query
            print(self.conn)
            print(self.cursor)
            self.cursor.execute("SELECT * FROM UserData")
            dbData = self.cursor.fetchall()
            print(dbData)
            return True

    def getDatabaseData(self) -> list:
        try:
            self.cursor.execute("SELECT * FROM UserData")
            dbData = self.cursor.fetchall()
            return dbData
        except:
            raise eh.databaseQueryFailed()

    def verifyDatabaseData(self, dbData) -> bool:
        if not dbData: # bool checking here works to determine if list is empty or not
            print("Database Empty!")
            return False
        else:
            print("Database full!")
            return True
    
    # user creation
    def createNewUser(self):
        self.registerWindow = regwin.RegisterWindow()
        pass

    # user login
    def loginUser(self):
        self.loginWindow = logwin.LoginWindow()
        pass

            
    # event functions
    def OpenExpenseWindow_EV(self) -> None:
        self.expenseWindow = expwin.ExpenseWindow()

    def OpenSavingsWindow_EV(self) -> None:
        self.savingsWindow = savwin.SavingsWindow()

if __name__ == '__main__':
    app = MainWindow()
    app.mainloop()
