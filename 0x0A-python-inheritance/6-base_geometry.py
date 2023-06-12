#!/usr/bin/python3
"""Defines a class BaseGeometry"""


class BaseGeometry:
    """Empty class with a public instance method area() that raises an
    Exception"""
    def area(self):
        """Raise an Exception"""
        raise Exception("area() is not implemented")
