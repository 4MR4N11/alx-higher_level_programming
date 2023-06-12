#!/usr/bin/python3
"""Defines a class BaseGeometry"""


class BaseGeometry:
    """a class with a public instance method area() that raises an
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


"""Defines a class Rectangle that inherits from BaseGeometry"""


class Rectangle(BaseGeometry):
    """a class Rectangle"""
    def __init__(self, width, height):
        """Instantiation with width and height"""
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)
