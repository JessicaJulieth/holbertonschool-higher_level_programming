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
    
    @property
    def size(self):
        '''
            property  to retrieve it
        '''
        return self.__size
    
    @size.setter
    def size(self, value):
        '''
            property  setter to set it
            Args:
            value : must be an integer and greater than zero"
        '''
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        '''
            define a method to get an area of square class
        '''
        return self.__size ** 2