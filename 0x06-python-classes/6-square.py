#!/usr/bin/python3

class Square():
    def __init__(self, size=0, position=(0, 0)):
        self._size = size
        self._position = position

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        self._size = value
        if not isinstance(self._size, int):
            raise TypeError("size must be an integer")
        if self._size < 0:
            raise ValueError("size must be >= 0")

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, value):
        self._position = value
        if not isinstance(self._position, tuple) and len(self._position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not isinstance(self._position[0], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not isinstance(self._position[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        return self._size * self._size

    def my_print(self):
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
