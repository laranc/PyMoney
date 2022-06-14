# datahandler.py
import os
import json
import sqlite3 as sql
import tools.database as db
import tools.user as u


def create_datafile(year: str) -> None:
    # filepath = os.path.join(os.curdir, f"/json/{year}.json")
    # print(filepath)
    # assuming that file doesent exist, based on prequisites for function call:
    try:
        datafile_primary = open(f"./json/{year}.json", 'w')
    except:
        print("Couldnt make file!")
    
def new_data_entry():
    pass

def pull_data(year: str) -> None:
    datafile_primary = open(f"./json/{year}.json", 'r')
    pass

def push_new_data(time_data: list[str]):
    # create db connection
    conn = db.connect_to_database("user_data.db")
    cursor = db.create_database_cursor(conn)

    # get database data
    cursor.execute("SELECT * FROM UserData")
    db_data = cursor.fetchall()

    # collect time data

    json_expenses = []
    json_incomes = []

    # essentially the schmatic for what will be reresented in the json
    # i.e :


    # {

    # construct dictionary
    json_entry = { # need to add expense data here?
        "userid": f"",
        "totalmonthexpenses": f"",
        "totalmonthincome": f"",
        "expenses": f"{json_expenses}", # this wont push as expected!!!
        "incomes": f"{json_incomes}",
    }

    # } 