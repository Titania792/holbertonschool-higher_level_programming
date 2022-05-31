#!/usr/bin/python3
"""Write a function that appends a string at the end of a text file"""


def append_write(filename="", text=""):
    """append a file"""
    with open(filename, "a") as f:
        return f.write(text)
