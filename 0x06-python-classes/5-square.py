#!/usr/bin/python3

class Square():
    def __init__(self, size=0):
        self._size = size

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

    def area(self):
        return self._size * self._size

    def my_print(self):
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
