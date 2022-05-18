#!/usr/bin/python3
"""Function that writes class Square and defines it by:
Private instance attribute
Instantiation with optional size
Public instance method"""


class Square:
    """Creating/defining Square class"""
    def __init__(self, size=0):
        """Initializes the class with the proper characteristics"""
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return (self.__size ** 2)

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
            self.__size = value

    def __lt__(self, comp):
        return self.area() < comp.area()

    def __le__(self, comp):
        return self.area() <= comp.area()

    def __eq__(self, comp):
        return self.area() == comp.area()

    def __ne__(self, comp):
        return self.area() != comp.area()

    def __ge__(self, comp):
        return self.area() >= comp.area()

    def __gt__(self, comp):
        return self.area() > comp.area()
