#!/usr/bin/python3
"""Write to file module"""


def write_file(filename="", text=""):
    """write to file function"""
    with open(filename, "w", encoding="utf-8") as file:
        file.write(text)
    file.close()
    return len(text)
