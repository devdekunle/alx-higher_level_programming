#!/udsr/bin/python3
"""Module to find the max integer ina list
"""


def max_integer(list=[]):
    """Function to find and return th ,ax integer in a list
    of integers. If the list is empty, the function returns None
    """
    if len(list) == 0:
        return None
    result = list[0]
    i = 0
    while i < len(list):
        if type(list[i]) is not int:
            raise TypeError("list must be a list of integers")
        elif list[i] > result:
            result = list[i]
        i += 1
    return result
