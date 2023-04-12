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
        if type(attrs) == list:
            for i in attrs:
                if type(i) != str:
                        my_dict = self.__dict__
                        break
                try:
                    my_dict[i] = getattr(self, i)
                except:
                    pass
        else:
            my_dict = self.__dict__
        return (my_dict)
