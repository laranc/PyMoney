# database.py
import sqlite3

# init connection
conn = sqlite3.connect("user_data.db")

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
