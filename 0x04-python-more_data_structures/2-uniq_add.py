#!/usr/bin/python3
def uniq_add(my_list=[]):
    u_num = set(my_list)
    l_num = list(u_num)
    res = 0
    for i in range(len(l_num)):
        res = res + l_num[i]
        i += 1
    return res
