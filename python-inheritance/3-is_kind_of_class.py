#!/usr/bin/python3
"""
Module 3-is_kind_of_class contains the function is_kind_of_class that checks
if an object is an instance of, or if the object is an instance of a class
that inherited from, the specified class.
"""

def is_kind_of_class(obj, a_class):
    """Check if an object is an instance of, or if it is an instance of a
    class that inherited from, the specified class.

    Args:
        obj: The object to check.
        a_class: The class to check against.

    Returns:
        True if obj is an instance of a_class or if obj is an instance of a
        class that inherited from a_class, False otherwise.
    """
    return isinstance(obj, a_class)
