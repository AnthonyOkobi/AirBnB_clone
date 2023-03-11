#!/usr/bin/python3
"""
City package for the AirBnB
"""
from .base_model import BaseModel


class City(BaseModel):
    """
    City class - city of location
    Class Attributes:
        state_id (str): the id of the state
        name: name of the city
    """

    state_id = ""
    name = ""
