#!/usr/bin/python3
"""Square class"""


class Square():
    """Square class with private instance attribute size and position,
       raise errors, public instance method area, getter and setter
       and public instance method my_print"""
    def __init__(self, size=0, position=(0, 0)):
        """__init__ method
        Args:
            size (int): size of square
            position (tuple): position of square
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """size getter
        Returns:
            int: size of square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """size setter
        Args:
            value (int): size of square
        """
        self.__size = value
        if not isinstance(self.__size, int):
            raise TypeError("size must be an integer")
        if self.__size < 0:
            raise ValueError("size must be >= 0")

    @property
    def position(self):
        """position getter
        Returns:
            tuple: position of square
        """
        return self.__position

    @position.setter
    def position(self, value):
        """position setter
        Args:
            value (tuple): position of square
        """
        self.__position = value
        if not isinstance(self.__position, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(self.__position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(self.__position[0], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(self.__position[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if self.__position[0] < 0 or self.__position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """area method
        Returns:
            int: area of square
        """
        return self.__size * self.__size

    def my_print(self):
        """my_print method
        Returns:
            prints square
        """
        p2 = 0
        if self.__size == 0:
            print()
        else:
            while p2 < self.__position[1] and self.__size != 0:
                print()
                p2 += 1
            i = 0
            while i < self.__size:
                p1 = 0
                y = 0
                while p1 < self.__position[0]:
                    print(' ', end='')
                    p1 += 1
                while y < self.__size:
                    print('#', end='')
                    y += 1
                print()
                i += 1
