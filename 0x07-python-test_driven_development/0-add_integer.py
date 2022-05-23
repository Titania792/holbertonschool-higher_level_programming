#!/usr/bin/python3
"""aaa"""


def add_integer(a, b=98):
    """bbb"""
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    
    return int(a) + int(b)
