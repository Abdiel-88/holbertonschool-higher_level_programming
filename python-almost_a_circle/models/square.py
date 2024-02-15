#!/usr/bin/python3
"""
This module contains the Square class that inherits from Rectangle.
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Represents a square object that inherits from Rectangle.
    A Square is a Rectangle with equal width and height.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a new Square instance.

        Args:
            size (int): The size of the square's sides.
            x (int, optional): The x coordinate of the square. Defaults to 0.
            y (int, optional): The y coordinate of the square. Defaults to 0.
            id (int, optional): The id of the object.
            If None, an id is automatically assigned.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        # Call the Rectangle's width setter for validation
        self.width = value
        self.height = value

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    def update(self, *args, **kwargs):
        attrs = ['id', 'size', 'x', 'y']
        if args:
            for attr, arg in zip(attrs, args):
                if attr == 'size':
                    self.size = arg  # Use the size property for validation
                else:
                    setattr(self, attr, arg)
        else:
            for key, value in kwargs.items():
                if key == 'size':
                    self.size = value  # Use the size property for validation
                elif key in attrs:
                    setattr(self, key, value)
