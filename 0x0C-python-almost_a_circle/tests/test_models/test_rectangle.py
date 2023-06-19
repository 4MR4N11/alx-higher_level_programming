#!/usr/bin/python3
"""Unittest for rectangle.py"""
import unittest
from unittest.mock import patch
import io
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestRectangle(unittest.TestCase):
    """Unittests for testing the Rectangle class"""

    def test_weight_is_integer(self):
        """ test weight """
        r1 = Rectangle(9, 2)
        r2 = Rectangle(7, 5)
        r3 = Rectangle(13, 4, 0, 0, 5)

        self.assertEqual(r1.width, 9)
        self.assertEqual(r2.width, 7)
        self.assertEqual(r3.width, 13)
        with self.assertRaises(ValueError):
            Rectangle(-5, 3)
        with self.assertRaises(TypeError):
            Rectangle(1.5, 4)
        with self.assertRaises(TypeError):
            Rectangle(None, 3)
        with self.assertRaises(TypeError):
            Rectangle("hello", 9)
        with self.assertRaises(TypeError):
            Rectangle({1, 2}, 3)

    def test_height_is_integer(self):
        """ test height """
        r1 = Rectangle(9, 2)
        r2 = Rectangle(7, 5)
        r3 = Rectangle(13, 4, 0, 0, 5)

        self.assertEqual(r1.height, 2)
        self.assertEqual(r2.height, 5)
        self.assertEqual(r3.height, 4)
        with self.assertRaises(ValueError):
            Rectangle(5, -3)
        with self.assertRaises(TypeError):
            Rectangle(4, 1.5)
        with self.assertRaises(TypeError):
            Rectangle(3, None)
        with self.assertRaises(TypeError):
            Rectangle(10, "hello", 2, 0, 12)
        with self.assertRaises(TypeError):
            Rectangle(10, {1, 2}, 0, 0, 12)

    def test_x_is_integer(self):
        """ test x """
        r1 = Rectangle(10, 2, 0, 0, 12)
        r2 = Rectangle(10, 2, 3, 0, 12)

        self.assertEqual(r1.x, 0)
        self.assertEqual(r2.x, 3)
        with self.assertRaises(ValueError):
            Rectangle(10, 2, -3, 0, 12)
        with self.assertRaises(TypeError):
            Rectangle(10, 2, 3.5, 0, 12)
        with self.assertRaises(TypeError):
            Rectangle(10, 2, None, 0, 12)
        with self.assertRaises(TypeError):
            Rectangle(10, 2, (1, 2), 0, 12)
        with self.assertRaises(TypeError):
            Rectangle(10, 2, "hello", 0, 12)
        with self.assertRaises(TypeError):
            Rectangle(10, 2, {1, 2}, 0, 12)

    def test_y_is_integer(self):
        """ test y """
        r1 = Rectangle(10, 2, 0, 0, 12)
        r2 = Rectangle(10, 2, 3, 2, 12)

        self.assertEqual(r1.y, 0)
        self.assertEqual(r2.y, 2)
        with self.assertRaises(ValueError):
            Rectangle(10, 2, 0, -2, 12)
        with self.assertRaises(TypeError):
            Rectangle(10, 2, 3, 2.6, 12)
        with self.assertRaises(TypeError):
            Rectangle(10, 2, 0, None, 12)
        with self.assertRaises(TypeError):
            Rectangle(10, 2, 0, float('inf'), 12)
        with self.assertRaises(TypeError):
            Rectangle(10, 2, 1, (1, 2, 3), 12)
        with self.assertRaises(TypeError):
            Rectangle(10, 2, 0, "hello", 12)
        with self.assertRaises(TypeError):
            Rectangle(10, 2, 0, {1, 2}, 12)

    def test_area(self):
        """ test the area """
        r1 = Rectangle(10, 2, 0, 0, 12)
        r2 = Rectangle(10, 3, 3, 2, 12)

        self.assertEqual(r1.area(), 20)
        self.assertEqual(r2.area(), 30)
        with self.assertRaises(ValueError):
            r3 = Rectangle(10, -2, 0, 0, 12)
            r3.area()
        with self.assertRaises(ValueError):
            r4 = Rectangle(-10, 3, 3, 2, 12)
            r4.area()

    def test_update1(self):
        """ test without args """
        a = Rectangle(10, 10, 10, 10, 10)
        a.update()
        self.assertEqual('[Rectangle] (10) 10/10 - 10/10', str(a))

    def test_update2(self):
        """ test with 1 args """
        a = Rectangle(10, 10, 10, 10, 10)
        a.update(89)
        self.assertEqual("[Rectangle] (89) 10/10 - 10/10", str(a))

    def test_update3(self):
        """ test with 5 args """
        a = Rectangle(10, 10, 10, 10, 10)
        a.update(89, 1, 2, 3, 4)
        self.assertEqual("[Rectangle] (89) 3/4 - 1/2", str(a))

    def test_update4(self):
        """ test with id None """
        a = Rectangle(10, 10, 10, 10, 10)
        a.update(None)
        self.assertEqual("[Rectangle] (None) 10/10 - 10/10", str(a))

    def test_update5(self):
        """ test with id None and args """
        a = Rectangle(10, 10, 10, 10, 10)
        a.update(None, 1, 2, 3)
        self.assertEqual("[Rectangle] (None) 3/10 - 1/2", str(a))

    def test_update6(self):
        """ test with strings for width """
        a = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            a.update(89, "Hello!")

    def test_update7(self):
        """ test with 0 for width"""
        a = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            a.update(89, 0)

    def test_update8(self):
        """ test update with string for height """
        a = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            a.update(89, 1, "Hello!")

    def test_update9(self):
        """ test with 0 for height """
        a = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            a.update(89, 1, 0)

    def test_update10(self):
        """ test with string for x """
        a = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            a.update(89, 1, 2, "Hello!")

    def test_update11(self):
        """ test with negative for y """
        a = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            a.update(89, 1, 2, 3, -4)

    def test_to_dictionary(self):
        """test the to_dictionary method"""
        Base._Base__nb_objects = 0
        a = Rectangle(6, 2)
        output = {'id': 1, 'width': 6, 'height': 2, 'x': 0, 'y': 0}
        self.assertDictEqual(a.to_dictionary(), output)
        a = Rectangle(1, 3, 5)
        output = {'id': 2, 'width': 1, 'height': 3, 'x': 5, 'y': 0}
        self.assertDictEqual(a.to_dictionary(), output)
        a = Rectangle(4, 4, 1, 6)
        output = {'id': 3, 'width': 4, 'height': 4, 'x': 1, 'y': 6}
        self.assertDictEqual(a.to_dictionary(), output)
        a = Rectangle(2, 7, 4, 2, 18)
        output = {'id': 18, 'width': 2, 'height': 7, 'x': 4, 'y': 2}
        self.assertDictEqual(a.to_dictionary(), output)

    def test_str(self):
        """test the output of the instance when printed"""
        Base._Base__nb_objects = 0
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            print(Rectangle(4, 8))
        assert fake_stdout.getvalue() == '[Rectangle] (1) 0/0 - 4/8\n'
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            print(Rectangle(1, 3, 5, 7, 12))
        assert fake_stdout.getvalue() == '[Rectangle] (12) 5/7 - 1/3\n'

    def test_exception(self):
        """test with exception"""
        a = Rectangle(1, 2, 3, 4, 6)
        self.assertRaises(TypeError, a.to_dictionary, 0)
        a = Rectangle(1, 2)
        self.assertRaises(TypeError, a.to_dictionary, None)


if __name__ == "__main__":
    unittest.main()
