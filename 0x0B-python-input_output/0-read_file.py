#!/usr/bin/python3
"""Write a function that reads a text file and prints it to stdout"""


def read_file(filename=""):
    """read a file"""
    with open(filename, "r") as f:
        print(f.read())
