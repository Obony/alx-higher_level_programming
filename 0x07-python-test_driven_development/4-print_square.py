#!/usr/bin/python3
def print_square(size):
    """Print a square with the # character.
    Args:
        size (int): The height/width of the square.
    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is < 0
    """
    # Check that size is an integer
    if not isinstance(size, int):
        # If size is not an integer, raise a TypeError with a helpful message
        raise TypeError("size must be an integer")

    # Check that size is greater than or equal to 0
    if size < 0:
        # If size is less than 0, raise a ValueError with a helpful message
        raise ValueError("size must be >= 0")

    # Check that size is not a float (i.e., a decimal number)
    if isinstance(size, float) and size < 0:
        # If size is a float and less than 0, raise a TypeError with a helpful message
        raise TypeError("size must be an integer")

    # Use nested loops to print out the square
    for i in range(size):
        # Loop over each column of the current row and print a # character
        for j in range(size):
            print("#", end="")

        # After printing all the characters in the current row, move to the next line
        print()

