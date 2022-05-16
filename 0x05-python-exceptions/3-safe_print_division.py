#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        res = a/b
    except ZeroDivisionError:
        return None
    finally:
        print("Inside result:{:d}".format(res))
        return res
