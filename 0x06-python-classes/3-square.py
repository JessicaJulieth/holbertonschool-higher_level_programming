#!/usr/bin/python3
"""Square class"""


class Square:
    """Empty Square class"""
    def __init__(self, size=0):
        if isinstance(size, int):
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
        else:
            raise TypeError("size must be an integer")

    def area(self):
        return (pow(self.__size, 2))


if __name__ != '__main':
    pass
