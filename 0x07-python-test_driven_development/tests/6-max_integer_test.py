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

    def test_types(self):
        self.assertRaises(TypeError, max_integer, "man")
        self.assertRaises(TypeError, max_integer, 6)
        self.assertRaises(TypeError, max_integer, False)
        self.assertRaises(TypeError, max_integer, None)
