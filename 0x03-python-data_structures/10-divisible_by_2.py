#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    nList = my_list.copy()
    i = 0
    for x in my_list:
        if x % 2 == 0:
            nList[i] = True
        else:
            nList[i] = False
        i += 1
    return nList
