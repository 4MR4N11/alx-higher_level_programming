#!/usr/bin/python3
"""rectangle module"""


class Rectangle:
    """rectangle class"""

    number_of_instances = 0
    print_symbol = "#"

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
        Rectangle.number_of_instances += 1

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
        rectangle = ""
        i = 0
        if self.__width == 0 or self.__height == 0:
            return rectangle
        while i < self.__height:
            j = 0
            while j < self.__width:
                rectangle += str(self.print_symbol)
                j += 1
            i += 1
            if i < self.__height:
                rectangle += '\n'
        return rectangle

    def __repr__(self):
        """repr method
        Return:
            string representation of the rectangle
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """del method
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """bigger or equal method"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        area1 = rect_1.__height * rect_1.__width
        area2 = rect_2.__height * rect_2.__width
        if area1 < area2:
            return rect_2
        else:
            return rect_1

    @classmethod
    def square(cls, size=0):
        """square class method
        Args:
            size: size of square
        """
        return cls(size, size)
