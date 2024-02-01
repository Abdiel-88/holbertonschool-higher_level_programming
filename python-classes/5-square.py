#!/usr/bin/python3
"""
Defines a class Square with size validation,
area calculation, and printing capability.
"""


class Square:
    """
    A class that defines a square by its size with validation
    and can calculate its area and print itself.
    """
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        """Retrieves the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square, with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the current square area."""
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square with the character #
        or an empty line if size is 0.
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size)


if __name__ == "__main__":
    Square = __import__('5-square').Square

    my_square = Square(3)
    my_square.my_print()

    print("--")

    my_square.size = 10
    my_square.my_print()

    print("--")

    my_square.size = 0
    my_square.my_print()

    print("--")
