#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    i = 0
    for elem in my_list:
        if (i < x):
            try:
                print("{}".format(my_list[i]), end="")
                i += 1
            except IndexError:
                print("\n")
    print("")
    return i
