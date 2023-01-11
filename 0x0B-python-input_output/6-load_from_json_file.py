#!/usr/bin/python3
""" Module to load an object from a json file that means
    to deserialize an object from a json file"""
import os
import json


def load_from_json_file(filename):
    """load an object from a json file"""
    with open(filename, encoding="utf-8") as my_file:
        return json.load(my_file)
