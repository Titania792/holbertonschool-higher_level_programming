#!/usr/bin/python3
"""function that returns a list object containing all attributes
and methods of an object"""


def lookup(obj):
    """
    returns the list
    """
    return list(dir(obj))
