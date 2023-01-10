#!/usr/bin/python3
""" check if an onject is an instance of a subclass"""
def inherits_from(obj, a_class):
    """check for a subclass"""
    return (issubclass(typeof(obj), a_class) and typeof(obj) != a_class)
