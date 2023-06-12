#!/usr/bin/python3
"""Defines a function that returns True if the object is an instance"""


def inherits_from(obj, a_class):
    """Return True if the object is an instance"""
    return issubclass(type(obj), a_class) and type(obj) is not a_class
