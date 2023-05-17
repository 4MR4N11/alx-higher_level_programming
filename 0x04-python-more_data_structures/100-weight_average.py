#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list:
        res = 0
        tmp = 0
        for x, y in my_list:
            res += x * y
            tmp += y
        res = res / tmp
        return res
    return 0
