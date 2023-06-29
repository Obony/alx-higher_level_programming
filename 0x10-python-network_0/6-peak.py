#!/usr/bin/python3
"""
This module contains a function to return peek of a list
"""


def find_peak(ints):
    """
    finds a peak in a list of unsorted integers
    """
    if not ints or type(ints) is not list:
        return None

    left, right = 0, len(ints) - 1
    while left < right:
        mid = left + (right - left) // 2
        condition_1 = (mid - 1 < 0 or ints[mid - 1] <= ints[mid])
        condition_2 = (mid + 1 >= len(ints) or ints[mid + 1] <= ints[mid])
        if condition_1 and condition_2:
            return ints[mid]
        elif mid - 1 >= 0 and ints[mid - 1] > ints[mid]:
            right = mid - 1
        elif mid + 1 < len(ints) and ints[mid + 1] > ints[mid]:
            left = mid + 1

    return ints[left]
