#!/usr/bin/python3
"""Unittest for base.py"""
import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Unittests for testing the Base class."""

    def setUp(self):
        """Set up test methods"""
        Base._Base__nb_objects = 0

    def test_id(self):
        """ test id """
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)

    def test_None_id(self):
        """ test id None """
        b1 = Base(None)
        b2 = Base(None)
        self.assertEqual(b1.id, b2.id - 1)

    def test_unique_id(self):
        """ test unique id """
        self.assertEqual(12, Base(12).id)

    def test_after_unique_id(self):
        """ test after the unique id """
        b1 = Base()
        b2 = Base(12)
        b3 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 12)
        self.assertEqual(b3.id, 2)

    def test_id_public(self):
        """ test public id """
        b = Base(12)
        b.id = 15
        self.assertEqual(b.id, 15)

    def test_private(self):
        """ test private """
        with self.assertRaises(AttributeError):
            print(Base(12).__nb_instances)

    def test_str_id(self):
        """ test str id """
        b1 = Base("hello")
        self.assertEqual(b1.id, "hello")

    def test_float_id(self):
        """ test float id """
        b1 = Base(1.5)
        self.assertEqual(b1.id, 1.5)

    def test_dict_id(self):
        """ test dict id """
        self.assertEqual(Base({"a": 1, "b": 2}).id, {"a": 1, "b": 2})

    def test_bool_id(self):
        """ test bool id """
        self.assertEqual(Base(True).id, True)

    def test_list_id(self):
        """ test list id """
        self.assertEqual(Base([1, 2, 3]).id, [1, 2, 3])

    def test_tuple_id(self):
        """ test tuple id """
        self.assertEqual(Base((1, 2)).id, (1, 2))

    def test_set_id(self):
        """ test set id """
        self.assertEqual(Base({1, 2, 3}).id, {1, 2, 3})

    def test_range_id(self):
        """ test range id """
        self.assertEqual(Base(range(2)).id, range(2))

    def test_two_args(self):
        """ test with two args """
        with self.assertRaises(TypeError):
            Base(1, 2)

    def test_to_json_string_type(self):
        """ test to_json_string method """
        r = Rectangle(10, 7, 2, 8, 6)
        self.assertEqual(type(Base.to_json_string([r.to_dictionary()])), str)

    def test_to_json_string_one_dict(self):
        """ test to_json_string method """
        r = Rectangle(10, 7, 2, 8, 6)
        self.assertTrue(len(Base.to_json_string([r.to_dictionary()])) == 53)

    def test_to_json_string_type(self):
        """ test to_json_string method """
        s = Square(10, 2, 3, 4)
        self.assertEqual(type(Base.to_json_string([s.to_dictionary()])), str)

    def test_to_json_string_one_dict(self):
        """ test to_json_string method """
        s = Square(10, 2, 3, 4)
        self.assertTrue(len(Base.to_json_string([s.to_dictionary()])) == 39)

    def test_to_json_string_empty_list(self):
        """ test to_json_string method """
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json_string_none(self):
        """ test to_json_string method """
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_to_json_string_no_args(self):
        """ test to_json_string method """
        with self.assertRaises(TypeError):
            Base.to_json_string()

    def test_to_json_string_more_than_one_arg(self):
        """ test to_json_string method """
        with self.assertRaises(TypeError):
            Base.to_json_string([], 1)

    def test_save_to_file_rectangle(self):
        """ test save_to_file method """
        r = Rectangle(10, 7, 2, 8, 5)
        Rectangle.save_to_file([r])
        with open("Rectangle.json", "r") as f:
            self.assertTrue(len(f.read()) == 53)

    def test_save_to_file_square(self):
        """ test save_to_file method """
        s = Square(10, 7, 2, 8)
        Square.save_to_file([s])
        with open("Square.json", "r") as f:
            self.assertTrue(len(f.read()) == 39)

    def test_save_to_file_cls_name(self):
        """ test save_to_file method """
        s = Square(10, 7, 2, 8)
        Base.save_to_file([s])
        with open("Base.json", "r") as f:
            self.assertTrue(len(f.read()) == 39)

    def test_save_to_file_overwrite(self):
        """ test save_to_file method """
        s = Square(9, 2, 39, 2)
        Square.save_to_file([s])
        s = Square(10, 7, 2, 8)
        Square.save_to_file([s])
        with open("Square.json", "r") as f:
            self.assertTrue(len(f.read()) == 39)

    def test_save_to_file_None(self):
        """ test save_to_file method """
        Square.save_to_file(None)
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file_empty_list(self):
        """ test save_to_file method """
        Square.save_to_file([])
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file_no_args(self):
        """ test save_to_file method """
        with self.assertRaises(TypeError):
            Rectangle.save_to_file()

    def test_save_to_file_more_than_one_arg(self):
        """ test save_to_file method """
        with self.assertRaises(TypeError):
            Square.save_to_file([], 1)

    def test_from_json_string_type(self):
        """ test from_json_string method """
        list_input = [{"id": 89, "width": 10, "height": 4}]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(type(list_output), list)

    def test_from_json_string_rectangle(self):
        """ test from_json_string method """
        list_input = [{"id": 89, "width": 10, "height": 4, "x": 7}]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_from_json_string_square(self):
        """ test from_json_string method """
        list_input = [{"id": 89, "size": 10, "height": 4}]
        json_list_input = Square.to_json_string(list_input)
        list_output = Square.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_from_json_string_None(self):
        """ test from_json_string method """
        self.assertEqual(Base.from_json_string(None), [])

    def test_from_json_string_empty_list(self):
        """ test from_json_string method """
        self.assertEqual(Base.from_json_string("[]"), [])

    def test_from_json_string_no_args(self):
        """ test from_json_string method """
        with self.assertRaises(TypeError):
            Base.from_json_string()

    def test_from_json_string_more_than_one_arg(self):
        """ test from_json_string method """
        with self.assertRaises(TypeError):
            Base.from_json_string([], 1)

    def test_create_rectangle(self):
        """ test create method """
        r1 = Rectangle(6, 4, 5, 1, 10)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual(str(r1), "[Rectangle] (10) 5/1 - 6/4")

    def test_create_rectangle_new(self):
        """ test create method """
        r1 = Rectangle(11, 9, 2, 4, 15)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual(str(r2), "[Rectangle] (15) 2/4 - 11/9")

    def test_create_rectangle_is(self):
        """ test create method """
        r1 = Rectangle(1, 3, 8, 7, 4)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertIsNot(r1, r2)

    def test_create_rectangle_equals(self):
        """ test create method """
        r1 = Rectangle(1, 3, 8, 7, 4)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertNotEqual(r1, r2)

    def test_create_square(self):
        """ test create method """
        s1 = Square(4, 3, 1, 10)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertEqual(str(s1), "[Square] (10) 3/1 - 4")

    def test_create_square_new(self):
        """ test create method """
        s1 = Square(4, 3, 1, 10)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertEqual(str(s2), "[Square] (10) 3/1 - 4")

    def test_create_square_is(self):
        """ test create method """
        s1 = Square(4, 3, 1, 10)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertIsNot(s1, s2)

    def test_create_square_equals(self):
        """ test create method """
        s1 = Square(4, 3, 1, 10)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertNotEqual(s1, s2)

    @classmethod
    def tearDown(self):
        """Delete any created files."""
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass
        try:
            os.remove("Square.json")
        except IOError:
            pass

    def test_load_from_file_rectangle(self):
        """ test load_from_file method """
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file([r1, r2])
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(str(r1), str(list_rectangles_output[0]))

    def test_load_from_file_rectangle_types(self):
        """ test load_from_file method """
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file([r1, r2])
        output = Rectangle.load_from_file()
        self.assertTrue(all(type(obj) == Rectangle for obj in output))

    def test_load_from_file_first_square(self):
        """ test load_from_file method """
        s1 = Square(5, 1, 3, 3)
        s2 = Square(9, 5, 2, 3)
        Square.save_to_file([s1, s2])
        list_squares_output = Square.load_from_file()
        self.assertEqual(str(s1), str(list_squares_output[0]))

    def test_load_from_file_square_types(self):
        """ test load_from_file method """
        s1 = Square(5, 1, 3, 3)
        s2 = Square(9, 5, 2, 3)
        Square.save_to_file([s1, s2])
        output = Square.load_from_file()
        self.assertTrue(all(type(obj) == Square for obj in output))

    def test_load_from_file_no_file(self):
        """ test load_from_file method """
        output = Square.load_from_file()
        self.assertEqual([], output)

    def test_load_from_file_more_than_one_arg(self):
        """ test load_from_file method """
        with self.assertRaises(TypeError):
            Base.load_from_file([], 1)


if __name__ == "__main__":
    unittest.main()
