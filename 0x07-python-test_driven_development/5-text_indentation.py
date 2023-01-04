#!/usr/bin/python3
"""This module contains the function which checks for the characters
. : and ? and adds a new line after the characters thereby
indrnting the text.
"""


def text_indentation(text=None):
    """This function indents the text psssed as
    aruguement and prints the indented text
    Args:
    text: the text to be indented
    Return: Nothing
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    else:
        i = 0
        new_text = ""
        while (i < len(text)):
            if text[i] not in [":", "?", "."]:
                if text[i] == " " and i == 0:
                    while text[i] == " ":
                        i += 1
                    continue
                new_text += text[i]
            elif text[i] in [":", "?", "."]:
                new_text += text[i] + (2 * '\n')
                if i == len(text) - 1:
                    break
                elif text[i + 1] == " ":
                    i += 1
                    while text[i] == " ":
                        if i == len(text) - 1:
                            break
                        i += 1
                    continue
            i += 1
        print(f"{new_text}", end='')
