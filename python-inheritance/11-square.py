#!/usr/bin/python3
"""
Module 11-square contains the Square class that inherits from Rectangle.
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A Square class that inherits from Rectangle."""

    def __init__(self, size):
        """
        Initializes a new Square instance.

        Args:
            size (int): The size of the square's sides.
        """
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            The area of the square.
        """
        return self.__size ** 2

    def __str__(self):
        """
        Returns the square description.

        Returns:
            The string representation of the square,
            formatted as [Square] <width>/<height>.
        """
        return f"[Square] {self.__size}/{self.__size}"
