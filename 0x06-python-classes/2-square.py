#!/usr/bin/python3
"""Square class"""


class Square():
    """Square class with private instance attribute size and raise errors"""
    def __init__(self, size=0):
        """__init__ method
        Args:
            size (int): size of square
        """
        self.__size = size
        if not isinstance(self.__size, int):
            raise TypeError("size must be an integer")
        if self.__size < 0:
            raise ValueError("size must be >= 0")
