# database.py
import sqlite3 as sql
import tools.errorhandler as eh


def create_database() -> None:
    # init connection
    try:
        conn = sql.connect("user_data.sqlite")
    except:
        print("ERR: FAILED TO CREATE DB")
        raise eh.database_create_error()  # custom error handling

    # create cursor object
    cursor = conn.cursor()

    # create initial table
    # TEXT type for date translates to 'YYYY-MM-DD HH:MM:SS.SSS' as date, no other date type exists
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS UserData
        (id INT(10) PRIMARY KEY, firstname TEXT, lastname TEXT, age INT, dateofbirth TEXT, password TEXT);
    ''')

    # commit to db
    conn.commit()

    # free resources
    cursor.close()
    conn.close()


# TESTING seeing if a constant connection can work
def connect_to_database() -> sql.Connection:
    try:
        conn: sql.Connection = sql.connect("user_data.sqlite")
        return conn
    except:
        raise eh.database_connection_error()


def create_database_cursor(conn: sql.Connection) -> sql.Cursor:
    try:
        cursor = conn.cursor()
        return cursor
    except:
        print("ERR FAILED TO CREATE CURSOR")


def disconnect_from_database(conn: sql.Connection, cursor: sql.Cursor) -> None:
    try:
        cursor.close()
        conn.close()
    except:
        print("ERR FAILED TO CLOSE CURSOR AND CONNECTION")


def get_database_data(cursor) -> list:
    try:
        cursor.execute("SELECT * FROM UserData")
        db_data = cursor.fetchall()
        print(db_data)  # debug
        return db_data
    except:
        raise eh.database_query_failed()


def purge_database(conn: sql.Connection, cursor: sql.Cursor) -> None:
    try:
        cursor.execute("DELETE FROM UserData")
        conn.commit()
        print("Database Purged")
    except:
        print("ERR FAILED TO PURGE DATABASE")
