#!/usr/bin/python3

""" This module contains the definition of an empty class Rectangle which
defines a rectangle
"""


class Rectangle:

    """This class defines a rectangle
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        method to iniialize an instance of a class
        Args:
        width:set the width
        height: set the height
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
        if self.width == 0 or self.height == 0:
            return ptr_rect
        for i in range(self.height):
            ptr_rect += (self.width * str(self.print_symbol) + "\n")
        return ptr_rect[:-1]

    def __repr__(self):
        """ This method returns an representation of a class method
        that can be parsed to o create a new instance
        Return: pt
        """
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """This method returns a string when an instance
        of the class is deleted
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """This method compares the area of two different class
        instances
        Arg:
        rect_1: first rectangle
        rect_2: second rectangle
        Return: biggest area
        """
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        else:
            if rect_1.area() >= rect_2.area():
                return rect_1
            else:
                return rect_2
