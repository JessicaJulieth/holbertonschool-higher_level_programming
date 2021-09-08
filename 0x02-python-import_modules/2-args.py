#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    Len = (len(sys.argv[1:]))
    if Len == 0:
        print("{} arguments.".format(Len))
    elif Len == 1:
        print("{} argument:".format(Len))
    else:
        print("{} arguments:".format(Len))
    for i in range(1, len(sys.argv)):
        print("{}: {}".format(i, sys.argv[i]))
