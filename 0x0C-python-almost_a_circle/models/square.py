#!/usr/bin/python3
"""
    Square class
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Define class Square

    Args:
        Rectangle (Base): class Rectangle
    """
    def __init__(self, size, x=0, y=0, id=None):
        """Initialisation
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        String representation of a Square

        Returns:
            str: Square <id> <x>/<y> - size
        """
        return ("[Square] ({0}) {1}/{2} - {3}".format(self.id,
                self.x, self.y, self.width))

    @property
    def size(self):
        """size getter

        Returns:
            int: private instance attribute x of rectangle
        """
        return self.width

    @size.setter
    def size(self, size):
        """
        Set the value in private instance attribute

        Args:
            size (int): size of square

        Raises:
            TypeError: width must be an integer
            ValueError: width must be > 0
        """
        if not isinstance(size, (int,)):
            raise TypeError("width must be an integer")
        if size <= 0:
            raise ValueError("width must be > 0")
        self.height = size
        self.width = size


    def update(self, *args, **kwargs):
        """
            Update the value of the Square with arbitrary
            arguments or keyword arguments
        """
        attr = ('x', 'id', 'size', 'y')
        if args and args[0] is not None:
            for idx in range(len(args)):
                setattr(self, attr[idx], args[idx])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        dictionary representation of a Square

        Returns:
            dict: attribute dictionary of Square
        """
        new_dict = {'id': self.id, 'x': self.x, 'size': self.size, 'y': self.y}
        return new_dict
