#!/usr/bin/python3
"""This module contains the function which checks for the characters . : and ? and adds a new line after the characters thereby indrnting the text.
"""
def text_indentation(text):
    """This function indents the text psssed as aruguement and prints the indented text
    Args: 
    text: the text to be indented
    Return: Nothing
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    elif text is None:
        raise TypeError(" text_indentation missing 1 required positional argument: 'text'")
    else:
        i = 0
        new_text = ""
        while (i < len(text)):
                
            if text[i] not in [":", "?", "."]:
                new_text += text[i]
            elif text[i] in [":", "?", "."]:
                new_text += text[i] + (2 * "\n")
                i += 1
                if text[i] == " ":
                    while(text[i] == " "):
                        i += 1
                continue
            i += 1
        print(new_text)               
