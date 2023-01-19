""" This module contains all the test cases for the rectangle.py module.
it checks tests cases and edge cases for all the methods
written within the Rectangle class"""
import os
from models.rectangle import Rectangle
import unittest


class TestRectangle_instantiation(unittest.TestCase):
    """test different cases for the id"""
    def test_id_instance_no_id(self):
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        self.assertEqual(r1.id, r2.id - 1)

    def test_id_three_instances(self):
        r1 = Rectangle(10, 2)
        r2 = Rectangle(3, 4, 1, 4, 8)
        r3 = Rectangle(2, 10)
        self.assertEqual(r1.id, r3.id - 1)

    def test_id_three_instances_after_normal_inst(self):
        r1 = Rectangle(10, 2)
        r2 = Rectangle(3, 4, 1, 4, 8)
        r3 = Rectangle(2, 10)
        r4 = Rectangle(5, 3, 4, 2)
        self.assertEqual(r1.id, r4.id - 2)

    def test_id_instance_None(self):
        r1 = Rectangle(10, 2, 3, 2, None)
        r2 = Rectangle(2, 10, 4, 2, None)
        self.assertEqual(r1.id, r2.id - 1)

    def test_passed_id(self):
        r2 = Rectangle(3, 4, 1, 4, 8)
        self.assertEqual(r2.id, 8)

    def test_change_id(self):
        r2 = Rectangle(3, 4, 1, 4, 8)
        r2.id = 3
        self.assertEqual(r2.id, 3)

    def test_string_id(self):
        r2 = Rectangle(3, 4, 1, 4, "man")
        self.assertEqual(r2.id, "man")

    def test_nb_instance(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(1, 2, 3, 4).__nb_instances)

    def test_float(self):
        r2 = Rectangle(3, 4, 1, 4, 8.2)
        self.assertEqual(r2.id, 8.2)

    def test_list(self):
        r2 = Rectangle(3, 4, 1, 4, [1, 3, 3])
        self.assertEqual(r2.id, [1, 3, 3])

    def test_tuple(self):
        r2 = Rectangle(3, 4, 1, 4, (1, 3, 3))
        self.assertEqual(r2.id, (1, 3, 3))

    def test_set(self):
        r2 = Rectangle(3, 4, 1, 4, {1, 3, 3})
        self.assertEqual(r2.id, {1, 3, 3})

    def test_dict(self):
        r2 = Rectangle(3, 4, 1, 4, {'name': 1, 'age': 3, 'me': 3})
        self.assertEqual(r2.id, {'name': 1, 'age': 3, 'me': 3})

    def test_negative(self):
        r2 = Rectangle(3, 4, 1, 4, -1)
        self.assertEqual(r2.id, -1)

    def test_bool(self):
        r2 = Rectangle(3, 4, 1, 4, False)
        self.assertEqual(r2.id, False)

    def test_range(self):
        r2 = Rectangle(3, 4, 1, 4, range(3))
        self.assertEqual(r2.id, range(3))

    def test_complex(self):
        r2 = Rectangle(3, 4, 1, 4, complex(4))
        self.assertEqual(r2.id, complex(4))

    def test_more_than_5_args(self):
        with self.assertRaises(TypeError):
            r = Rectangle(1, 2, 3, 4, 5, 6)

    def test_no_args(self):
        with self.assertRaises(TypeError):
            r = Rectangle()


class TestRectangle_width(unittest.TestCase):
    """ Class to check the width method"""
    def test_width_normal(self):
        r = Rectangle(1, 2)
        self.assertEqual(r.width, 1)

    def test_width_type(self):
        r = Rectangle(1, 2)
        self.assertTrue(type(r.width), int)

    def test_width_change(self):
        r = Rectangle(1, 2)
        r.width = 5
        self.assertEqual(r.width, 5)

    def test_width_negative(self):
        with self.assertRaises(ValueError):
            r = Rectangle(-1, 2)

    def test_width_zero(self):
        with self.assertRaises(ValueError):
            r = Rectangle(0, 3)

    def test_width_float(self):
        with self.assertRaises(TypeError):
            r = Rectangle(2.34, 3)

    def test_width_string(self):
        with self.assertRaises(TypeError):
            r = Rectangle("hi", 3)

    def test_width_list(self):
        with self.assertRaises(TypeError):
            r = Rectangle([1], 3)

    def test_width_tuple(self):
        with self.assertRaises(TypeError):
            r = Rectangle((1, ), 3)

    def test_width_dict(self):
        with self.assertRaises(TypeError):
            r = Rectangle({'hi': 1}, 3)

    def test_width_range(self):
        with self.assertRaises(TypeError):
            r = Rectangle(range(3), 3)
