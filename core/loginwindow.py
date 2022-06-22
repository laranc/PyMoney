# loginwindow.py
import tkinter as tk
from tkinter import Tk
from tkinter import ttk
from tkinter import Text
from tkinter import Entry
from tkinter import messagebox

import tools.database as db
import tools.user as u


class login_window(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        # set initial data
        self.title("Login Window")
        self.geometry("500x600")

        # set initial data
        self.title("Register Window")
        self.geometry("500x600")  # adjust these sizes!!!

        # title label
        self.title_label = ttk.Label(self, text="Welcome Back Existing User!")
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

        # set the input boxes
        self.firstname_text_widget = Text(self, height=1, width=20)
        self.lastname_text_widget = Text(self, height=1, widt=20)
        self.age_text_widget = Text(self, height=1, width=20)
        self.dateofbirth_text_widget = Text(self, height=1, width=20)
        # password field WHY DOESNT IT CONFORM TO WINDOW?
        self.password_text_widget = Entry(self, show="*", width=28)

        # position and insert text into input boxes
        self.firstname_text_widget.grid(row=2, column=4)
        self.lastname_text_widget.grid(row=3, column=4)
        self.age_text_widget.grid(row=4, column=4)
        self.dateofbirth_text_widget.grid(row=5, column=4)
        self.password_text_widget.grid(row=6, column=4)

        # submit button
        self.submit_new_user_button = ttk.Button(
            self, text="SUBMIT", command=self.validate_user_login_EV)

        # place button
        self.submit_new_user_button.grid(row=7, column=3)

    def validate_user_login_EV(self):
        conn = db.connect_to_database()
        cursor = db.create_database_cursor(conn)

        # get db data
        cursor.execute("""
            SELECT * FROM UserData;
        """)

        db_data = cursor.fetchall()

        # get user from inputs
        in_user_firstname = self.firstname_text_widget.get(1.0, tk.END+"-1c")
        in_user_lastname = self.lastname_text_widget.get(1.0, tk.END+"-1c")
        in_user_age = int(self.age_text_widget.get(1.0, tk.END+"-1c"))
        in_user_dateofbirth = self.dateofbirth_text_widget.get(
            1.0, tk.END+"-1c")
        in_user_password = self.password_text_widget.get()  # password specific

        login_check = False
        # check user against database
        for i in db_data:
            if i[1] == in_user_firstname and i[2] == in_user_lastname and i[3] == in_user_age and i[4] == in_user_dateofbirth and i[5] == in_user_password:
                u.current_user_id = i[0]
                messagebox.showinfo(title="Login Successfull",
                                    message="Login Successfull")
                login_check = True
                break

            if not(login_check):
                messagebox.showerror(title="Login Failed",
                                     message="Invalid credential")
            # free db resources
            db.disconnect_from_database(conn, cursor)

            # close window
            self.destroy()
