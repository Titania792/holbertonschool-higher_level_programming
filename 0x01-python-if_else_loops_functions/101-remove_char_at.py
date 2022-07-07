#!/usr/bin/python3
def remove_char_at(str, n):
    """remove char at n"""
    if n < 0:
        cpstr = str
    else:
        cpstr = str[:n] + str[n+1:]
    return cpstr
