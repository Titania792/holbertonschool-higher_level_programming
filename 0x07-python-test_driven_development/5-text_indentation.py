#!/usr/bin/python3
"""function that prints text"""


def text_indentation(text):
    """this function prints a text with 2 new lines
    after each of these characters: ., ? and :"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    txt1 = text.replace(". ", ".\n\n")
    txt2 = txt1.replace("? ", "?\n\n")
    txt3 = txt2.replace(": ", ":\n\n")
    print(txt3, end="")