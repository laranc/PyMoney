# registerwindow.py
import tkinter as tk
from tkinter import Tk
from tkinter import ttk
from tkinter import Text

class RegisterWindow(tk.Tk):
    def __init__(self) -> None:
        super().__init__()

        # set initial data
        self.title("Register Window")
        self.geometry("500x600")

        # title label
        self.titleLabel = ttk.Label(self, text="Welcome New User!")
        self.titleLabel.grid(row=1, column=5)

        # set the labels
        self.firstnameLabel = ttk.Label(self, text="Firstname:")
        self.lastnameLabel = ttk.Label(self, text="Lastname:")
        self.ageLabel = ttk.Label(self, text="Age:")
        self.dateofbirthLabel = ttk.Label(self, text="Date of Birth:")
        self.passwordLabel = ttk.Label(self, text="Password:")

        # position labels
        self.firstnameLabel.grid(row=3, column=3)
        self.lastnameLabel.grid(row=4, column=3)
        self.ageLabel.grid(row=4, column=3)
        self.dateofbirthLabel.grid(row=5, column=3)
        self.passwordLabel.grid(row=6, column=3)

        # set the input boxes 
        self.firstnameTextWidget = Text(self)
        self.firstnameTextWidgetPlacholder = "eg.John doe"
        self.firstnameTextWidget.grid(row=3, column=4)
        self.firstnameTextWidget.insert("end", self.firstnameTextWidgetPlacholder)
