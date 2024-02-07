#!/usr/bin/python3
"""
This module defines the MyList class which
inherits from the built-in list class.
It includes a method to print the list
elements in ascending order.
"""


class MyList(list):
    """MyList class inherits from list.
    Attributes:
        Inherits all attributes from the built-in list class.
    Methods:
        print_sorted(self): Prints the elements of the list in ascending order.
    """
    def print_sorted(self):
        """
        Prints the list elements in ascending
        order without modifying the original list.
        """
        print(sorted(self))


if __name__ == "__main__":
    # Example usage
    my_list = MyList()
    my_list.append(1)
    my_list.append(4)
    my_list.append(2)
    my_list.append(3)
    my_list.append(5)
    print("Original list:")
    print(my_list)
    print("Sorted list:")
    my_list.print_sorted()
    print("Original list after sorting:")
    print(my_list)
