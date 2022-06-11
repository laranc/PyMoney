#loginwindow.py
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
        self.geometry("500x600") # adjust these sizes!!!

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
        self.password_text_widget = Entry(self, show="*", width=28) # password field WHY DOESNT IT CONFORM TO WINDOW?

        # position and insert text into input boxes
        self.firstname_text_widget.grid(row=2, column=4)
        self.lastname_text_widget.grid(row=3, column=4)
        self.age_text_widget.grid(row=4, column=4)
        self.dateofbirth_text_widget.grid(row=5, column=4)
        self.password_text_widget.grid(row=6, column=4)

        # submit button
        self.submit_new_user_button = ttk.Button(self, text="SUBMIT", command=self.validate_user_login_EV)

        # place button
        self.submit_new_user_button.grid(row=7, column=3)

    def validate_user_login_EV(self):
        conn = db.connect_to_database("user_data.db")
        cursor = db.create_database_cursor(conn)

        # get db data
        cursor.execute("""
            SELECT * FROM UserData;
        """)

        db_data = cursor.fetchall()

        # make user from database
        db_user = u.User(db_data[0], db_data[1], db_data[2], db_data[3], db_data[4])

        # get user from inputs
        user_firstname = self.firstname_text_widget.get(1.0, tk.END+"-1c")
        user_lastname = self.lastname_text_widget.get(1.0, tk.END+"-1c")
        user_age = int(self.age_text_widget.get(1.0, tk.END+"-1c")) # only value really needing validation
        user_dateofbirth = self.dateofbirth_text_widget.get(1.0, tk.END+"-1c")
        user_password = self.password_text_widget.get() # password specific

        # make user from input
        in_user = u.User(user_firstname, user_lastname, user_age, user_dateofbirth, user_password)

        # check data against db data
        if db_data[0] != in_user.firstname:
            messagebox.showerror(title="login failed!", message="Firstname invalid!")
        elif db_data[1] != in_user.lastname:
            messagebox.showerror(title="login failed!", message="Lastname invalid!")
        elif db_data[2] != in_user.age:
            messagebox.showerror(title="login failed!", message="Age invalid!")
        elif db_data[3] != in_user.dateofbirth:
            messagebox.showerror(title="login failed!", message="Date Of Birth invalid!")
        elif db_data[4] != in_user.password:
            messagebox.showerror(title="login failed!", message="Password invalid!")
        else: # input valid
            messagebox.showinfo(title="login succesfull", message="Login Succesfull")
            # close window
            self.destroy()
