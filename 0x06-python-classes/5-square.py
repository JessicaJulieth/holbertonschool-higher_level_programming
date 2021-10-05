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
        """Define Square area"""
        return self.__size ** 2

    @property
    def size(self):
        """Get size value"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set size value"""
        if isinstance(value, int):
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value
        else:
            raise TypeError("size must be an integer")

    def my_print(self):
        """Print the Square with #"""
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__size):
                print("#" * self.__size)
