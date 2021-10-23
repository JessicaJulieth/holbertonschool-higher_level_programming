#!/usr/bin/python3
"""Rectangle class
"""


from models.base import Base


class Rectangle(Base):
    """Define a Rectangle class
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialisation of Rectangle

        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
            x (int, optional): [description]. Defaults to 0.
            y (int, optional): [description]. Defaults to 0.
            id (int, optional): Rectangle identification. Defaults to None.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Width Getter

        Returns:
            int: private instance attribute width of rectangle
        """
        return self.__width

    @property
    def height(self):
        """Height Getter

        Returns:
            int: private instance attribute height of rectangle
        """
        return self.__height

    @property
    def x(self):
        """x Getter

        Returns:
            int: private instance attribute x of rectangle
        """
        return self.__x

    @property
    def y(self):
        """y Getter

        Returns:
            int: private instance attribute y of rectangle
        """
        return self.__y

    @width.setter
    def width(self, value):
        """Set the value in private instance attribute

        Args:
            value (int): width value
        """
        self.__width = value

    @height.setter
    def height(self, value):
        """Set the value in private instance attribute

        Args:
            value (int): height value
        """
        self.__height = value

    @x.setter
    def x(self, value):
        """Set the value in private instance attribute

        Args:
            value (int): x value
        """
        self.__x = value

    @y.setter
    def y(self, value):
        """Set the value in private instance attribute

        Args:
            value (int): y value
        """
        self.__y = value
