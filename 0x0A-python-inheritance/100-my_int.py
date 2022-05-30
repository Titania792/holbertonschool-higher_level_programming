#!/usr/bin/python3
"""Write a class MyInt"""


class MyInt(int):
    """inherits from int"""

    def __eq__(self, other):
        return self.real != other.real

    def __ne__(self, other):
        return self.real == other.real
