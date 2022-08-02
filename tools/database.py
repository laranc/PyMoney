# database.py
import sqlite3 as sql


def create_database() -> None:
    # init connection
    try:
        connection = sql.connect("user_data.sqlite")
        cursor = connection.cursor()
        print("DEBUG: DB CONNECTION OPENED -- create_database()")
        try:
            # create initial table
            # TEXT type for date translates to 'YYYY-MM-DD HH:MM:SS.SSS' as date, no other date type exists
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS UserData
                (id INT(10) PRIMARY KEY, firstname TEXT, lastname TEXT, age INT, dateofbirth TEXT, password TEXT);
            ''')
            # commit to db
            connection.commit()
        except:
            print("ERR FAILED TO CREATE TABLE")
    except:
        print("ERR: FAILED TO CREATE DB")
    else:
        cursor.close()
        connection.close()
        print("DEBUG: DB CONNECTION CLOSED -- create_database()")


def fetch_data() -> list:
    try:
        connection = sql.connect("user_data.sqlite")
        cursor = connection.cursor()
        print("DEBUG: DB CONNECITON OPENED -- fetch_data()")
        try:
            cursor.execute("SELECT * FROM UserData;")
            db_data = cursor.fetchall()
            print(db_data)  # debug
            cursor.close()
            connection.close()
            print("DEBUG: DB CONNECTION CLOSED -- fetch_data()")
            return db_data
        except:
            print("ERR FAILED TO WRITE TO DATABASE")
            return []
    except:
        print("ERR FAILED TO CONNECT TO DATABASE")
        return []


def commit_data(command: str) -> None:
    try:
        connection = sql.connect("user_data.sqlite")
        cursor = connection.cursor()
        try:
            cursor.execute(command)
            connection.commit()
            print("DEBUG: DB CONNECTION OPENED -- commit_data()")
        except:
            print("ERR FAILED TO EXECUTE COMMAND: ", command)

        try:
            cursor.execute("SELECT * FROM UserData;")
            print(cursor.fetchall())
        except:
            print("ERR FAILED TO EXECUTE FETCH ALL")
    except:
        print("ERR FAILED TO COMMIT DATA")
    else:
        cursor.close()
        connection.close()
        print("DEBUG: DB CONNECTION CLOSED -- commit_data()")


def purge_database() -> None:
    try:
        connection = sql.connect("user_data.sqlite")
        cursor = connection.cursor()
        cursor.execute("DELETE FROM UserData;")
        connection.commit()
        print("Database Purged")
        cursor.close()
        connection.close()
    except:
        print("ERR FAILED TO PURGE DATABASE")
