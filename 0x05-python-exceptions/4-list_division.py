#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    nlist = []
    for i in range(list_length):
        try:
            res = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
            res = 0
        except (TypeError, ValueError):
            print("wrong type")
            res = 0
        except IndexError:
            print("out of range")
            res = 0
        finally:
            nlist.append(res)
    return (nlist)
