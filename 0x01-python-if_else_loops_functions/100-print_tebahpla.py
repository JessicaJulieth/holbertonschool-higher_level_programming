#!/usr/bin/python3
def reversAlphabets():
    for i in range(122, 96, -1):
        if i % 2 != 0:
            i -= 32
        print("{:c}".format(i), end='')


reversAlphabets()
