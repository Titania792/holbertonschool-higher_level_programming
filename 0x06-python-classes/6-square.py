#!/usr/bin/python3
"""Function that writes class Square and defines it by:
Private instance attribute
Instantiation with optional size
Public instance method"""


class Square:
    """Creating/defining Square class"""
    def __init__(self, size=0, position=(0, 0)):
        """Initializes the class with the proper characteristics"""
        self.__size = size
        self.__position = position

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
    def position(self, size):
        if type(size) is not tuple or len(size) != 2 or \
                type(size[0]) is not int or type(size[1]) is not int or \
                size[0] < 0 or size[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = size

    def my_print(self):
        if self.__size == 0:
            print("")
        else:
            if self.__position[1] > 0:
                for i in range(self.__position[1]):
                    print("")
            for j in range(self.__size):
                for x in range(self.__position[0]):
                    print(' ', end="")
                for i in range(self.__size):
                    print("#", end="")
                print("")
