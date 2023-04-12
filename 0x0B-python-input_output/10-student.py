#!/usr/bin/python3
"""Defines a class Student."""


class Student:
    '''
        Represent a student
    '''
    def __init__(self, first_name, last_name, age):
        '''
            Initializing instance variables
        '''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        '''
            Get a dictionary representation of the Student
        '''
        my_dict = {}
        for item in dir(self):
            condition_1 = not item.startswith("__")
            condition_2 = not callable(getattr(self, item))
            if type(attrs) is list:
                condition_3 = item in attrs
            else:
                condition_3 = True
            if condition_1 and condition_2 and condition_3:
                my_dict[item] = getattr(self, item)

        return
