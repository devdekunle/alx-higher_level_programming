#!/usr/bin/python3
"""Module to convert class instance of student class to json"""


class Student:
    """defining the class student"""

    def __init__(self, first_name, last_name, age):
        """object instantaition"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """receives dictionary representation"""
        obj_dict = self.__dict__.copy()
        if type(attrs) is not list:
            return obj_dict
        """ if attrs is a list, we loop through attrs to
            check for strings"""
        for string in attrs:
            if type(string) is not str:
                return obj_dict

        new_obj = {}
        """ loop through each element of the list and compare
        with corresponding key of dict"""
        i = 0
        while (i < len(attrs)):
            for key in obj_dict:
                if attrs[i] == key:
                    new_obj[key] = obj_dict[key]
            i += 1
        return new_obj
