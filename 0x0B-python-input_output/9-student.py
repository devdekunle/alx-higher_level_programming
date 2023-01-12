#!/usr/bin/python3
"""Module to convert class instance of student class to json"""


class Student:
    """defining the class student"""

    def __init__(self, first_name, last_name, age):
        """object instantaition"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """receives dictionary representation"""
        return self.__dict__.copy()
        
