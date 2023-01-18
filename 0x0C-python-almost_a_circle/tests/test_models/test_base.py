"""This unittest module contains all the test cases for all the possible
input cases for all the methods contained in the Base.py module"""

import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase_instantaition(unittest.TestCase):
    """tests for instantiation of Base Class"""

    def test_zero_arg(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    def test_three_instances(self):
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 2)

    def test_None(self):
        b1 = Base(None)
        b2 = Base(None)
        self.assertEqual(b1.id, b2.id - 1)

    def test_nb_instances_after_passed_id(self):
        b1 = Base()
        b2 = Base(15)
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 1)

    def test_passed_id(self):
        self.assertEqual(Base(23).id, 23)

    def test_id_change(self):
        b1 = Base(23)
        b1.id = 34
        self.assertEqual(b1.id, 34)

    def test_nb_private_instance(self):
        with self.assertRaises(AttributeError):
            print(Base(21).__nb_instances)

    def test_id_str(self):
        self.assertEqual("boy", Base("boy").id)

    def test_float_id(self):
        self.assertEqual(3.2, Base(3.2).id)

    def test_negative_id(self):
        self.assertEqual(-3, Base(-3).id)

    def test_dict_id(self):
        self.assertEqual({"h": 1, "a": 2}, Base({"h": 1, "a": 2}).id)

    def test_bool_id(self):
        self.assertEqual(True, Base(True).id)

    def test_list_id(self):
        self.assertEqual([4, 5, 2], Base([4, 5, 2]).id)

    def test_list_tuple(self):
        self.assertEqual((1, 2), Base((1, 2)).id)

    def test_set_id(self):
        self.assertEqual({1, 2, 4}, Base({1, 2, 4}).id)

    def test_range_id(self):
        self.assertEqual(range(4), Base(range(4)).id)

    def test_complex_id(self):
        self.assertEqual(complex(3), Base(complex(3)).id)

    def test_two_args(self):
        with self.assertRaises(TypeError):
            Base(3, 4)


class Test_to_json_string(unittest.TestCase):
    """Unittest to test conversion to json string"""

    def test_to_json_sring_rectangle_subclass(self):
        r = Rectangle(10, 2, 4, 2, 8)
        self.assertEqual(str, type(Base.to_json_string([r.to_dictionary()])))

    def test_to_json_string_one_dictionary(self):
        r = Rectangle(20, 1, 3, 2, 5)
        self.assertTrue(len(Base.to_json_string([r.to_dictionary()])))

    def test_to_json_string_two_dicts(self):
        r1 = Rectangle(1, 2, 3, 4, 5)
        r2 = Rectangle(6, 7, 8, 9, 10)
        dict_list = [r1.to_dictionary(), r2.to_dictionary()]
        self.assertEqual(len(Base.to_json_string(dict_list)), 105)

    def test_to_json_string_square_type(self):
        s = Square(1, 2, 4, 5)
        self.assertEqual(str, type(Base.to_json_string([s.to_dictionary()])))

    def test_to_json_string_square_two_dictionaries(self):
        s1 = Square(1, 2, 3, 5)
        s2 = Square(3, 2, 4, 1)
        dict_list = [s1.to_dictionary(), s2.to_dictionary()]
        self.assertEqual(len(Base.to_json_string(dict_list)), 76)

    def test_to_json_string_square_one_dictionary(self):
        s = Square(1, 2, 4, 1)
        self.assertEqual(len(Base.to_json_string([s.to_dictionary()])), 38)

    def test_to_json_string_empty_list(self):
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json_string_none(self):
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_to_json_string_without_arg(self):
        with self.assertRaises(TypeError):
            Base.to_json_string()

    def test_to_json_string_two_args(self):
        with self.assertRaises(TypeError):
            Base.to_json_string([], "name")


