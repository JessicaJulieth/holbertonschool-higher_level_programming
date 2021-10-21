#!/usr/bin/python3
""" Print square """


def print_square(size):
    """ Function that prints a square with the character #
        Arg:
        size: list_length square
        Raise:
        TypeError: size must be an integer
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise TypeError("size must be >= 0")
    if size == float and size < 0:
        raise TypeError("size must be an integer")
    for i in range(size):
        print("#" * size)
