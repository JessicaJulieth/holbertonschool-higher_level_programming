#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    new_Dictionary = list(a_dictionary.keys())
    for i in new_Dictionary:
        if value == a_dictionary.get(i):
            del a_dictionary[i]
    return a_dictionary