class TestBase_save_to_file(unittest.TestCase):
    """test conditions for save to file"""
    @classmethod
    def tearDown(self):
        """Delete any created files"""
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass
        try:
            os.remove("Square.json")
        except IOError:
            pass
        try:
            os.remove("Base.json")
        except IOError:
            pass

    def test_save_to_file_for_rectangle(self):
        r = Rectangle(1, 2, 4, 2, 4)
        Rectangle.save_to_file([r])
        with open("Rectangle.json", "r") as my_file:
            self.assertEqual(len(my_file.read()), 52)

    def test_save_to_file_two_rect(self):
        r1 = Rectangle(3, 4, 3, 2, 5)
        r2 = Rectangle(4, 1, 10, 3, 4)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as my_file:
            self.assertEqual(len(my_file.read()), 105)

    def test_save_to_file_square(self):
        s = Square(1, 3, 5, 3)
        Square.save_to_file([s])
        with open("Square.json", "r") as my_file:
            self.assertEqual(len(my_file.read()), 38)

    def test_save_to_file_two_square(self):
        s1 = Square(3, 5, 3, 6)
        s2 = Square(5, 12, 5, 3)
        Square.save_to_file([s1, s2])
        with open("Square.json", "r") as my_file:
            self.assertEqual(len(my_file.read()), 77)

    def test_save_to_file_with_cls_name(self):
        r = Rectangle(2, 6, 9, 2, 3)
        Base.save_to_file([r])
        with open("Base.json", "r") as my_file:
            self.assertEqual(len(my_file.read()), 52)

    def test_save_to_file_overwrite(self):
        r = Rectangle(4, 5, 2, 5, 2)
        Rectangle.save_to_file([r])
        r = Rectangle(3, 2, 5, 2)
        Rectangle.save_to_file([r])
        with open("Rectangle.json", "r") as my_file:
            self.assertEqual(len(my_file.read()), 53)

    def test_save_file_none(self):
        Square.save_to_file(None)
        with open("Square.json", "r") as my_file:
            self.assertEqual("[]", my_file.read())

    def test_save_to_file_empty(self):
        with self.assertRaises(TypeError):
            Square.save_to_file()

    def test_save_to_file_empty_list(self):
        Square.save_to_file([])
        with open("Square.json", "r") as my_file:
            self.assertEqual("[]", my_file.read())

    def test_save_to_file_no_argument(self):
        with self.assertRaises(TypeError):
            Square.save_to_file()

    def test_save_to_file_more_args(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file([], 3)


class TestBase_from_json_string(unittest.TestCase):
    """Test cases for from json_string"""
    def test_from_json_string_rectangle(self):
        list_input = [{'id': 89, 'width': 10, 'height': 4}]
        json_list_output = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_output)
        self.assertEqual(list_input, list_output)

    def test_from_json_string_square(self):
        list_input = [{'id': 89, 'width': 10, 'height': 4}]
        json_list_output = Square.to_json_string(list_input)
        list_output = Square.from_json_string(json_list_output)
        self.assertEqual(list_input, list_output)

    def test_from_json_string_two_square(self):
        list_input = [
            {'id': 89, 'width': 10, 'height': 4},
            {'id': 7, 'width': 1, 'height': 7}
        ]
        json_list_output = Square.to_json_string(list_input)
        list_output = Square.from_json_string(json_list_output)
        self.assertEqual(list_input, list_output)

    def test_from_json_string_type_(self):
        list_input = [{'id': 89, 'width': 10, 'height': 4}]
        json_list_output = Square.to_json_string(list_input)
        list_output = Square.from_json_string(json_list_output)
        self.assertEqual(list, type(list_output))

    def test_from_json_string_two_Rectangles(self):
        list_input = [
            {'id': 89, 'width': 10, 'height': 4, "x": 7, "y": 2},
            {'id': 7, 'width': 1, 'height': 7, "x": 4, "y": 2}
        ]
        json_list_output = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_output)
        self.assertEqual(list_input, list_output)

    def test_from_json_string_None(self):
        list_out = Square.from_json_string(None)
        self.assertEqual([], list_out)

    def test_from_json_string_empty(self):
        list_out = Rectangle.from_json_string("[]")
        self.assertEqual([], list_out)

    def test_from_json_string_no_args(self):
        with self.assertRaises(TypeError):
            Base.from_json_string()

    def test_from_json_string_more_args(self):
        with self.assertRaises(TypeError):
            Base.from_json_string([], [])


