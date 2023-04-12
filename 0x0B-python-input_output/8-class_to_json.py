#!/usr/bin/python3
"""Defines a Python class-to-JSON function."""


def class_to_json(obj):
    '''
        Returns the dict representation of a class
    '''
    return (getattr(obj, "__dict__"))
