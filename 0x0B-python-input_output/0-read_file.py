#!/usr/bin/python3
"""
    This file contains a function
    to open and read a file.
"""


def read_file(filename=""):
    """
    Reads a text file (UTF8)
    and prints it to stdout.
    """

    if filename == "":
        return
    else:
        with open(file=filename, mode="r", encoding="utf-8") as df:
            txt = df.read()
            print(txt)
        return txt
