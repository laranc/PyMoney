# datahandler.py
from io import TextIOWrapper
import os
import json
import sqlite3 as sql
import tools.database as db
import tools.user as u


def create_datafile(year: str, month: str, user_id: int) -> None:
    try:
        datafile_primary = open(f"./json/{year}.json", 'w')
    except:
        print("Couldnt make file!")


def data_init(year: str, month: str, user_id: int) -> TextIOWrapper:
    data_file = open(f"./json/{year}.json", 'w')
    json_data: list[str] = {"user-id": user_id, "month": month, "total-monthly-expenses": "",
                            "total-monthly-income": "", "expenses": {'': ''}, "incomes": {'': ''}}
    data_file.write(json.dumps(json_data, indent=1))
    return data_file


def pull_data(year: str) -> list[str]:
    if os.stat(f"./json/{year}.json").st_size == 0:  # if no file exists
        return []
    else:
        data_file = open(f"./json/{year}.json", 'r')
        data: list[dict] = json.load(data_file)
        json_obj: int
        for i in range(len(data)):
            if data[i]["user-id"] == u.get_user_id():
                json_obj = i

        user_id = data[json_obj]["user-id"]
        month = data[json_obj]["month"]  # organise data
        total_expenses = data[json_obj]["total-monthly-expenses"]
        total_income = data[json_obj]["total-monthly-income"]
        local_expenses = {}  # make dictionary for expense and income data
        local_incomes = {}
        for expense_name in data["expenses"]:  # make dictionary
            local_expenses[f"{expense_name}"] = str(
                data[json_obj]["expenses"][expense_name])
        for income_name in data[json_obj]["incomes"]:
            local_incomes[f"{income_name}"] = str(
                data[json_obj]["incomes"][income_name])

        print(local_expenses)
        print(local_incomes)

        data_out: list[str] = [str(user_id), str(month), str(
            total_expenses), str(total_income), local_expenses, local_incomes]
        return data_out, json_obj


def push_data(year: str, month: str, data_type: str, data_name: str, data_value: str) -> None:
    if os.stat(f"./json/{year}.json").st_size == 0:
        data_file = data_init(year, month, u.get_user_id)
    else:
        data_file = open(f"./json/{year}.json", 'r+')

    json_data_raw: list[dict] = json.load(data_file)
    json_obj_data, json_obj = pull_data(year)

    json_data_dict = {}
    json_data_dict["user-id"] = json_obj_data[0]
    json_data_dict["month"] = json_obj_data[1]  # WATCH CASTING
    json_data_dict["total-monthly-expenses"] = json_obj_data[2]
    json_data_dict["total-monthly-income"] = json_obj_data[3]
    json_data_dict["expenses"] = json_obj_data[4]
    json_data_dict["incomes"] = json_obj_data[5]

    # make new data
    if data_type == "expenses":
        json_data_dict["expenses"][data_name] = data_value
    else:
        json_data_dict["incomes"][data_name] = data_value

    print(f"DICT = {json_data_dict}")

    data_file.truncate(0)  # empty file
    json_data_out: list[dict]
    for i in json_data_raw:
        if i == json_obj:
            json_data_out[i] = json_data_dict
        else:
            json_data_out[i] = i

    # json.dumps(json_data_dict, sort_keys=True, indent=4, separators=(',', ': ')) # doesnt quite work
    print(json.dumps(json_data_out, indent=4))
    data_file.write(json.dumps(json_data_out, indent=4))  # format json data
    # json.dump(json_dict_formatted, data_file)
    # print(json.load(data_file))


def remove_data(json_file_name: str, data_type: str, data_name: str, data_value: str) -> None:
    data_file = open(f"./json/{json_file_name}.json", 'r+')
    json_data_raw: list[dict] = json.load(data_file)
    json_obj_data, json_obj = pull_data(json_file_name)

    json_data_dict = {}
    json_data_dict["month"] = json_obj_data[0]  # WATCH CASTING
    json_data_dict["user-id"] = json_obj_data[1]
    json_data_dict["total-monthly-expenses"] = json_obj_data[2]
    json_data_dict["total-monthly-income"] = json_obj_data[3]
    json_data_dict["expenses"] = json_obj_data[4]
    json_data_dict["incomes"] = json_obj_data[5]

    if data_type == "expenses":
        del json_data_dict["expenses"][data_name]
    else:
        del json_data_dict["incomes"][data_name]

    print(f"DICT = {json_data_dict}")

    data_file.truncate(0)
    json_data_out: list[dict]
    for i in json_data_raw:
        if i == json_obj:
            json_data_out[i] = json_data_dict
        else:
            json_data_out[i] = i

    print(json.dumps(json_data_out, indent=4))
    data_file.write(json.dumps(json_data_out, indent=4))


def verify_month(json_file_name: str):
    json_data = pull_data(json_file_name)
    curr_month = int(json_data)
