#!/usr/bin/python3
def no_c(my_string):
    arry = list(my_string)
    for i in arry:
        while "c" in arry:
            arry.remove("c")
        while "C" in arry:
            arry.remove("C")
        my_string = "".join(str(i) for i in arry)
    return my_string
