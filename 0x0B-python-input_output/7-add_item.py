#!/usr/bin/python3
""" Module to load, add and save objects using json"""

from sys import argv
import json
import os
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


filename = "add_item.json"
if os.path.isfile(filename):
    my_obj = load_from_json_file(filename)
else:
    my_obj = []
my_obj.extend(argv[1:])
save_to_json_file(my_obj, filename)
