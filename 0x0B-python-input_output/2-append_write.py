#!/usr/bin/python3
"""append module"""


def append_write(filename="", text=""):
    """append to the end of a file"""
    with open(filename, "a", encoding="utf-8") as file:
        file.write(text)
        file.close()
        return len(text)
