#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    large = 0
    while l < x:
        try:
            print("{}".format(my_list[large]), end="")
        except IndexError:
            break
        large += 1
    print("")
    return (large)
