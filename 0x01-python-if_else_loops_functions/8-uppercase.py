#!/usr/bin/python3
def uppercase(str):
    for char in str:
        if ord(char) >= 97 and ord(char) <= 122:
            print("{:s}".format(chr(ord(char) - 32)), end='')
        else:
            print("{:s}".format(char), end='')
    print("\n", end='')
