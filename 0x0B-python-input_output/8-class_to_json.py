#!/usr/bin/python3
""" Module to serialize a class instance """


def class_to_json(obj):
    """method to return the dictionary description with
    simple data structure"""
    obj_dict = {}
    if hasattr(obj, "__dict__"):
        obj_dict = obj.__dict__.copy()
    return obj_dict
