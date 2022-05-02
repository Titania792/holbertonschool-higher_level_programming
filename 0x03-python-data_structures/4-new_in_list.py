#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if my_list:
        b = my_list.copy()
        if idx < 0 or idx >= len(my_list):
            return b
        else:
            b[idx] = element
            return b
