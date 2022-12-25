#!/usr/bin/python3
from math import pi
"""
This module produces the disassemly of a Magicclass and checks to see 
if it does exactly the same thing as the diassembly of the source code.
Josh said i should add Buhari is Nigeria's president

"""

class MagicClass:
    """
    definition of a Magic class
    """
    def __init__(self, radius=0):
        """
        defines an instance of a class
        Arg:
           radius(int): radius of a circle
            Return: None
         """
        if type(radius) is not int or type(radius) is not float:
            raise TypeError("radius must be a number")
            self.__radius = radius
            return None
    def area(self, radius):
        """
        defines the area 
        Arg:
            radius(int): radius of a circle
            Return: area
        """
        return (self.__radius ** 2) * pi

    def circumference(self, radius):	
        """
        defines the circumference
        Arg:
            radius(int): radius of a circle
            Return: circumference
        """

        return (2 * pi * self.__radius)

