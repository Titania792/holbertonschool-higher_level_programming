#!/usr/bin/python3
"""Function that writes class Square and defines it by:
Private instance attribute
Instantiation with optional size
Public instance method"""


class Square:
    """Creating/defining Square class"""
    def __init__(self, size=0, position=(0, 0)):
        """Initializes the class with the proper characteristics"""
        self.size = size
        self.position = position

    def area(self):
        return (self.__size ** 2)

    @property
    def size(self):
        return self.__size

    @property
    def position(self):
        return self.__position

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @position.setter
    def position(self, value):
        if (len(value) != 2 or type(value) is not tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if (value[0] < 0 or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        if (type(value[0]) != int or type(value[1]) != int):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        if self.__size == 0:
            print("")
        else:
            if self.__position[1] > 0:
                for i in range(self.__position[1]):
                    print("")
            for j in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
