#!/usr/bin/python3
"""module that creates a class called Base"""

import json


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
        """ static method returns the JSON string representation of
        list_dictionaries
        Attributes:
            list_dictionaries: list of dictionaries
        Returns:
            json string
        """
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
