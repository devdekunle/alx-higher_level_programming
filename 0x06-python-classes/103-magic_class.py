#!/usr/bin/python3
from math import pi
class MagicClass:
        def __init__(self, radius=0):
                if type(radius) is not int or type(radius) is not float:
                        raise TypeError("radius must be a number")
                self.__radius = radius
                return None
        def area(self, radius):
                return (self.__radius ** 2) * pi

        def circumference(self, radius):
                return (2 * pi * self.__radius)

