#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    i = 0
    for elem in my_list:
            try:
                print("{:d}".format(my_list[i]), end="")
            except ValueError:
                pass
            else:
                i += 1
    print("")
    return i
