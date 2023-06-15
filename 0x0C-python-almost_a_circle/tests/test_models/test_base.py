#!/usr/bin/python3
"""Unittest for base.py"""
import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class Test_Base(unittest.TestCase):
    """Test cases for Base class"""

    def setUp(self):
        """Set up test methods"""
        Base._Base__nb_objects = 0

    def test_base_id(self):
        """Test for base class id"""
        b1 = Base()
        b2 = Base()
        b3 = Base()
        b4 = Base(12)
        b5 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)
        self.assertEqual(b4.id, 12)
        self.assertEqual(b5.id, 4)
        b1 = Base("hello")
        b2 = Base("world")
        b3 = Base(12)
        self.assertEqual(b1.id, "hello")
        self.assertEqual(b2.id, "world")
        self.assertEqual(b3.id, 12)

    def test_to_json_string(self):
        """Test for to_json_string method"""
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")
        self.assertEqual(Base.to_json_string([{"id": 1}]), '[{"id": 1}]')
        self.assertEqual(Base.to_json_string([{"id": 1}, {"id": 2}]),
                         '[{"id": 1}, {"id": 2}]')

    def test_to_json_string_type(self):
        """Test for to_json_string method"""
        self.assertEqual(type(Base.to_json_string(None)), str)
        self.assertEqual(type(Base.to_json_string([])), str)
        self.assertEqual(type(Base.to_json_string([{"id": 1}])), str)
        self.assertEqual(type(Base.to_json_string([{"id": 1}, {"id": 2}])),
                         str)

    def test_to_json_string_empty(self):
        """Test for to_json_string method"""
        self.assertEqual(Base.to_json_string([]), "[]")
        self.assertEqual(Base.to_json_string([{}]), "[{}]")
        self.assertEqual(Base.to_json_string([{}, {}]), "[{}, {}]")
        self.assertEqual(Base.to_json_string([{}, {}, {}]), "[{}, {}, {}]")

    def test_to_json_string_None(self):
        """Test for to_json_string method"""
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_to_json_string_more(self):
        """Test for to_json_string method"""
        self.assertEqual(Base.to_json_string([{"id": 1}, {"id": 2}]),
                         '[{"id": 1}, {"id": 2}]')

    def test_save_to_file(self):
        """Test for save_to_file method"""
        Base.save_to_file(None)
        with open("Base.json", "r") as file:
            self.assertEqual(file.read(), "[]")
        Base.save_to_file([])
        with open("Base.json", "r") as file:
            self.assertEqual(file.read(), "[]")
        Base.save_to_file(None)
        with open("Base.json", "r") as file:
            self.assertEqual(file.read(), "[]")
        rect = Rectangle(10, 7, 2, 8, 5)
        Rectangle.save_to_file([rect])
        with open("Rectangle.json", "r") as file:
            self.assertTrue(len(file.read()) == 53)
        rect1 = Rectangle(10, 7, 2, 8, 5)
        rect2 = Rectangle(2, 4, 1, 2, 3)
        Rectangle.save_to_file([rect1, rect2])
        with open("Rectangle.json", "r") as file:
            self.assertTrue(len(file.read()) == 105)
        square = Square(10, 7, 2, 8)
        Square.save_to_file([square])
        with open("Square.json", "r") as file:
            self.assertTrue(len(file.read()) == 39)
        square1 = Square(10, 7, 2, 8)
        square2 = Square(8, 1, 2, 3)
        Square.save_to_file([square1, square2])
        with open("Square.json", "r") as file:
            self.assertTrue(len(file.read()) == 77)
        square = Square(8, 5, 9, 2)
        Square.save_to_file([square])
        square = Square(10, 7, 2, 8)
        Square.save_to_file([square])
        with open("Square.json", "r") as file:
            self.assertTrue(len(file.read()) == 39)
        Square.save_to_file([])
        with open("Square.json", "r") as file:
            self.assertEqual("[]", file.read())
        with self.assertRaises(TypeError):
            Rectangle.save_to_file()
        with self.assertRaises(TypeError):
            Square.save_to_file([], 1)

    def test_from_json_string(self):
        """Test for from_json_string method"""
        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string("[]"), [])
        self.assertEqual(Base.from_json_string('[{"id": 1}]'), [{"id": 1}])
        self.assertEqual(Base.from_json_string('[{"id": 1}, {"id": 2}]'),
                         [{"id": 1}, {"id": 2}])

    def test_from_json_string_type(self):
        """Test for from_json_string method"""
        self.assertEqual(type(Base.from_json_string(None)), list)
        self.assertEqual(type(Base.from_json_string("[]")), list)
        self.assertEqual(type(Base.from_json_string('[{"id": 1}]')), list)
        self.assertEqual(type(Base.from_json_string('[{"id": 1}, {"id": 2}]')),
                         list)

    def test_from_json_string_empty(self):
        """Test for from_json_string method"""
        self.assertEqual(Base.from_json_string("[]"), [])
        self.assertEqual(Base.from_json_string("[{}]"), [{}])
        self.assertEqual(Base.from_json_string("[{}, {}]"), [{}, {}])

    def test_from_json_string_None(self):
        """Test for from_json_string method"""
        self.assertEqual(Base.from_json_string(None), [])

    def test_from_json_string_more(self):
        """Test for from_json_string method"""
        self.assertEqual(Base.from_json_string('[{"id": 1}, {"id": 2}]'),
                         [{"id": 1}, {"id": 2}])

    def test_create(self):
        """Test for create method"""
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual(str(r1), str(r2))
        self.assertIsNot(r1, r2)
        self.assertNotEqual(r1, r2)
        r1 = Square(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Square.create(**r1_dictionary)
        self.assertEqual(str(r1), str(r2))
        self.assertIsNot(r1, r2)
        self.assertNotEqual(r1, r2)

    def test_load_file(self):
        """Tests for non existant and empty file"""
        if (os.path.exists("Rectangle.json") is True):
            os.remove("Rectangle.json")
        if (os.path.exists("Square.json") is True):
            os.remove("Square.json")
        if (os.path.exists("Base.json") is True):
            os.remove("Base.json")
        lst = Rectangle.load_from_file()
        self.assertEqual(lst, [])
        os.mknod("Rectangle.json")
        lst = Rectangle.load_from_file()
        self.assertEqual(lst, [])
        rect_a = Rectangle(2, 4)
        rect_b = Rectangle(1, 1)
        rect_c = Rectangle(6, 6)
        my_list = [rect_a, rect_b, rect_c]
        Rectangle.save_to_file([rect_a, rect_b, rect_c])
        my_list_loaded = Rectangle.load_from_file()
        self.assertEqual(type(my_list), type(my_list_loaded))
        self.assertEqual(len(my_list), len(my_list_loaded))
        for i in range(len(my_list)):
            self.assertEqual(type(my_list_loaded[i]), type(my_list[i]))
            self.assertEqual(my_list[i].to_dictionary(),
                             my_list_loaded[i].to_dictionary())
        os.remove("Rectangle.json")
        rect_a = Square(2)
        rect_b = Square(1)
        rect_c = Square(6)
        my_list = [rect_a, rect_b, rect_c]
        Square.save_to_file([rect_a, rect_b, rect_c])
        my_list_loaded = Square.load_from_file()
        self.assertEqual(type(my_list), type(my_list_loaded))
        self.assertEqual(len(my_list), len(my_list_loaded))
        for i in range(len(my_list)):
            self.assertEqual(type(my_list_loaded[i]), type(my_list[i]))
            self.assertEqual(my_list[i].to_dictionary(),
                             my_list_loaded[i].to_dictionary())
        os.remove("Square.json")
        with self.assertRaises(TypeError):
            Base.load_from_file("Hello")


if __name__ == "__main__":
    unittest.main()
