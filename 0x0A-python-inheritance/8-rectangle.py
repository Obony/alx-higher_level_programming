#!/usr/bin/python3
"""creating BaseGeometry class"""


class BaseGeometry:
    """class BaseGeometry represented"""

    def area(self):
        """when it is not implemented"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''
            Validating the integer
        '''
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


    class Rectangle(BaseGeometry):
    """ Rectangle is a Derived or Sub Class of BaseGeometry """

    def __init__(self, width, height):
        """ Initializes data for the rectangle class """

        BaseGeometry.integer_validator(self, "width", width)
        self.__width = width
        BaseGeometry.integer_validator(self, "height", height)
        self.__height = height
