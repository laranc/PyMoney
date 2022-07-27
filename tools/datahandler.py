# datahandler.py
from io import TextIOWrapper
import os
import json
import sqlite3 as sql
import tools.database as db
import tools.user as u


def data_init(year: str, month: str) -> None:
    data_file = open(f"./json/{u.get_user_details()[0]}.json", 'w')
    json_data = {
        year: [
                {
                    "month": month,
                    "expenses": {},
                    "incomes": {}
                }
        ]
    }

    data_file.truncate(0)
    data_file.write(json.dumps(json_data, indent=4))
    print("Template data added to empty file")


def check_data(year: str, month: str, cont: bool) -> bool:
    if os.stat(f"./json/{u.get_user_details()[0]}.json").st_size == 0:
        data_init(year, month)
        return False
    else:
        data_file = open(f"./json/{u.get_user_details()[0]}.json", 'r')
        data = json.load(data_file)
        print(f"DATA[ARRAY]: {data}")
        data_present = False
        for i in data[year]:
            # print(f"DICT [i]: {i}")
            # print(f"DATA [i], [month]: {i['user-id']}, {i['month']}")
            # print(f"USER-ID: {u.get_user_id()}")
            if i["month"] == month:
                data_present = True

        if not(data_present):
            if cont:
                json_data = {
                    year: [
                            {
                                "month": month,
                                "expenses": {},
                                "incomes": {}
                            }
                    ]
                }

                data.append(json_data)
                data_file.close()
                data_file = open(f"./json/{u.get_user_details()[0]}.json", 'w')
                print(f"CEREALISED JSON: {json.dumps(data, indent=4)}")
                data_file.write(json.dumps(data, indent=4))
                print("Template data added to existing file")
                return False
            else:
                print("JSON object for corresponding user not found")
                return False
        else:
            print("JSON object for current user found")
            return True


def pull_data(year: str, month: str) -> list[str]:
    if not(check_data(year, month, False)):
        return [], None
    else:
        data_file = open(f"./json/{u.get_user_details()[0]}.json", 'r')
        data = json.load(data_file)
        print(data)
        json_obj: int
        for i in data[year]:
            print(i)
            if i["month"] == month:
                json_obj = data[year].index(i)

        month = data[year][json_obj]["month"]  # organise data
        local_expenses = {}  # make dictionary for expense and income data
        local_incomes = {}
        for expense_name in data[year][json_obj]["expenses"]:  # make dictionary
            local_expenses[expense_name] = str(
                data[year][json_obj]["expenses"][expense_name])
        for income_name in data[year][json_obj]["incomes"]:
            local_incomes[income_name] = str(
                data[year][json_obj]["incomes"][income_name])

        print(local_expenses)
        print(local_incomes)

        data_out: list[str] = [str(month), local_expenses, local_incomes]
        return data_out, json_obj


def push_data(year: str, month: str, data_type: str, data_name: str, data_value: str) -> None:
    check_data(year, month, True)

    data_file = open(f"./json/{u.get_user_details()[0]}.json", 'r')

    json_data_raw = json.load(data_file)
    json_obj_data, json_obj = pull_data(year, month)

    json_data_dict = {}
    json_data_dict["month"] = json_obj_data[0]  # WATCH CASTING
    json_data_dict["expenses"] = json_obj_data[1]
    json_data_dict["incomes"] = json_obj_data[2]

    # make new data
    json_data_dict[data_type][data_name] = data_value

    print(f"DICT = {json_data_dict}")

    data_file.close()
    data_file = open(
        f"./json/{u.get_user_details()[0]}.json", 'w')  # empty file
    json_data_out = json_data_raw
    for i in range(len(json_data_raw[year])):
        if i == json_obj:
            json_data_out[year][i] = json_data_dict

    print(f"JSON DATA OUT: {json_data_out}")
    # json.dumps(json_data_dict, sort_keys=True, indent=4, separators=(',', ': ')) # doesnt quite work
    print(f"JSON DUMP: {json.dumps(json_data_out, indent=4)}")
    data_file.write(json.dumps(json_data_out, indent=4))  # format json data
    # json.dump(json_dict_formatted, data_file)
    # print(json.load(data_file))


def remove_data(year: str, month: str, data_type: str, data_name: str, data_value: str) -> None:
    data_file = open(f"./json/{u.get_user_details()[0]}.json", 'r')
    json_data_raw = json.load(data_file)
    json_obj_data, json_obj = pull_data(year, month)

    json_data_dict = {}
    json_data_dict["month"] = json_obj_data[0]  # WATCH CASTING
    json_data_dict["expenses"] = json_obj_data[1]
    json_data_dict["incomes"] = json_obj_data[2]

    if data_type == "expenses":
        del json_data_dict["expenses"][data_name]
    else:
        del json_data_dict["incomes"][data_name]

    print(f"DICT = {json_data_dict}")

    data_file.close()
    data_file = open(f"./json/{u.get_user_details()[0]}.json", 'w')
    json_data_out = json_data_raw
    for i in range(len(json_data_raw[year])):
        if i == json_obj:
            json_data_out[year][i] = json_data_dict

    print(json.dumps(json_data_out, indent=4))
    data_file.write(json.dumps(json_data_out, indent=4))
