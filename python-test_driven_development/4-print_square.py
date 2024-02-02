#!/usr/bin/python3
"""Module for print_square method."""


def print_square(size):
    """Method for printing a square with # characters.

    Args:
        size: The int size of the square's side.

    Raises:
        TypeError: If size is not an int.
        ValueError: If size is < 0.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    print((("#" * size + "\n") * size), end="")


# Ensure there are two blank lines before the end of the file comment or code
# And also ensure there's a newline at the very end of the file

