#!/usr/bin/python3
"""Inheritance from class Ractangle"""


class Square(Rectangle):
    """ a square class that inherits from Rectangle class"""
    def __init__(self, size):
        """instantiation of the square class"""
        self.integer_validator("size", size)
        self.__size = size
    def area(self):
        """return the area of a square"""
        return (self.__size ** 2)
        
