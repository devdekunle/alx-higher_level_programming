#!/usr/bin/python3

""" This module contains the definition of an empty class Rectangle which
defines a rectangle
"""


class Rectangle:

    """This class defines a rectangle
    """
    def __init__(self, width=0, height=0):
        """
        method to iniialize an instance of a class
        Args:
        width:set the width
        height: set the height
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ return the value of the width
        Return: width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """sets the width to a given value
        Args:
        value: value to set
        Return: Nothing
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ return the value of the width
        Return: height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """sets the height to a given value
        Args:
        value: value to set
        Return: Nothing
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
