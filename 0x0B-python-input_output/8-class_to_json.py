#!/usr/bin/python3
""" Module to serialize a class instance """
import json


def class_to_json(obj):
    """method to return the dictionary description with
    simple data structure"""
    obj_str = json.dumps(obj.__dict__)
    return obj_str
