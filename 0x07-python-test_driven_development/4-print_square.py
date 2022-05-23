#!/usr/bin/python3
"""function that prints a square"""


def print_square(size):
    """this function prints a square with the character #"""
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    print(((("#" * size) + "\n") * size)[:-1])