#!/usr/bin/python3
""" Module to deserialize a string. That is to convert it from a string 
    to an object"""

import json


def from_json_string(my_str):
    """ return a deserialized string"""
    return json.loads(my_str)
