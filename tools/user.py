# user.py
# 'struct' representation of user as existing in the database
from dataclasses import dataclass


@dataclass
class User():
    id: int
    firstname: str
    lastname: str
    age: int
    dateofbirth: str
    password: str


current_user = User


def set_user_details(id: int, first_name: str, last_name: str, age: int, dateofbirth: str,  password: str) -> None:
    global current_user
    current_user.id = id
    current_user.firstname = first_name
    current_user.lastname = last_name
    current_user.age = age
    current_user.dateofbirth = dateofbirth
    current_user.password = password


def get_user_details() -> list:
    global current_user
    try:
        return [current_user.id, current_user.firstname, current_user.lastname, current_user.age, current_user.dateofbirth, current_user.password]
    except NameError:
        print("Current user details undefined: Error in login process")
