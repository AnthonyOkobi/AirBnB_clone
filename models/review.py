#!/usr/bin/python3
"""
Review package for the AirBnB
"""
from .base_model import BaseModel


class Review(BaseModel):
    """
    Review class - reviews of the places
    Class Attributes:
        place_id (str): id of the place to be reviewed
        user_id (str): id of the user reviewing
        text (str): review
    """

    place_id = ""
    user_id = ""
    text = ""
