#!/usr/bin/python3
"""Defines a JSON file-reading function."""


def load_from_json_file(filename):
    """create an object from a JSON file"""
    from json import load
    with open(filename, "r", encoding="UTF-8") as f:
        return load(f)
