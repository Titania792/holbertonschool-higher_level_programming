#!/usr/bin/python3
"""Write a function that confirms if an object is exactly an instance of a class"""


def is_same_class(obj, a_class):
    """
    returns True if the object is exactly an instance of the specified class ; otherwise False
    """
    return type(obj) == a_class
