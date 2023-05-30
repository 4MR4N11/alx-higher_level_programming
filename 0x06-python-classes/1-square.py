#!/usr/bin/python3
"""Square class"""


class Square():
    """Square class with private instance attribute size"""
    def __init__(self, size=0):
        """__init__ method.

        Args:
            size (int): size of square

        """
        self._size = size
