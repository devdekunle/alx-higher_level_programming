#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list is None or len(my_list) == 0:
        return None
    largest_val = my_list[0]
    for num in my_list:
        if num > largest_val:
            largest_val = num
    return largest_val
