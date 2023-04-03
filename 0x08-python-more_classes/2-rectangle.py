#!/usr/bin/python3
"""Define a rectangle"""


class Rectangle:
    """Represents rectangle"""

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.
        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        self.height = height
        self.width = width

    @property
    def height(self):
        """Get/set the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """
            Checking for TypeError and ValueError
            then setting up the private var
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """Get/set the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """
            Checking for TypeError and ValueError
            then setting up the private var
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        """
            Calculates the area of a rectangle
        """
        return self.height * self.width

    def perimeter(self):
        """
            Calculates the perimeter of a rectangle
        """
        if self.height == 0 or self.width == 0:
            return 0

        return (self.height + self.width) * 2
