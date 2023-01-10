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
