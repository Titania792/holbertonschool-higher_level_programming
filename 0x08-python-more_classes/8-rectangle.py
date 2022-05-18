#!/usr/bin/python3
"""Function that writes class Rectangle and defines it by:
Private instance attribute
Instantiation with optional
Public instance method"""


class Rectangle:
    """Creating/defining Rectangle class"""
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Initializes the class with the proper characteristics"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
                    out += str(self.print_symbol)
                out += "\n"
        return out[:-1]

    def __repr__(self):
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        area1 = rect_1.area
        area2 = rect_2.area
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if (area2() > area1()):
            return rect_2
        else:
            return rect_1
