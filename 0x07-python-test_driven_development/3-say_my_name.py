#!/usr/bin/pyhton3
"""This module contains a function that prints a name"""


def say_my_name(first_name, last_name=""):
    """This function prints a name

    Args:
        first_name (str): The first name to print
        last_name (str): The last name to print

    Raises:
        TypeError: If first_name or last_name are not strings
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    elif type(last_name) is not str:
        raise TypeError("last_name must be a string")
    else:
        print("My name is {} {}".format(first_name, last_name))
