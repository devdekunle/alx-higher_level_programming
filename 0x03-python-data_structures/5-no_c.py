#!/usr/bin/python3
def no_c(my_string):
    res = []
    for letter in my_string:
        if letter != 'c' and letter != 'C':
            res.append(letter)
    return ''.join(res)
