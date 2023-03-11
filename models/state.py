#!/usr/bin/python3
"""
State package for the AirBnB
"""
from .base_model import BaseModel


class State(BaseModel):
    """
    State class - state of location
    Class Attributes:
        name (str): name of the state
    """

    name = ""
