#!/usr/bin/python3
'''
    Implement Geometry class
'''
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    '''
        Implement class Square
    '''
    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        return (self.__size ** 2)

    def __str__(self):
        """string representation of Square object"""
        return "[Square] {}/{}".format(self.__size, self.__size)
