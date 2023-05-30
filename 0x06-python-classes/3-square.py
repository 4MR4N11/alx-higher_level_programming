#!/usr/bin/python3

class Square():
    """Square class"""
    def __init__(self, size=0):
        """__init__ method
        Args:
            size (int): size of square
        """
        self._size = size
        if not isinstance(self._size, int):
            raise TypeError("size must be an integer")
        if self._size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """area method
        Returns:
            int: area of square
        """
        return self._size * self._size
