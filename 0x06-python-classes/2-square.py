#!/usr/bin/python3
"""Function that writes a class Square and defines it by:
private instance attribute 'size'"""


class Square:
    """Creating/defining Square class"""
    def __init__(self, size=0):
        """Initializes the class with the proper characteristics"""
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
