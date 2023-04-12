#!/usr/bin/python3
"""
Defines a Pascal's Triangle function
"""


def pascal_triangle(n):
    """
    returns a list of lists of integers representing the Pascal’s triangle of n
    """
    if n <= 0:
        return []

    pascal = [[1]]
    if n >= 2:
        pascal.append([1, 1])
    for time in range(n-2):
        prev = pascal[-1]
        new_list = [1, 1]
        index = 1
        for i in range(0, len(prev)-1):
            new_list.insert(index, (prev[i] + prev[i+1]))
            index += 1
        pascal.append(new_list)

    return pascal
