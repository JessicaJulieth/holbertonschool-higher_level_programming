#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
of = "Last digit of"
a1 = "and is less than 6 and not 0"
a2 = "and is greater than 5"
a3 = "and is 0"
lastD = int(repr(number)[-1])
if number < 0:
    lastD *= -1
if lastD < 6:
    if lastD != 0:
        print("{} {} is {} {}".format(of, number, lastD, a1))
elif lastD > 5:
    print("{} {} is {} {} ".format(of, number, lastD, a2))
if lastD == 0:
    print("{} {} is {} {} ".format(of, number, lastD, a3))
