#!/usr/bin/python3
"""
Module 0-add_integer
Adds two integer or float values.
"""


def add_integer(a, b=98):
    """Return the addition of a and b as integers."""
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
