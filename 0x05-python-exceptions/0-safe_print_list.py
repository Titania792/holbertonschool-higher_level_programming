#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    l = 0
    while l < x:
        try:
             print("{}".format(my_list[l]), end = "")
        except IndexError:
            break
        l += 1
    print("")
    return (l)
