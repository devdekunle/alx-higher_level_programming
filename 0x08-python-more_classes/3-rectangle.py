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

    def area(self):
        """This method returns the area of a rectangle
        Args:
        Return: Area of a rectangle
        """
        return (self.height * self.width)

    def perimeter(self):
        """This method gets the perimeter of arectangle and returns it
        Args:
        Return: perimeter
        """
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return 2 * (self.height + self.width)

    def __str__(self):
        """ This method make an object printable
        Return: ptr_rect
        """
        ptr_rect = ""
        for i in range(self.height):
            ptr_rect += (self.width * "#") + "\n"
        return ptr_rect[:-1]
