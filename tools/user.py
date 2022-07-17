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


current_user_id: int


def set_user_id(user_id: int) -> None:
    global current_user_id
    current_user_id = user_id


def get_user_id() -> int:
    global current_user_id
    try:
        return current_user_id
    except NameError:
        print("Current User ID undefined")
