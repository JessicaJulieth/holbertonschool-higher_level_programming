#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_Dict = a_dictionary.copy()
    for i in new_Dict:
        new_Dict[i] *= 2
    return new_Dict
