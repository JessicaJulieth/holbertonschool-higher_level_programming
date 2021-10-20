#!/usr/bin/python3
"""Real definition of a rectangle"""


class Rectangle:
    """ Class Rectangle that defines a rectangle """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ Initialize a rectangle """
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

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

    def __str__(self):
        """ Getter method __str__ """
        Str = ""
        if self.__width == 0 or self.__height == 0:
            return Str
        else:
            for row in range(self.__height):
                for char in range(self.__width):
                    Str += str(self.print_symbol)
                Str += '\n'
            return Str[:-1]

    def __repr__(self):
        """ Getter method __repr__ """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """ Delete method __del__"""
        delet = ("Bye rectangle...")
        Rectangle.number_of_instances -= 1
        print("{}".format(delet))

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ Compares two rectangles """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """ new Rectangle instance with width == height == size """
        return cls(size, size)
