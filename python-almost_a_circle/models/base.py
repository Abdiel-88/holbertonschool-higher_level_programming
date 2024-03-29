#!/usr/bin/python3
"""
This module defines the Base class for the project. It aims to manage id
attributes in all future classes and avoid duplicating code.
"""
import json
import os


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
    def from_json_string(json_string):
        """
        Returns the list of the JSON string representation json_string.

        Args:
            json_string (str): A string representing a list of dictionaries.

        Returns:
            list: The list represented by json_string. Returns an empty list if
            json_string is None or empty.
        """
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

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

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns the JSON string representation of list_dictionaries.

        Args:
            list_dictionaries (list of dict): A list of dictionaries.

        Returns:
            str: The JSON string representation of list_dictionaries.
        """
        if not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def create(cls, **dictionary):
        """
        Returns an instance with all
        attributes set according to the dictionary.

        Args:
            **dictionary: A dictionary of attributes to set on the instance.

        Returns:
            Instance of cls with attributes set according to dictionary.
        """
        # Create a "dummy" instance with default mandatory attributes
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        else:
            raise TypeError("Unknown class name")

        # Use the instance's update method to set the actual attributes
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        Returns a list of instances from a file named <Class name>.json.

        Returns:
            list: A list of class instances.
        """
        filename = f"{cls.__name__}.json"

        # Check if the file exists, return an empty list if it doesn't
        if not os.path.isfile(filename):
            return []

        # Read from the file and deserialize the JSON string
        with open(filename, 'r') as file:
            json_string = file.read()
        list_dictionaries = cls.from_json_string(json_string)

        # Convert each dictionary into an instance using create method
        instances = [cls.create(**d) for d in list_dictionaries]

        return instances
