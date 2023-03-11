#!/usr/bin/python3
"""
Amenity package for the AirBnB
"""
from .base_model import BaseModel


class Amenity(BaseModel):
    """
    Amenity class - features that provide comfort, convenience, or pleasure
    Class Attributes:
        name (str): name of the feature
    """

    name = ""
