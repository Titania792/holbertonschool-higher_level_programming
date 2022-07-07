#!/usr/bin/python3
def remove_char_at(str, n):
    """remove char at n"""
    cpstr = str[:n] + str[n+1:]
    return cpstr
