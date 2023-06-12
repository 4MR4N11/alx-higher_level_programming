#!/usr/bin/python3
"""Defines a class BaseGeometry"""


class BaseGeometry:
    """Empty class with a public instance method area() that raises an
    Exception and a public instance method integer_validator() that validates
    value"""
    def area(self):
        """Raise an Exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate value"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
