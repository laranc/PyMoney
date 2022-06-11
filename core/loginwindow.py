#loginwindow.py
import tkinter as tk
from tkinter import Tk
from tkinter import ttk

class login_window(tk.Tk):
    def __init__(self) -> None:
        super().__init__()

        # set initial data
        self.title("Login Window")
        self.geometry("500x600")