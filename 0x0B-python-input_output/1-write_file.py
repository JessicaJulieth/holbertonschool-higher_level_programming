#!/usr/bin/python3
"""
This function writes
a string to a text file
"""


def write_file(filename="", text=""):
    """
    writes the string s
    to the file and returns the number of characters written
    """
    with open(file=filename, encoding='utf-8', mode='w') as df:
        return df.write(text)
