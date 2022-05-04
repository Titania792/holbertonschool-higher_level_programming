#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    cpd = a_dictionary.copy()
    for key in cpd:
        if cpd[key] == value:
            del a_dictionary[key]
    return a_dictionary
