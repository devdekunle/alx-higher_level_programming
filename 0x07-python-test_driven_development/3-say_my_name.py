#!/usr/bin/python3
""" This module print the name of the arguements of the function.
It also checks all edge cases to
make sure that the function works
efficiently.
"""


def say_my_name(first_name, last_name=""):
    """ the function prints thr first and last
    name while also checking all edge cases
    Args:
    first_name: first name
    last_name: last name
    Return: Nothing
    """
    if first_name is None:
        raise TypeError(r"say_my_name() missing 1 required \
        positional argument: 'first_name'")
    elif type(first_name) is not str:
        raise TypeError("first_name must be a string")
    elif type(last_name) is not str:
        raise TypeError("last_name must be a string")
    else:
        print("My name is {} {}".format(first_name, last_name))
