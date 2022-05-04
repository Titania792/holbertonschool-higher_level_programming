#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    nd = a_dictionary.copy()
    for key, value in nd.items():
        nd[key] = value * 2
    return nd
