#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    try:
        i = 0
        for n in my_list:
            if i < x:
                print(n, end='')
                i += 1
    except IndexError:
        pass
    print()
    return i
