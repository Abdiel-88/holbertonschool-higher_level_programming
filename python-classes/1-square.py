#!/usr/bin/python3
"""Defines a class Square that represents a square, instantiated with size."""

class Square:
    """A class that defines a square by its size, a private instance attribute."""
    def __init__(self, size):
        self.__size = size


if __name__ == "__main__":
    my_square = Square(3)
    print(type(my_square))
    print(my_square.__dict__)

    try:
        print(my_square.size)
    except Exception as e:
        print(e)

    try:
        print(my_square.__size)
    except Exception as e:
        print(e)
