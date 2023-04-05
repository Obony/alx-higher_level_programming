#!/usr/bin/python3
"""Class square declaration"""


class Square:
    """My square class"""

    def __init__(self, size=0):
        """Initializing my square class
        Args:
            size: size of my square
        Raises:
            TypeError: if size is not integer
            ValueError: if size < 0
        """

        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size
