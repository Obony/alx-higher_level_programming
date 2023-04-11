#!/usr/bin/python3
"""Defines a class Rectangle that inherits from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle is derived or Sub Class of BaseGeometry"""

    def __init__(self, width, height):
        """Initializes data for the rectangle class"""

        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """string representation of a Rectangle object"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
