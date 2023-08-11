#!/usr/bin/python3
<<<<<<< HEAD
from models.base_model import BaseModel


class Place(BaseModel):
=======
""" Class place """
from models.base_model import BaseModel

class place(BaseModel):
    """ place class that inherits BaseModel."""
>>>>>>> 654eb7633356ce5e35eadba8f9604d08a91d85e4
    city_id = ""
    user_id = ""
    name = ""
    description = ""
<<<<<<< HEAD
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
=======
    numbers_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    longitude = 0.0
    latitude = 0.0
>>>>>>> 654eb7633356ce5e35eadba8f9604d08a91d85e4
    amenity_ids = []
