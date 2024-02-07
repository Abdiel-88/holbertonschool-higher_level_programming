#!/usr/bin/python3
"""
Module 2-is_same_class contains a function that checks if an object is exactly
an instance of a specified class.
"""


def is_same_class(obj, a_class):
    """Determine if an object is exactly an instance of a specified class.

    Args:
        obj: The object to check.
        a_class: The class to match the type of obj against.

    Returns:
        True if obj is exactly an instance of a_class; False otherwise.
    """
    return type(obj) is a_class
