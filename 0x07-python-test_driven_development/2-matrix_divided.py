#!/usr/bin/python3
""""""

def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix by a given divisor.

    Args:
    - matrix: A list of list containing integers or floats.
    - div: A number (integer or float) to divide the elements of the matrix.

    Raises:
    - TypeError: If matrix is not a lists of integers or float.
    - TypeError: If each row of the matrix does not have the same size.
    - ZeroDivisionError: if div is equal tozero.

    Returns:
    - A new matrix with elements rounded to 2 decimal places after division.
    """


    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    
    return [[round(val / div, 2) for val in row] for row in matrix]
