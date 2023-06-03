#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Class to test the max_integer function"""

    def test_max_integer(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_max_integer_empty(self):
        self.assertEqual(max_integer([]), None)

    def test_max_integer_negative(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([-12, -3, -4, -2]), -2)

    def test_max_integer_float(self):
        self.assertEqual(max_integer([1.1, 2.2, 3.3, 4.4]), 4.4)
        self.assertEqual(max_integer([1.1, 3.3, 4.4, 2.2]), 4.4)

    def test_max_integer_string(self):
        self.assertEqual(max_integer("Hello"), 'o')
        self.assertEqual(max_integer("Hello"), 'o')

    def test_max_integer_tuple(self):
        self.assertEqual(max_integer((1, 2, 3, 4)), 4)
        self.assertEqual(max_integer((1, 3, 4, 2)), 4)
        self.assertEqual(max_integer((4, 3, 2, 1)), 4)

    def test_max_integer_list_of_strings(self):
        self.assertEqual(max_integer(["Hello", "World"]), 'World')

    def test_max_integer_list_of_tuples(self):
        self.assertEqual(max_integer([(1, 2), (3, 4)]), (3, 4))

    def test_max_integer_list_of_lists(self):
        self.assertEqual(max_integer([[1, 2], [3, 4]]), [3, 4])

    def test_max_integer_list_of_floats(self):
        self.assertEqual(max_integer([1.1, 2.2, 3.3, 4.4]), 4.4)
        self.assertEqual(max_integer([1.1, 3.3, 4.4, 2.2]), 4.4)
