#!/usr/bin/python3
"""module that creates a class called Base"""

class Base():
    """This class will be the “base” of all other classes in this project.
    Its goal is to manage the id attribute in all your future classes and
    to avoid duplicating the same code.

    Args:
        _nb_objects (int): private class attribute
    """

    __nb_objects = 0

    def __init__(self, id=None):
        
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
