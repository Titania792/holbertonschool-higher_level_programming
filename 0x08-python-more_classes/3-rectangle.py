#!/usr/bin/python3
"""Function that writes class Rectangle and defines it by:
Private instance attribute
Instantiation with optional
Public instance method"""


class Rectangle:
    """Creating/defining Rectangle class"""
    def __init__(self, width=0, height=0):
        """Initializes the class with the proper characteristics"""
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return (self.__height * self.__width)

    def perimeter(self):
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return ((self.__height * 2) + (self.__width * 2))

    def __str__(self):
        out = ""
        if self.__height == 0 or self.__width == 0:
            return out
        else:
            for j in range(self.__height):
                for i in range(self.__width):
                    out += "#"
                out += "\n"
        return out[:-1]
