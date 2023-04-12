#!/usr/bin/python3
"""Defines a JSON file-writing function."""


def save_to_json_file(my_obj, filename):
    """write an object to a text file using JSON"""
    from json import dump
    with open(filename, "w", encoding="UTF-8") as f:
        dump(my_obj, f)
