#!/usr/bin/python3
""" This module cotains the function which prints a square based 
    on the size that has been passed to the function.
    It also checks all possible egde cases to make sure
    that the function works effectively.
"""

def print_square(size=None):
    """method which creates a square based on the size
    Args:
    size: the size of the square to print
    Return: Nothing
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    elif type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    else:
        for i in range(size):
          print(f"{size * '#'}")
