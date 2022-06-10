# database.py
import sqlite3 as sql
import errorhandler as eh

def createDatabase():
    # init connection
    try:
        conn = sql.connect("user_data.db")
    except:
        print("ERR: FAILED TO CREATE DB")
        raise eh.databaseCreateError() # custom error handling

    # create cursor object
    cursor = conn.cursor()

    # create initial table
    # TEXT type for date translates to 'YYYY-MM-DD HH:MM:SS.SSS' as date, no other date type exists
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS UserData
        (firstname TEXT, lastname TEXT, age INT, dateofbirth TEXT, password TEXT) 

    ''')

    # commit to db
    conn.commit()

    # free resources
    cursor.close()
    conn.close()

def connectToDatabase(db_name: str) -> sql.Connection: # TESTING seeing if a constant connection can work
    try:
        conn: sql.Connection = sql.connect(db_name)
        return conn
    except:
        raise eh.databaseConnectionError()

def createDatabaseCursor(conn: sql.Connection) -> sql.Cursor:
    try:
        cursor = conn.cursor()
        return cursor
    except:
        print("ERR FAILED TO CREATE CURSOR")

def disconnectFromDatabase(conn: sql.Connection, cursor: sql.Cursor):
    try:
        cursor.close()
        conn.close()
    except:
        print("ERR FAILED TO CLOSE CURSOR AND CONNECTION")


