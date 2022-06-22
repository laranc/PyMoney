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
