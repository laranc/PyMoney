# registerwindow.py
import tkinter as tk
from tkinter import Tk
from tkinter import ttk

class RegisterWindow(tk.Tk):
    def __init__(self) -> None:
        super().__init__()

        # set initial data
        self.title("Register Window")
        self.geometry("500x600")