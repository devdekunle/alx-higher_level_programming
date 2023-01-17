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
        b1 = Base()
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 2)
        print(b1.id, b3.id)

    def test_None(self):
        b1 = Base(None)
        b2 = Base(None)
        self.assertEqual(b1.id, b2.id - 1)

    def test_nb_instances_after_passed_id(self):
        b1 = Base()
        b1 = Base(15)
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
    pass

            if __name__ == "__main__":
                unittest.main()
