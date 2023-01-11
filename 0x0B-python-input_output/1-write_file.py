#!/usr/bin/python3
""" Module to write to a file"""


def write_file(filename="", text=""):
    """ function to write toa file"""
    with open(filename, mode="w", encoding="utf-8") as my_file:
        my_file.write(text)

    with open(filename, encoding="utf-8") as my_file:
        line = my_file.read()
    return len(line)
