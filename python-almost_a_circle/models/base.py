#!/usr/bin/python3
"""
This module defines the Base class for the project. It aims to manage id
attributes in all future classes and avoid duplicating code.
"""
import json


class Base:
    """
    The Base class to act as the foundation for all other classes in this
    project.

    Attributes:
        __nb_objects (int): A class attribute to count the number of objects
                            if no id is given.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes a new Base instance.

        Args:
            id (Optional[int]): The id of the instance. If None, an id is
                                automatically assigned.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns the JSON string representation of list_dictionaries.

        Args:
            list_dictionaries (list of dict): A list of dictionaries.

        Returns:
            str: The JSON string representation of list_dictionaries.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)
