#!/usr/bin/python3
#1-search_replace.py
#Faith Nyaberi <faithnyabz69@gmail.com>

def search_replace(my_list, search, replace):
    return (list(map(lambda x: replace if x is search else x, my_list)))
