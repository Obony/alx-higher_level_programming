#!/usr/bin/python3
#1-search_replace.py
#Faith Nyaberi <faithnyabz69@gmail.com>

def search_replace(my_list, search, replace):
    new_list = my_list[:]
    for index, item in enumerate(new_list):
        if (item == search):
            new_list[index] = replace
    return new_list
