#!/usr/bin/python3
"""Real definition of a rectangle"""


class Rectangle:
    """ Class Rectangle that defines a rectangle """
    def __init__(self, width=0, height=0):
        """ Initialize a rectangle """
        self.height = height
        self.width = width

    @property
    def width(self):
        """ Getter method width """
        return self.__width

    @width.setter
    def width(self, value):
        """ Setter method width """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ Getter method height """
        return self.__height

    @height.setter
    def height(self, value):
        """ Setter method height """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """ Getter method area """
        return self.width * self.height

    def perimeter(self):
        """ Getter method perimeter """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)
