#!/usr/bin/python3
"""write a class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """creating class"""

    def __init__(self, width, height):
        """initializing"""
        self.__width = self.integer_validator("width", width)
        self.__height = self.integer_validator("height", height)

    def area(self):
        """returns area"""
        return (self.__height * self.__width)

    def __str__(self):
        """returns string"""
        return (f"[Rectangle] {self.__width}/{self.__height}")
