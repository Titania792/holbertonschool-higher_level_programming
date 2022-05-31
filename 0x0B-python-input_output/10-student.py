#!/usr/bin/python3
"""write a class"""


class Student:
    """student class"""

    def __init__(self, first_name, last_name, age):
        """Initialize class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """returns the dictionary representation of a Student instance"""
        if attrs is not None:
            return {key: value for key, value in self.__dict__.items() if key in attrs}
        return self.__dict__
