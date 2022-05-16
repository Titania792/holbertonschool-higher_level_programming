#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError) as wrong:
        print("Exception: {}".format(wrong), file=sys.stderr)
        return False
