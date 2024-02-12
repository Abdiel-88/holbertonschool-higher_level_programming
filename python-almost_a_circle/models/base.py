#!/usr/bin/python3
"""Defines a base model class."""
import json
import csv
import turtle

"""
This module defines the Base class.
The Base class serves as the foundation for all other classes in this project.
It manages an id attribute for instances to avoid duplicating code.
"""


class Base:
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base instance.
        Args:
            id (int): The id of the instance.
            If None, an id is automatically assigned.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
