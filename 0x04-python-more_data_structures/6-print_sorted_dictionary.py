#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sortDict = sorted(a_dictionary.items())
    for i in sortDict:
        print("{}: {}".format(i[0], i[1]))
