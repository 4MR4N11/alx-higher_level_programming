#!/usr/bin/python3
"""Defines a class Square that inherits from Rectangle (9-rectangle.py)"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """a class Square"""
    def __init__(self, size):
        """Instantiation with size"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Return the area of the Square"""
        return self.__size ** 2
