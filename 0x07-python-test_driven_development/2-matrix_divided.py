#!/usr/bin/python3
"""Defines a matrix division function."""
def matrix_divided(matrix, div):
    """Divide all elements of a matrix.
    Args:
        matrix (list): A list of lists of ints or floats.
        div (int/float): The divisor.
    Raises:
        TypeError: If the matrix contains non-numbers.
        TypeError: If the matrix contains rows of different sizes.
        TypeError: If div is not an int or float.
        ZeroDivisionError: If div is 0.
    Returns:
        A new matrix representing the result of the division.
    """

    # Iterate over each row in the matrix
    for row in matrix:
        # If the row is not a list, or it contains non-numeric values, raise an error
        if not isinstance(row, list) or not all(isinstance(elem, (int, float)) for elem in row):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Check that all rows have the same length
    # Get the length of the first row
    first_row_len = len(matrix[0])
    # Iterate over each row in the matrix
    for row in matrix:
        # If the length of the row is not the same as the length of the first row, raise an error
        if len(row) != first_row_len:
            raise TypeError("Each row of the matrix must have the same size")

    # Check that div is a number
    # If div is not a number, raise an error
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Check that div is not 0
    # If div is 0, raise an error
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Divide all elements of the matrix by div, rounded to 2 decimal places
    # Iterate over each row in the matrix
    new_matrix = []
    for row in matrix:
        # Create a new row to store the divided values
        new_row = []
        # Iterate over each element in the row, divide it by div, and append it to the new row
        for elem in row:
            new_elem = round(elem/div, 2)
            new_row.append(new_elem)
        # Append the new row to the new matrix
        new_matrix.append(new_row)

    # Return the new matrix
    return new_matrix
