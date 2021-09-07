#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastD = int(repr(number)[-1])
of = ("Last digit of {} is {}".format(number, lastD))
if number < 0:
    lastD *= -1
if lastD < 6:
    if lastD != 0:
        print("{} and is less than 6 and not 0".format(of, number, lastD))
elif lastD > 5:
    print("{} {} is {} and is greater than 5".format(of, number, lastD))
if lastD == 0:
    print("{} {} is {} and is 0".format(of, number, lastD))
