#!/usr/bin/python3
"""
This function writes
a string to a text file
"""


def append_write(filename="", text=""):
    """
    writes the string s
    to the file and returns the number of characters written
    """
    with open(file=filename, encoding='utf-8', mode='a') as df:
        return df.write(text)
