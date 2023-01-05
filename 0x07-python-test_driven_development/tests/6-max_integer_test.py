#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class testMaxInteger(unittest.TestCase):
    """ class to test cases for the maxx_integer function
    """
    def test_max_integer(self):
        self.assertAlmostEqual(max_integer([23, 20, 20]), 23)
        self.assertAlmostEqual(max_integer([-1, -4, -6, 3]), 3)
        self.assertAlmostEqual(max_integer([3]), 3)
        self.assertAlmostEqual(max_integer([-1, -2, -3, -6]), -1)
        self.assertEqual(max_integer(), None)
        self.assertAlmostEqual(max_integer([-1, 4, 5, 3, 2]), 5)
        self.assertAlmostEqual(max_integer([]), None)
        self.assertAlmostEqual(max_integer([-2]), -2)
        self.assertAlmostEqual(max_integer([4, 8, -1]), 8)

