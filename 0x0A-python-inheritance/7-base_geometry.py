#!/usr/bin/python3
"""module containing an empty BaseGeomety class"""


class BaseGeometry:
    """an empty class"""
    def area(self):
        """ raises an error"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """method to validate input
        Args:
        name: name to input
        value: value to input
        Return: Nothing
        """
        if type(value) is not int:

            raise TypeError(f"{name:s} must be an integer")
        if value <= 0:
            raise ValueError(f"{name:s} must be greater than 0")
