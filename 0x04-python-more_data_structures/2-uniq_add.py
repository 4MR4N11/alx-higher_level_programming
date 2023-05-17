#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    index = 0
    for i in my_list:
        if index == my_list.index(i):
            sum += i
        index += 1
    return sum
