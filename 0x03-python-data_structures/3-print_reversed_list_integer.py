#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    copy_list = my_list.copy()
    copy_list.reverse()
    for i in copy_list:
        print("{:d}".format(i))
