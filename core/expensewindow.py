# expensewindow.py
import tkinter as tk
from tkinter import Tk, Text
from tkinter import ttk
from tkinter import PhotoImage


# windows
#import core.dialogs.addexpensewindow as addexpwin

# database
import tools.datahandler as dh

class expense_window(tk.Tk):
    def __init__(self, time_data: list[str], time_raw: str) -> None:
        super().__init__()
    
        # get time
        self.time_data = time_data
        self.time_raw = time_raw

        # set window icon
        # self.win_icon = PhotoImage(file='./icons/expense-icon.png')
        # print(self.win_icon) # not working, pyimage 1?
        # self.iconphoto(False, self.win_icon)


        # set initial data
        self.title("Expense Window")
        self.geometry("500x600")

        # title label
        self.title_label = ttk.Label(
            self, text="Expense for " + self.time_raw)
        self.title_label.grid(row=0, column=4)

        # buttons
        self.add_expense_window_button = ttk.Button(
            self, text="Add Expense", command=self.open_add_expense_window_EV)
        self.add_expense_window_button.grid(row=4, column=4)

        # table frame
        expenses_table_frame = ttk.Frame(
            master=self, relief=tk.SOLID, borderwidth=2)

        
        self.display_data()
        # for x in range(2):
        #     for y in range(2):
        #         label = ttk.Label(self, text="daasdasdasd")
        #         label.grid(row=x, column=y)

        expenses_table_frame.grid(row=6, column=5)
        expenses_table = ttk.Label(self, text="Placeholder")
        expenses_table.grid(row=0, column=1)

        # add expenses frame
        add_expenses_frame = ttk.Frame(
            master=self, relief=tk.SOLID, borderwidth=2)
        add_expenses_frame.grid(row=10, column=1)

        # labels
        self.name_label = ttk.Label(add_expenses_frame, text="Expense Name")
        self.name_label.grid(row=4, column=4)

        self.value_label = ttk.Label(add_expenses_frame, text="Expense Value")
        self.value_label.grid(row=5, column=4)

        # text input
        self.name_input = Text(add_expenses_frame, height=1, width=20)
        self.name_input.grid(row=4, column=5)

        self.value_input = Text(add_expenses_frame, height=1, width=20)
        self.value_input.grid(row=5, column=5)

        # submit data
        self.add_new_expense = ttk.Button(self, text="Add New Expense", command=self.add_new_expense_EV)
        
        
        # remove expenses frame


    def display_data(self) -> None:
        # get json data
        json_data: list[str] = dh.pull_data(self.time_data[3])
        if len(json_data) == 0: # file empty
            pass
        else: # file is full
            pass
        
    def add_new_expense_EV(self) -> None:

        name = self.name_input.get(1.0, tk.END+"-1c")
        value = self.value_input.get(1.0, tk.END+"-1c")

        dh.push_new_data()
        self.display_data()

    # def open_add_expense_window_EV(self) -> None:
    #     self.add_expense_window = addexpwin.add_expense_window(
    #         self.time_data, self.time_raw)
