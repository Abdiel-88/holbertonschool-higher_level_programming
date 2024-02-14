#!/usr/bin/python3
"""
This module contains the Rectangle class that inherits from Base.
"""

from models.base import Base


class Rectangle(Base):
    """
    Represents a rectangle object that inherits from Base.

    Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
        x (int): The x coordinate of the rectangle.
        y (int): The y coordinate of the rectangle.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a new Rectangle instance.

        Args:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
        x (int, optional): The x coordinate of the rectangle. Defaults to 0.
        y (int, optional): The y coordinate of the rectangle. Defaults to 0.
        id (int, optional): The id of the object.
        If None, an id is automatically assigned.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Gets or sets the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Gets or sets the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Gets or sets the x coordinate of the rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Gets or sets the y coordinate of the rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        Returns the area of the Rectangle instance.
        """
        return self.width * self.height

    def display(self):
        """
        Prints the Rectangle instance to stdout using the '#' character,
        taking into account the x and y attributes.
        """
        # Print the "y" top margin
        print("\n" * self.y, end="")

        # Print each row of the rectangle
        for row in range(self.height):
            # Print the "x" left margin followed by the row of "#"
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """
        Returns the string representation of the Rectangle instance.
        """
        return (f"[Rectangle] ({self.id}) {self.x}/{self.y} "
                f"- {self.width}/{self.height}")
