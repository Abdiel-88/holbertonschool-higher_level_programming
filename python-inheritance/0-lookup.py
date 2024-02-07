#!/usr/bin/python3
"""
This module defines the lookup function that returns a list of available attributes
and methods of an object.
"""

def lookup(obj):
    """Returns the list of available attributes and methods of an object.

    Args:
        obj: The object to list attributes and methods for.

    Returns:
        list: A list of strings, each representing an attribute or method name.
    """
    return dir(obj)
