#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        if isinstance(value, int):
            print("{:d}".format(value))
            return True
    except Exception as err:
        print("Exeption: {}".format(err), file=sys.stderr)
        return False
