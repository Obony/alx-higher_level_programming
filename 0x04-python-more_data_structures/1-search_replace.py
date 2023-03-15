#!/usr/bin/python3
#1-search_replace.py
#Faith Nyaberi <faithnyabz69@gmail.com>

def search_replace(my_list, search, replace):
    '''Replace all occurrences of an element by another in a new list.'''
    new_list = []
    for i in range(len(my_list)):
        if my_list[i] == search:
            new_list.append(replace)
        else:
            new_list.append(my_list[i])
            return (new_list)

