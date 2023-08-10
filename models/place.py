#!/usr/bin/python3
""" Class place """
from models.base_model import BaseModel

class place(BaseModel):
    """ place class that inherits BaseModel."""
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    numbers_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    longitude = 0.0
    latitude = 0.0
    amenity_ids = []
