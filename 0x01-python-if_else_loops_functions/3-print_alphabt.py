#!/usr/bin/python3
def lowerAlphabets():
    for c in range(97, 123):
        if c not in (101, 113):
            print("{:s}".format(chr(c)), end='')


lowerAlphabets()
