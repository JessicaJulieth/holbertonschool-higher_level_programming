#!/usr/bin/python3

def add_integer(a, b=98):
    """add numbers and return int()
    Arguments:
        a {int} -- [int of float]
    Keyword Arguments:
        b {int} -- [int of float] (default: {98})
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return a+b
