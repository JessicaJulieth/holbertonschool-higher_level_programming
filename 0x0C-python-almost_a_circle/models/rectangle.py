#!/usr/bin/python3
"""Rectangle class
"""


from models.base import Base


class Rectangle(Base):
    """
    Define a Rectangle class which inherits from the Base class
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialisation of Rectangle

        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
            x (int/optional): Defaults to 0.
            y (int): Defaults to 0.
            id (int/optional): Rectangle identification. Defaults to None.
        """
        super().__init__(id)

        self.x = x
        self.y = y
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Width Getter Decorator

        Returns:
            int: private instance attribute width of the rectangle class
        """
        return self.__width

    @property
    def height(self):
        """
        Height Getter Decorator

        Returns:
            int: Private instance attribute height of the rectangle class
        """
        return self.__height

    @property
    def x(self):
        """
        x Getter Decorator

        Returns:
            int: Private instance attribute x of the rectangle class
        """
        return self.__x

    @property
    def y(self):
        """
        y Getter Decorator

        Returns:
            int: private instance attribute y of rectangle class
        """
        return self.__y

    @width.setter
    def width(self, value):
        """
        Set the value in private instance attribute (variable width)

        Args:
            value (int): width value
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """
        Set the value in private instance attribute (variable height)

        Args:
            value (int): height value
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """
        Set the value in private instance attribute (variable x)

        Args:
            value (int): x value
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """
        Set the value in private instance attribute (variable y)

        Args:
            value (int): y value
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        Define Rectangle area: Calculate the area of a rectangle

        Returns:
            int : Rectangle area value
        """
        return self.__width * self.__height

    def display(self):
        """
            Prints the Rectangle instance with character #
        """
        [print("") for _ in range(self.__y)]
        [print(" " * self.x + "#" * self.width) for _ in range(self.height)]

    def __str__(self):
        """
            String representation of Rectangle
        """
        return ("[Rectangle] ({0}) {1}/{2} - {3}/{4}".format(self.id,
                self.x, self.y, self.width, self.height))

    def update(self, *args, **kwargs):
        """
            Update the value of the Rectangle with arbitrary
            (keyword/positional) arguments
        """
        attr = ('width', 'height', 'id', 'x', 'y')
        if args and args[0] is not None:
            for idx in range(len(args)):
                setattr(self, attr[idx], args[idx])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
