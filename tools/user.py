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

global current_user_id

def get_user_id():
    return current_user_id
