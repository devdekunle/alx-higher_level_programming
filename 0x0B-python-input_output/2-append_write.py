#!/usr/bin/python3
""" Module to append to a file"""


def append_write(filename="", text=""):
    """return numbr of characters appended"""
    with open(filename, mode="a", encoding="utf-8") as my_file:
       len_append = my_file.write(text) 
       return len_append
