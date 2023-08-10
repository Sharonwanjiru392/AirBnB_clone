#!/usr/bin/python3
"""Define User class."""
from model.base_model import BaseModel

class User(Base_model):
    """Represent User.
    Attributes:
        email (str): email of the user.
        password (str): The user password.
        first_name (str): The first name of the user.
        last_name (str): The user last name."""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
