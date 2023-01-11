#!/usr/bin/python3
""" Module to convert object into string representation using json"""
import json

def to_json_string(my_obj):
    """ returns the serialized object"""
    return json.dumps(my_obj)
