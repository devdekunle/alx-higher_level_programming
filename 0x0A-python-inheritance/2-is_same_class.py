#!/usr/bin/python3
""" module to check if sn onject is an instance of a class"""


def is_same_class(obj, a_class):
    """returns a booleans if an object is an instance of a class"""
    return (type(obj) == a_class)
