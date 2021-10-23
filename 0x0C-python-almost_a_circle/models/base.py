#!/usr/bin/python3
"""module that creates a class called Base"""

from json import dumps


class Base():
    """This class will be the “base” of all other classes in this project.
    Its goal is to manage the id attribute in all your future classes and
    to avoid duplicating the same code.

    Attributes:
        __nb_objects = 0: private class attribute
    """

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """
        Function to returns the JSON string
        representation of list_dictionaries
        Args:
            list_dictionaries dict: instance dictionary
        Returns:
            str: JSON object as a string
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return dumps(list_dictionaries)
