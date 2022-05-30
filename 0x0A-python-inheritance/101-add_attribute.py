#!/usr/bin/python3
"""function that adds a new attribute"""


def add_attribute(a_class, a_name, a_value):
    """adding attribute if it's possible"""
    if hasattr(a_class, '__dict__'):
        setattr(a_class, a_name, a_value)
    else:
        raise TypeError("can't add new attribute")
