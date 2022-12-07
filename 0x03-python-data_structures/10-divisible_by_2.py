#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    nw_list = []
    for i in my_list:
        if i % 2 == 0:
            nw_list.append(True)
        else:
            nw_list.append(False)
    return nw_list
