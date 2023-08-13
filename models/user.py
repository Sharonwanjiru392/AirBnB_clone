#!/usr/bin/python3
<<<<<<< HEAD
from models.base_model import BaseModel

"""Class model of a User."""


class User(BaseModel):
=======
"""Define User class."""
from model.base_model import BaseModel

class User(Base_model):
    """Represent User.
    Attributes:
        email (str): email of the user.
        password (str): The user password.
        first_name (str): The first name of the user.
        last_name (str): The user last name."""
>>>>>>> 654eb7633356ce5e35eadba8f9604d08a91d85e4
    email = ""
    password = ""
    first_name = ""
    last_name = ""
