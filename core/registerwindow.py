# registerwindow.py
import tkinter as tk
from tkinter import Tk, ttk, Text, Entry, messagebox

import tools.database as db
import tools.user as u

import core.mainwindow as maiwin


class register_window(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        # set initial data
        self.title("Register Window")
        self.geometry("500x600")  # adjust these sizes!!!

        # title label
        self.title_label = ttk.Label(self, text="Welcome New User!")
        self.title_label.grid(row=0, column=3)

        # set the labels
        self.firstname_label = ttk.Label(self, text="Firstname:")
        self.lastname_label = ttk.Label(self, text="Lastname:")
        self.age_label = ttk.Label(self, text="Age:")
        self.dateofbirth_label = ttk.Label(self, text="Date of Birth:")
        self.password_label = ttk.Label(self, text="Password:")

        # position labels
        self.firstname_label.grid(row=2, column=3)
        self.lastname_label.grid(row=3, column=3)
        self.age_label.grid(row=4, column=3)
        self.dateofbirth_label.grid(row=5, column=3)
        self.password_label.grid(row=6, column=3)

        # some testing ### grid is a lot superior
        # self.firstname_label.pack(padx=10, side=tk.BOTTOM)
        # self.lastname_label.pack(padx=10, side=tk.BOTTOM)
        # self.age_label.pack(side=tk.BOTTOM)
        # self.dateofbirth_label.pack(side=tk.BOTTOM)
        # self.password_label.pack(side=tk.BOTTOM)

        # set the input boxes
        self.firstname_text_widget = Text(self, height=1, width=20)
        self.lastname_text_widget = Text(self, height=1, widt=20)
        self.age_text_widget = Text(self, height=1, width=20)
        self.dateofbirth_text_widget = Text(self, height=1, width=20)
        # password field WHY DOESNT IT CONFORM TO WINDOW?
        self.password_text_widget = Entry(self, show="*", width=28)

        # define input box placeholders
        self.firstname_text_widget_placeholder = "e.g John"
        self.lastname_text_widget_placeholder = "e.g Doe"
        self.age_text_widget_placeholder = "e.g 27"
        self.dateofbirth_text_widget_placeholder = "21/12/1968"
        self.password_text_widget_placeholder = "e.g ILikeCoding45"

        # position and insert text into input boxes
        self.firstname_text_widget.grid(row=2, column=4)
        self.firstname_text_widget.insert(
            "end", self.firstname_text_widget_placeholder)
        self.lastname_text_widget.grid(row=3, column=4)
        self.lastname_text_widget.insert(
            "end", self.lastname_text_widget_placeholder)
        self.age_text_widget.grid(row=4, column=4)
        self.age_text_widget.insert("end", self.age_text_widget_placeholder)
        self.dateofbirth_text_widget.grid(row=5, column=4)
        self.dateofbirth_text_widget.insert(
            "end", self.dateofbirth_text_widget_placeholder)
        self.password_text_widget.grid(row=6, column=4)
        self.password_text_widget.insert(
            "end", self.password_text_widget_placeholder)

        # submit button
        self.submit_new_user_button = ttk.Button(
            self, text="SUBMIT", command=self.submit_new_user_EV)

        # place button
        self.submit_new_user_button.grid(row=7, column=3)

    def verify_user_input(self) -> None:
        try:
            # only value really needing validation
            user_age = int(self.age_text_widget.get(1.0, tk.END + "-1c"))
        except:
            messagebox.showerror(
                title="ERROR", message="Input must be valid!!")

    def submit_new_user_EV(self) -> None:

        # verify user input
        self.verify_user_input()

        conn = db.connect_to_database()
        cursor = db.create_database_cursor(conn)

        db_data = cursor.fetchall()

        # make user from info
        user_firstname = self.firstname_text_widget.get(1.0, tk.END+"-1c")
        user_lastname = self.lastname_text_widget.get(1.0, tk.END+"-1c")
        # only value really needing validation
        user_age = int(self.age_text_widget.get(1.0, tk.END+"-1c"))
        user_dateofbirth = self.dateofbirth_text_widget.get(1.0, tk.END+"-1c")
        user_password = self.password_text_widget.get()  # password specific

        if not db_data:
            u.set_user_id(0)
        else:
            u.set_user_id(len(db_data) - 1)

        user = u.User(u.get_user_id(), user_firstname, user_lastname, user_age,
                      user_dateofbirth, user_password)

        # add data to database # NEEDS FIXING
        cursor.execute(f"""
            INSERT OR IGNORE INTO UserData(id, firstname, lastname, age, dateofbirth, password)
            VALUES('{u.get_user_id()}', '{user.firstname}', '{user.lastname}', {user.age}, '{user.dateofbirth}', '{user.password}')
        """)

        conn.commit()

        ### DEBUG ###
        # print data in db to confirm
        cursor.execute("""
            SELECT * FROM UserData
        """)
        print(cursor.fetchall())

        # free db resources
        db.disconnect_from_database(conn, cursor)

        # close window
        self.destroy()
