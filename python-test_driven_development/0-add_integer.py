#!/usr/bin/python3
"""
This module defines a function add_integer that adds two numbers.
The numbers must be integers or floats, where floats are cast to integers before addition.
"""

def add_integer(a, b=98):
    """
    Adds two integers or floats.
    
    Parameters:
    a (int, float): The first number.
    b (int, float, optional): The second number. Defaults to 98.

    Returns:
    int: The sum of a and b, with both cast to integers if they are floats.

    Raises:
    TypeError: If either a or b is neither an integer nor a float.
    """
    if (not isinstance(a, int) and not isinstance(a, float)) or a is None:
        raise TypeError("a must be an integer")
    if (not isinstance(b, int) and not isinstance(b, float)) or b is None:
        raise TypeError("b must be an integer")
    return int(a) + int(b)

# Test code block, for demonstration purposes
if __name__ == "__main__":
    add_integer = __import__('0-add_integer').add_integer

    print(add_integer(1, 2))
    print(add_integer(100, -2))
    print(add_integer(2))
    print(add_integer(100.3, -2))
    try:
        print(add_integer(4, "School"))
    except Exception as e:
        print(e)
    try:
        print(add_integer(None))
    except Exception as e:
        print(e)
