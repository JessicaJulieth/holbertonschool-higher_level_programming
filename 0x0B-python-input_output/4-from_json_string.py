#!/usr/bin/python3
"""
function that returns an object (Python data structure)
represented by a JSON string
"""

from json import loads


def from_json_string(my_str):
    """
    function that returns an object (Python data structure)
    represented by a JSON string
    """
    return loads(my_str)
