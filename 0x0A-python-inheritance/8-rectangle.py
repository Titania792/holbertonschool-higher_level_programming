#!/usr/bin/python3
"""write a class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """creating class"""

    def __init__(self, width, height):
        """initializing"""
        self.__width = self.integer_validator("width", width)
        self.__height = self.integer_validator("height", height)
