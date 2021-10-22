#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """ Test cases to find the maximum integer """
    def Max_Interger(self):

        self.assertEqual(max_integer([5, 10, 15, 20]), 20)
        self.assertEqual(max_integer([15, -15, -20, -8]), 15)
        self.assertEqual(max_integer([0]), 0)
        self.assertEqual(max_integer([25, 50, 45]), 50)
        self.assertEqual(max_integer([-5, 0, 9]), 9)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([1]), 1)


if __name__ == '__main__':
    unittest.main()
