#!/usr/bin/python3
"""
This module provides a MyList class that inherits from the built-in list class
and includes a method for printing the list elements in ascending sorted order.
"""


class MyList(list):
    """
    MyList extends the built-in list with a method to print sorted.
    """
    def print_sorted(self):
        """
        Prints the list in ascending order without modifying the original list.
        """
        print(sorted(self))


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/1-my_list.txt")
