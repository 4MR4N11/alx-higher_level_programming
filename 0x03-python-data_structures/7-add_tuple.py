#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    new_tuple = ()
    tmp1 = 0
    tmp2 = 0
    i = 0
    while i < len(tuple_a) and i < 2:
        if i == 0:
            tmp1 += tuple_a[i]
        else:
            tmp2 += tuple_a[i]
        i += 1
    i = 0
    while i < len(tuple_b) and i < 2:
        if i == 0:
            tmp1 += tuple_b[i]
        else:
            tmp2 += tuple_b[i]
        i += 1
    new_tuple = (tmp1, tmp2)
    return new_tuple
