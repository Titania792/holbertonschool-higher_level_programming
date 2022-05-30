#!/usr/bin/python3
"""Write a class MyList"""


class MyList(list):
    """inherits from list"""

    def print_sorted(self):
        """prints the list in ascending order"""
        print(sorted(self))
