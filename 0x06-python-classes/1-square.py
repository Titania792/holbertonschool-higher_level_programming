#!/usr/bin/python3
"""function that writes a class called 'Square' and defines it by:
private instance attribute 'size' and instantiation
with size (no type/value verification)"""


class Square:
    """Creating/defining Square class"""
    def __init__(self, size):
        """Initializes the class with the proper characteristics"""
        self.__size = size
