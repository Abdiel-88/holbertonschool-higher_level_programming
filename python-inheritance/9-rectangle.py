#!/usr/bin/python3
"""
Module 9-rectangle contains the Rectangle
class that inherits from BaseGeometry.
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A Rectangle class that inherits from BaseGeometry."""

    def __init__(self, width, height):
        """
        Initializes a new Rectangle instance with validated width and height.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Calculates the area of the rectangle.

        Returns:
            The area of the rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Returns the rectangle description.

        Returns:
            The string representation of the rectangle.
        """
        return f"[Rectangle] {self.__width}/{self.__height}"
