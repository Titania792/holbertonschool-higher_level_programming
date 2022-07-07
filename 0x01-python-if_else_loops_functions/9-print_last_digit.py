#!/usr/bin/python3
def print_last_digit(number):
    """print last digit"""
    if number < 0:
        number = -number
    print(number % 10, end='')
    return number % 10
