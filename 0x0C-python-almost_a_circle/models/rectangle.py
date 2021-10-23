#!/usr/bin/python3
from models.base import Base
"""module that creates a class called Rectangle that inherits from Base"""


class Rectangle(Base):
    """class Rectangle that inherits from Base class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """class Constructor
        Attributes:
            width: Private instance attribute (integer)
            height: Private instance attribute (integer)
            x: Private instance attribute (integer), 0 by default
            y: Private instance attribute (integer, 0 by default
            id: Private instance attribute (integer) inherited from Base
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ method for width value
        Return:
            width value: integer greater than 0
        """
        return self.__width

    @width.setter
    def width(self, value):
        """ setter method for width
        Attribute:
            width value: must be an integer greater than zero
        """
        self.__width = value

    @property
    def height(self):
        """ method for height value
        Return:
            height value: integer greater than 0
        """
        return self.__height

    @height.setter
    def height(self, value):
        """ setter method for height
        Attribute:
            height value: must be an integer greater than zero
        """
        self.__height = value

    @property
    def x(self):
        """ method for x value
        Return:
            x value: integer >= 0
        """
        return self.__x

    @x.setter
    def x(self, value):
        """ setter method for x
        Attribute:
            x value: must be an integer >= 0
        """
        self.__x = value

    @property
    def y(self):
        """ method for y value
        Return:
            y value: integer >= 0
        """
        return self.__y

    @y.setter
    def y(self, value):
        """ setter method for y
        Attribute:
            y value: must be an integer >= 0
        """
        self.__y = value

    def area(self):
        """ public method that calculates area
        Returns:
            area: integer
        """
        return self.width * self.height
