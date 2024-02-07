#!/usr/bin/python3
"""
Module 7-base_geometry contains the class BaseGeometry with enhanced
functionality including a method for validating integer values.
"""


class BaseGeometry:
    """A class with public instance methods."""

    def area(self):
        """Raises an Exception with a message indicating that the method
        is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates that a given value is an integer greater than 0.

        Args:
            name (str): The name of the value.
            value (int): The value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
