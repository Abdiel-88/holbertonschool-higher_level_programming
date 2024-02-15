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
        """Converts list of dictionaries to JSON string."""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON string representation of list_objs to a file.

        Args:
            list_objs (list): A list of instances that inherit from Base.
        """
        filename = f"{cls.__name__}.json"
        list_dicts = []
        if list_objs is not None:
            list_dicts = [obj.to_dictionary() for obj in list_objs]

        json_string = cls.to_json_string(list_dicts)

        with open(filename, 'w') as f:
            f.write(json_string)
