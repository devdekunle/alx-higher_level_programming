#!/usr/bin/python3
"""Inheritance from class Ractangle"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ a square class that inherits from Rectangle class"""
    def __init__(self, size):
        """instantiation of the square class"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """return the area of a square"""
        return (self.__size ** 2)

    def __str__(self):
        """make then object printable"""
        return f"[Square] {self.__size}/{self.__size}"
