#!/usr/bin/python3
"""
This module defines the matrix_divided function that divides all elements
of a matrix.
"""

def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a divisor and rounds the results
    to 2 decimal places. Validates matrix integrity and divisor validity.
    """
    matrix_err = "matrix must be a matrix (list of lists) of integers/floats"
    size_err = "Each row of the matrix must have the same size"
    num_err = "div must be a number"
    zero_err = "division by zero"

    if (not isinstance(matrix, list) or
        not all(isinstance(row, list) for row in matrix) or
        not all(isinstance(elem, (int, float)) for row in matrix for elem in row)):
        raise TypeError(matrix_err)

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError(size_err)

    if not isinstance(div, (int, float)):
        raise TypeError(num_err)

    if div == 0:
        raise ZeroDivisionError(zero_err)

    return [[round(elem / div, 2) for elem in row] for row in matrix]
