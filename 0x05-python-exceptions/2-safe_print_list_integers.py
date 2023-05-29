#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    try:
        i = 0
        for n in range(x):
            if isinstance(my_list[n], int):
                print("{:d}".format(my_list[n]), end='')
                i += 1
    except (TypeError, ValueError):
        pass
    print()
    return i
