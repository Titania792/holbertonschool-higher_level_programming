#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list:
        a = []
        for i in my_list:
            if my_list[i] % 2 == 0:
                a.insert(i, True)
            else:
                a.insert(i, False)
        return a
