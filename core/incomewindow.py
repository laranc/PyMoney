# savingswindow.py
import tkinter as tk
from tkinter import ttk, Tk, Text, PhotoImage

# database
import tools.datahandler as dh


class income_window(tk.Tk):
    def __init__(self, time_data: list[str], time_raw: str, user_id: int) -> None:
        super().__init__()
        # get user id
        self.user_id = user_id

        # get time
        self.time_data = time_data
        self.time_raw = time_raw

        # set window icon
        # self.win_icon = PhotoImage(file="./icons/income-icon.png")
        # print(self.win_icon) # not working, pyimage 1?
        # self.iconphoto(False, self.win_icon)

        # set initial data
        self.title("Income Window")
        self.geometry("500x600")

        # title label
        self.title_label = ttk.Label(
            self, text="Income for " + time_raw)
        self.title_label.grid(row=0, column=4)

        # table frame
        self.income_table = ttk.Frame(
            master=self, relief=tk.SOLID, borderwidth=2)
        self.income_table.grid(row=6, column=1)

        self.income_table.income_table_name_label = ttk.Label(
            self.income_table, text="Name")
        self.income_table.income_table_name_label.grid(row=0, column=0)

        self.income_table.income_table_value_label = ttk.Label(
            self.income_table, text="Value")
        self.income_table.income_table_value_label.grid(row=0, column=1)

        self.display_data()

        # add income frame
        self.add_income_frame = ttk.Frame(
            master=self, relief=tk.SOLID, borderwidth=2)
        self.add_income_frame.grid(row=10, column=1)

        # labels
        self.add_income_frame.add_income_name_label = ttk.Label(
            self.add_income_frame, text="Income Name")
        self.add_income_frame.add_income_name_label.grid(row=4, column=4)

        self.add_income_frame.add_income_value_label = ttk.Label(
            self.add_income_frame, text="Income Value")
        self.add_income_frame.add_income_value_label.grid(row=5, column=4)

        # text input
        self.add_income_frame.add_income_name_input = Text(
            self.add_income_frame, height=1, width=20)
        self.add_income_frame.add_income_name_input.grid(row=4, column=5)

        self.add_income_frame.add_income_value_input = Text(
            self.add_income_frame, height=1, width=20)
        self.add_income_frame.add_income_value_input.grid(row=5, column=5)

        # submit data
        self.add_new_income_button = ttk.Button(
            self, text="Add New Income", command=self.add_new_income_EV)
        self.add_new_income_button.grid(row=11, column=1)

        # remove income frame
        self.remove_income_frame = ttk.Frame(
            master=self, relief=tk.SOLID, borderwidth=2)
        self.remove_income_frame.grid(row=10, column=4)

        self.remove_income_frame.remove_income_name_label = ttk.Label(
            self.remove_income_frame, text="Income Name")
        self.remove_income_frame.remove_income_name_label.grid(row=4, column=4)

        self.remove_income_frame.remove_income_value_label = ttk.Label(
            self.remove_income_frame, text="Income Value")
        self.remove_income_frame.remove_income_value_label.grid(
            row=5, column=4)

        # text input
        self.remove_income_frame.remove_income_name_input = Text(
            self.remove_income_frame, height=1, width=20)
        self.remove_income_frame.remove_income_name_input.grid(row=4, column=5)

        self.remove_income_frame.remove_income_value_input = Text(
            self.remove_income_frame, height=1, width=20)
        self.remove_income_frame.remove_income_value_input.grid(
            row=5, column=5)

        # submit data
        self.remove_new_income_button = ttk.Button(
            self, text="Remove Income", command=self.remove_income_EV)
        self.remove_new_income_button.grid(row=11, column=4)

    def display_data(self) -> None:
        # get json data
        json_data: list[str] = dh.pull_data(self.time_data[3])
        print(f"DATA = {json_data}")
        if len(json_data) == 0:  # file empty
            pass
        else:  # file is full
            self.income_table.destroy()
            self.income_table = ttk.Frame(
                master=self, relief=tk.SOLID, borderwidth=2)
            self.income_table.grid(row=6, column=1)
            row = 1
            for key in json_data[5]:
                name = ttk.Label(self.income_table, text=f"{key}")
                name.grid(row=row, column=0)
                value = ttk.Label(self.income_table,
                                  text=f"{json_data[5][key]}")
                value.grid(row=row, column=1)
                row += 1

    def add_new_income_EV(self) -> None:
        name = self.add_income_frame.add_income_name_input.get(
            1.0, tk.END+'-1c')
        value = self.add_income_frame.add_income_value_input.get(
            1.0, tk.END+'-1c')

        dh.push_data(self.time_data[3], "incomes", name, value)
        self.display_data()

    def remove_income_EV(self) -> None:
        name = self.remove_income_frame.remove_income_name_input.get(
            1.0, tk.END+'-1c')
        value = self.remove_income_frame.remove_income_value_input.get(
            1.0, tk.END+'-1c')

        dh.remove_data(self.time_data[3], "incomes", name, value)
        self.display_data()
