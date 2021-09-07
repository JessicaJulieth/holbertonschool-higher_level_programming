#!/usr/bin/python3
def lowerAlphabets():
    for c in range(97, 123):
        if c not in (101, 112):
            print("{:s}".format(chr(c)), end='')


lowerAlphabets()
