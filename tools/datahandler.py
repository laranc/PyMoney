# datahandler.py
import os
import json
import sqlite3 as sql
import tools.database as db
import tools.user as u


def create_datafile(year: str) -> None:
    # filepath = os.path.join(os.curdir, f"/json/{year}.json")
    # print(filepath)
    # assuming that file doesent exist, based on prequisites for function call:
    try:
        datafile_primary = open(f"./json/{year}.json", 'w')
    except:
        print("Couldnt make file!")

def pull_data(year: str) -> list[str]:
    if os.stat(f"./json/{year}.json").st_size == 0: # if no file exists
        return []
    else:
        datafile_primary = open(f"./json/{year}.json", 'r')
        data: dict = json.load(datafile_primary)
        month = data["month"] # organise data
        user_id = data["user-id"]
        total_expenses = data["total-monthly-expenses"]
        total_income = data["total-monthly-income"]
        local_expenses = {} # make dictionary for expense and income data
        local_incomes = {}
        for expense_name in data["expenses"]: # make dictionary
            local_expenses[f"{expense_name}"] = str(
                data["expenses"][expense_name])
        for income_name in data["incomes"]:
            local_incomes[f"{income_name}"] = str(data["incomes"][income_name])

        print(local_expenses)
        print(local_incomes)

        data_out: list[str] = [str(month), str(user_id), str(
            total_expenses), str(total_income), local_expenses, local_incomes]
        return data_out


def push_data(json_file_name: str, data_type: str, data_name: str, data_value: str) -> None:
    # loop through json
    # TO DO #
    data_file = open(f"./json/{json_file_name}.json", 'r+')
    #json_data = json.loads(json_file_name)
    json_data = pull_data(json_file_name)
    data_file.truncate(0)  # empty file
    json_data_dict = {}
    json_data_dict["month"] = json_data[0] # WATCH CASTING
    json_data_dict["user-id"] = json_data[1]
    json_data_dict["total-monthly-expenses"] = json_data[2]
    json_data_dict["total-monthly-income"] = json_data[3]
    json_data_dict["expenses"] = json_data[4]
    json_data_dict["incomes"] = json_data[5]

    # make new data
    if data_type == "expenses":
        json_data_dict["expenses"][data_name] = data_value
    else:
        json_data_dict["incomes"][data_name] = data_value

    print(f"DICT = {json_data_dict}")
    #json.dumps(json_data_dict, sort_keys=True, indent=4, separators=(',', ': ')) # doesnt quite work
    print(json.dumps(json_data_dict, indent=1))
    data_file.write(json.dumps(json_data_dict, indent=1)) # format json data
    #json.dump(json_dict_formatted, data_file)
    # print(json.load(data_file))


def remove_data(json_file_name: str, data_type: str, data_name: str, data_value: str) -> None:
    data_file = open(f"./json/{json_file_name}.json", 'r+')
    json_data = pull_data(json_file_name)
    data_file.truncate(0)
    json_data_dict = {}
    json_data_dict["month"] = json_data[0] # WATCH CASTING
    json_data_dict["user-id"] = json_data[1]
    json_data_dict["total-monthly-expenses"] = json_data[2]
    json_data_dict["total-monthly-income"] = json_data[3]
    json_data_dict["expenses"] = json_data[4]
    json_data_dict["incomes"] = json_data[5]

    if data_type == "expenses":
        del json_data_dict["expenses"][data_name]
    else:
        del json_data_dict["incomes"][data_name]

    print(f"DICT = {json_data_dict}")
    json.dump(json_data_dict, data_file)


def verify_month(json_file_name: str):
    json_data = pull_data(json_file_name)
    curr_month = int(json_data)