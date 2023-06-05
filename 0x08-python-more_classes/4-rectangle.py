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
        self.__width = width
        self.__height = height
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if height < 0:
            raise ValueError("height must be >= 0")

    @property
    def width(self):
        """width getter
        Return:
            int: width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """width setter
        Args:
            value (int): width
        """
        self.__width = value
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

    @property
    def height(self):
        """height getter
        Return:
            int: height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """height setter
        Args:
            value (int): height
        """
        self.__height = value
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

    def area(self):
        """area method
        Return:
            area of the rectangle
        """
        return self.__height * self.__width

    def perimeter(self):
        """perimeter method
        Return:
            the rectangle perimeter
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__height + self.__width)

    def __str__(self):
        """str method
        Return:
            string representation of the rectangle
        """
        str = ""
        i = 0
        if self.__width == 0 or self.__height == 0:
            return str
        while i < self.__height:
            j = 0
            while j < self.__width:
                str += '#'
                j += 1
            i += 1
            if i < self.__height:
                str += '\n'
        return str

    def __repr__(self):
        """repr method
        Return:
            string representation of the rectangle
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)
