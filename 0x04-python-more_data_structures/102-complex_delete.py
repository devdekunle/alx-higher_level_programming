#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for key, res in sorted(a_dictionary.items()):
        if res == value:
            del a_dictionary[key]
    return a_dictionary
