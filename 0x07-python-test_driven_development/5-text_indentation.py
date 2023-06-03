#!/usr/bin/python3

"""This module contains a function that prints a text with 2 new lines after
 each of these characters: ., ? and :"""


def text_indentation(text):
    if type(text) is not str:
        raise TypeError("text must be a string")
    i = 0
    while i < len(text):
        if text[i] == '.' or text[i] == '?' or text[i] == ':':
            print(text[i], end='')
            i += 1
            while i < len(text) and (text[i].isspace() or text[i] == '\n'):
                i += 1
            print('\n')
        print(text[i], end='')
        i += 1
