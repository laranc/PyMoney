# registerwindow.py
import tkinter as tk
from tkinter import Tk
from tkinter import ttk
from tkinter import Text

class register_window(tk.Tk):
    def __init__(self) -> None:
        super().__init__()

        # set initial data
        self.title("Register Window")
        self.geometry("500x600")

        # title label
        self.title_label = ttk.Label(self, text="Welcome New User!")
        self.title_label.grid(row=1, column=5)

        # set the labels
        self.firstname_label = ttk.Label(self, text="Firstname:")
        self.lastname_label = ttk.Label(self, text="Lastname:")
        self.age_label = ttk.Label(self, text="Age:")
        self.dateofbirth_label = ttk.Label(self, text="Date of Birth:")
        self.password_label = ttk.Label(self, text="Password:")

        # position labels
        self.firstname_label.grid(row=3, column=3)
        self.lastname_label.grid(row=4, column=3)
        self.age_label.grid(row=4, column=3)
        self.dateofbirth_label.grid(row=5, column=3)
        self.password_label.grid(row=6, column=3)

        # set the input boxes 
        self.firstname_text_widget = Text(self)
        self.firstname_text_widget_placeholder = "eg.John doe"
        self.firstname_text_widget.grid(row=3, column=4)
        self.firstname_text_widget.insert("end", self.firstname_text_widget_placeholder)
