#!/usr/bin/python3
""" check if an onject is an instance of a subclass"""


def inherits_from(obj, a_class):
    """check for a subclass"""
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
