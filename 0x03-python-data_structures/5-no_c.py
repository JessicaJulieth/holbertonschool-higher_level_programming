#!/usr/bin/python3
def no_c(my_string):
    for i in my_string[0:]:
        if i not in ("C","c"):
            print("{:s}".format(str(i)), end="")