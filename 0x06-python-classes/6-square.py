#!/usr/bin/python3

class Square():
    """Square class"""
    def __init__(self, size=0, position=(0, 0)):
        """__init__ method
        Args:
            size (int): size of square
            position (tuple): position of square
        """
        self._size = size
        self._position = position

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

    @property
    def position(self):
        """position getter
        Returns:
            tuple: position of square
        """
        return self._position

    @position.setter
    def position(self, value):
        """position setter
        Args:
            value (tuple): position of square
        """
        self._position = value
        if not isinstance(self._position, tuple) and len(self._position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not isinstance(self._position[0], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not isinstance(self._position[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")

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
        p2 = 0
        while p2 < self._position[1]:
            print()
            p2 += 1
        i = 0
        while i < self._size:
            p1 = 0
            y = 0
            while p1 < self._position[0]:
                print(' ', end='')
                p1 += 1
            while y < self._size:
                print('#', end='')
                y += 1
            print()
            i += 1
