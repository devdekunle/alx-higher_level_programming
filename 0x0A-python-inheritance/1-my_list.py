#!/usr/bin/python3
"""This module is has a subclass that inherita a super class
    """


class MyList(list):
    """This class deffines a method to print a sorted list
    """
    def __init__(self):
        """initialize the object using the preferred class"""
        super().__init__()

    def print_sorted(self):
        """This method returns a sorted list"""
        print(sorted(self))
