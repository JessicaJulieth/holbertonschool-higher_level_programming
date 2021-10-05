#!/usr/bin/python3
"""Square class"""


class Square:
    """Empty Square class"""
    def __init__(self, size=0, position=(0, 0)):
        """Initialize Square attribute"""
        self.size = size
        self.__position = position

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
        if self.__position[1] > 0:
            print('\n'*self.__position[1], end='')
        else:
            for i in range(self.__size):
                print(' '*self.__position[0], end='')
                print("#" * self.__size)

    @property
    def position(self):
        """Get position values"""
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError(
                "position must be a tuple of 2 positive integers")
        elif not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError(
                "position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise TypeError(
                "position must be a tuple of 2 positive integers")
        else:
            self.__position = value
