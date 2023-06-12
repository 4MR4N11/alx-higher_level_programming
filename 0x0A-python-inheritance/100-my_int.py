#!/usr/bin/python3
"""Defines a class MyInt"""


class MyInt(int):
    """Represent an int with == and != operators inverted"""

    def __ne__(self, other):
        """Return True if both objects are equal"""
        return int(self) == int(other)

    def __eq__(self, other):
        """Return True if both objects are not equal"""
        return int(self) != int(other)
