#!/usr/bin/python3
"""Square class"""


class Square():
    """Square class with private instance attribute size and raise errors
       and public instance method area and getter and setter
       and public instance method my_print"""
    def __init__(self, size=0):
        """__init__ method
        Args:
            size (int): size of square
        """
        self._size = size

    @property
    def size(self):
        """size getter
        Returns:
            int: size of square
        """
        return self._size

    @size.setter
    def size(self, value):
        """size setter
        Args:
            value (int): size of square
        """
        self._size = value
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

    def my_print(self):
        """my_print method
        Returns:
            prints square
        """
        if self._size == 0:
            print('')
        else:
            x = 0
            while x < self._size:
                y = 0
                while y < self._size:
                    print('#', end='')
                    y += 1
                print()
                x += 1
