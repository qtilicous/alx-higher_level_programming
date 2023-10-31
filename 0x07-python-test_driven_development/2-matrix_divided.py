#!/usr/bin/python3
"""
This module defines a function that divides all elements of a matrix.

"""


def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix by a given divisor.

    Args:
        matrix (list of lists): The matrix to be divided.
        div (int or float): The divisor.

    Returns:
        list of lists: A new matrix with elements divided by div, rounded to 2 decimal places.

    Raises:
        TypeError: If matrix is not a list of lists of integers or floats,
                   or if each row of the matrix has different sizes,
                   or if div is not a number (integer or float).
        ZeroDivisionError: If div is equal to 0.
    """
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not matrix:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    num_columns = len(matrix[0])

    for row in matrix:
        if len(row) != num_columns:
            raise TypeError("Each row of the matrix must have the same size")

        for element in row:
            if not (isinstance(element, int) or isinstance(element, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not (isinstance(div, int) or isinstance(div, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    result = [[round(element / div, 2) for element in row] for row in matrix]

    return result
