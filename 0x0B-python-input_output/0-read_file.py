#!/usr/bin/python3
""" Module to read a file and print it"""


def read_file(filename=""):
    """ function to read a file and print it"""
    with open(filename, encoding="utf-8") as my_file:
        read_file = my_file.read()
        print(read_file, end='')
