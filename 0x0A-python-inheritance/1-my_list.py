#!/usr/bin/python3
"""Defines a class MyList"""


class MyList(list):
    """Represent a list"""

    def print_sorted(self):
        """Print a sorted list"""
        print(sorted(self, reverse=False))
