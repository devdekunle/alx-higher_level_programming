#!usr/bin/python3
""" This module contains a function that adds 2 integers
    and also checking all possible edge cases for different 
    values of a and b.
    it also typecasts the value if it is a float so as to esure that the returned
    value is an integert
"""
def add_integer(a, b=98):
    """This function adds two integers
    Args:
    a: First  arguement
    b:second arguement
    Return: sum
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    elif type(b) not in [int, float]:
       raise TypeError("b must be an integer")
    elif a is None:
        raise TypeError("add_integer() missing 1 required positional argument: 'a'")
    return (int(a) + int(b))
