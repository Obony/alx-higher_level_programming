#!/usr/bin/python3
'''
   Adding the two integers
   a (int | float)
   b (int | float)
'''


def add_integer(a, b=98):
    '''
        Adding the two integers
    '''
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")

    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")

    return (int(a) + int(b))
