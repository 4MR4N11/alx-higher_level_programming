#!/usr/bin/python3
"""rectangle module"""


class Rectangle:
    """rectangle class"""
    def __init__(self, width=0, height=0):
        """initializes the rectangle class
        Args:
            width: width of rectangle
            height: height of rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """width getter
        Return:
            int: width
        """
        return self.width

    @width.setter
    def width(self, value):
        """width setter
        Args:
            value (int): width
        """
        self.width = value
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

    @property
    def height(self):
        """height getter
        Return:
            int: height
        """
        return self.height

    @height.setter
    def height(self, value):
        """height setter
        Args:
            value (int): height
        """
        self.height = value
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