class TestBase_create_instance(unittest.TestCase):
    """ test class method to create a list of inatances"""
    def test_create_rectangle(self):
        r1 = Rectangle(2, 4, 2, 5, 8)
        r1_dict = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dict)
        self.assertEqual("[Rectangle] (8) 2/5 - 2/4", str(r1))

    def test_create_rectangle_new(self):
        r1 = Rectangle(2, 4, 2, 5, 8)
        r1_dict = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dict)
        self.assertEqual("[Rectangle] (8) 2/5 - 2/4", str(r2))

    def test_create_rectangle_not_equal(self):
        r1 = Rectangle(2, 4, 2, 5, 8)
        r1_dict = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dict)
        self.assertNotEqual(r1, r2)

    def test_create_rectangle_is_not(self):
        r1 = Rectangle(2, 4, 2, 5, 8)
        r1_dict = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dict)
        self.assertIsNot(r1, r2)

    def test_create_square(self):
        s1 = Square(5, 7, 9, 3)
        s1_dict = s1.to_dictionary()
        s2 = Square.create(**s1_dict)
        self.assertEqual("[Square] (3) 7/9 - 5", str(s1))

    def test_create_square_new(self):
        s1 = Square(5, 7, 9, 3)
        s1_dict = s1.to_dictionary()
        s2 = Square.create(**s1_dict)
        self.assertEqual("[Square] (3) 7/9 - 5", str(s2))

    def test_create_square_not_equal(self):
        s1 = Square(5, 7, 9, 3)
        s1_dict = s1.to_dictionary()
        s2 = Square.create(**s1_dict)
        self.assertNotEqual(s1, s2)

    def test_create_square_is_not(self):
        s1 = Square(5, 7, 9, 3)
        s1_dict = s1.to_dictionary()
        s2 = Square.create(**s1_dict)
        self.assertIsNot(s1, s2)

    def test_create_base_None(self):
        with self.assertRaises(TypeError):
            s = Square.create(None)

    def test_create_base_list(self):
        with self.assertRaises(TypeError):
            r = Rectangle.create([1, 3, 4, 7])

    def test_create_base_tuple(self):
        with self.assertRaises(TypeError):
            r = Rectangle.create((1, 3))


class TestBase_load_from_file(unittest.TestCase):
    """test cases for load from file"""
    @classmethod
    def tearDown(self):
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass
        try:
            os.remove("Square.json")
        except IOError:
            pass

    def test_load_from_file_rectangle(self):
        r1 = Rectangle(1, 2, 3, 4, 5)
        r2 = Rectangle(4, 5, 2, 6, 3)
        Rectangle.save_to_file([r1, r2])
        list_rect_output = Rectangle.load_from_file()
        self.assertEqual(str(r1), str(list_rect_output[0]))

    def test_load_from_file_rectangle_second_instance(self):
        r1 = Rectangle(1, 2, 3, 4, 5)
        r2 = Rectangle(4, 5, 2, 6, 3)
        Rectangle.save_to_file([r1, r2])
        list_rect_output = Rectangle.load_from_file()
        self.assertEqual(str(r2), str(list_rect_output[1]))

    def test_load_from_file_check_all_instances(self):
        r1 = Rectangle(1, 2, 3, 4, 5)
        r2 = Rectangle(4, 5, 2, 6, 3)
        Rectangle.save_to_file([r1, r2])
        list_output = Rectangle.load_from_file()
        self.assertTrue(all(type(ins) == Rectangle for ins in list_output))

    def test_load_from_file_square(self):
        s1 = Square(1, 2, 3, 4)
        s2 = Square(4, 5, 2, 6)
        Square.save_to_file([s1, s2])
        list_square_output = Square.load_from_file()
        self.assertEqual(str(s1), str(list_square_output[0]))

    def test_load_from_file_square_second_instance(self):
        s1 = Square(2, 3, 4, 5)
        s2 = Square(5, 2, 6, 3)
        Square.save_to_file([s1, s2])
        list_square_output = Square.load_from_file()
        self.assertEqual(str(s2), str(list_square_output[1]))

    def test_load_from_file_square_all_instances(self):
        s1 = Square(2, 3, 4, 5)
        s2 = Square(5, 2, 6, 3)
        Square.save_to_file([s1, s2])
        list_square_output = Square.load_from_file()
        self.assertTrue(all(type(obj) == Square for obj in list_square_output))

    def test_load_from_file_no_file(self):
        s = Square.load_from_file()
        self.assertEqual([], s)

    def test_load_from_file_more_args(self):
        with self.assertRaises(TypeError):
            Base.load_from_file([], 1)

        if __name__ == "__main__":
            unittest.main()
