#!/usr/bin/python3
"""Write a function that writes a string to a text file"""


def write_file(filename="", text=""):
    """write a file"""
    with open(filename, "w") as f:
        return f.write(text)
