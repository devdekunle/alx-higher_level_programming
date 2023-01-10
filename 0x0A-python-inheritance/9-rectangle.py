#!/usr/bin/python3
""" module to inherit from BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ class inherits from BaseGeometry"""
    def __init__(self, width, height):
        """validate input with BaseGeometry"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """ get the area of a rectangle"""
        return (self.__height * self.__width)

    def __str__(self):
        """print the object"""
        return f"[Rectangle] {self.__width}/{self.__height}"
