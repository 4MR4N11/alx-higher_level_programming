#!/usr/bin/python3
def no_c(my_string):
    length = len(my_string)
    new_str = ""
    i = 0
    while i < length:
        if my_string[i] != 'c' and my_string[i] != 'C':
            new_str += str(my_string[i])
        i += 1
    return new_str
