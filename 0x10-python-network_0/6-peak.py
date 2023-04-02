#!/usr/bin/python3
"""
Technical interview preparation
Write a function that finds a peak in a list of unsorted integers.

Prototype: def find_peak(list_of_integers):
You are not allowed to import any module
Your algorithm must have the lowest complexity
(hint: you don’t need to go through all numbers to find a peak)
6-peak.py must contain the function
6-peak.txt must contain the complexity of your algorithm:
O(log(n)), O(n), O(nlog(n)) or O(n2)
Note: there may be more than one peak in the list
"""


def find_peak(list_of_integers):
    """
    function to find a peak in a list of integers
    A peak is a number in a list of unsorted integers,
    where its value is greater or equal to its adjacent integers
    that is left and right neighbours
    """
    if list_of_integers is None:
        return
    if len(list_of_integers) == 0:
        return None

    else:
        i = 0
        if type(list_of_integers[i]) is not int\
        or type(list_of_integers[i + 1]) is not int:
            raise TypeError("list must be a list of integers")
        elif list_of_integers[i] >= list_of_integers[i + 1]:
            return list_of_integers[i]
        else:
            i += 1
            while i < len(list_of_integers):
                if type(list_of_integers[i]) is not int\
                    or type(list_of_integers[i - 1]) is not int\
                    or type(list_of_integers[i + 1]) is not int:
                    raise TypeError("list must be a list of integers")
                if list_of_integers[i] >= list_of_integers[i - 1] and\
                    list_of_integers[i] >= list_of_integers[i + 1]:
                    return list_of_integers[i]

                else:
                    i += 1
