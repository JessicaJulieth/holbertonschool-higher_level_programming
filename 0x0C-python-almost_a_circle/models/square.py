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
