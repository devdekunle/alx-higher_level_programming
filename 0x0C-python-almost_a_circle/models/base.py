#!/usr/bin/python3
""" A module to create a class Base"""

import json
import os


class Base:
    """class base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """object instantiation"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the json string of list dictionaries"""
        if type(list_dictionaries) is not list:
            raise TypeError("list_dictionaries must be a list of dictionaries")
        if len(list_dictionaries) == 0 or list_dictionaries is None:
            return "[]"
        for i in list_dictionaries:
            if type(i) is not dict:
                raise TypeError("list_dictionaries must be a\
                                list of dictionaries")
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """write the json string representation of an object to a file"""
        if list_objs is None:
            with open(f"{cls.__name__}.json", "w") as my_file:
                my_file.write([])
        if type(list_objs) is not list:
            raise TypeError("list_objs must be a list of objects")
        dict_list = []
        for obj in list_objs:
            if not issubclass(cls, Base):
                raise NameError(f"name '{cls__name__}' is not defined")
            elif not isinstance(obj, cls):
                raise NameError(f"name '{obj.__name__}' is not defined")

            else:
                """ convert object to dictionary"""
                obj_dict = obj.to_dictionary()
                dict_list.append(obj_dict)
        """save list to json file after appending all object
        dictionaries to list"""
        json_str = cls.to_json_string(dict_list)
        with open(f"{cls.__name__}.json", "w") as my_file:
            my_file.write(json_str)

    @staticmethod
    def from_json_string(json_string):
        """Returns the list representation of s json string"""
        if json_string is None or len(json_string) == 0:
            json_string = "[]"
        return (json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with the attributes already set"""
        if type(dictionary) is not dict:
            raise TypeError("dictionary must be of type dict")
        dummy_inst = cls(3, 4, 1, 2)
        dummy_inst.update(**dictionary)
        return dummy_inst

    @classmethod
    def load_from_file(cls):
        """class method to return a list of instances"""
        if os.path.exists(f"{cls.__name__}.json"):
            with open(f"{cls.__name__}.json", "r") as my_file:
                """store string read from file"""
                string_inst_dict = my_file.read()
        else:
            return ""
        """ call from_json_string and convert string read from file
            to list and assign return list of dictionaries
            to list_inst_dict"""
        list_inst_dict = cls.from_json_string(string_inst_dict)
        inst_list = []
        """loop throught each dictionary in the list and creat an instance"""
        for ins_dict in list_inst_dict:
            """append each created instance to inst_list"""
            inst_list.append(cls.create(**ins_dict))
        return inst_list
