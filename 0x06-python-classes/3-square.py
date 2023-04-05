#!/usr/bin/python3
"""My square declaration"""


class Square:
    """My square class introduction"""

    def __init__(self, size=0):
        """Initializing this square class
        Args:
            size: size of my square
        Raises:
            TypeError: if size is not integer
            ValueError: if size is less than zero
        """

        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size

    def area(self):
        """
        Calculate area of my square
        Returns: The square of the size
        """

        return (self.__size ** 2)
