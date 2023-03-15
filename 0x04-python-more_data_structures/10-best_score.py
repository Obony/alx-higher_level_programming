#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        key, value = max(a_dictionary.items(), key=lambda x: x[1])
        return key
