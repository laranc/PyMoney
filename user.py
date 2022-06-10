# user.py
# 'struct' representation of user as existing in the database
from dataclasses import dataclass

@dataclass
class User():
    firstname: str
    lastname: str
    age: int
    dateofbirth: str
    password: str
