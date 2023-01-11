#!/usr/bin/python3
""" Module to save an object to a file in json representation
    also same as saving a serialized object(converted to a string)
    in a file"""
import os
import json


def save_to_json_file(my_obj, filename):
    """This function writes an object to a file in
        json represntation"""
    with open(filename, mode="w", encoding="utf-8") as my_file:
        json.dump(my_obj, my_file)
