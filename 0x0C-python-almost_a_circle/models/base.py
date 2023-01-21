#!/usr/bin/python3
""" A module to create a class Base"""

import json
import os
import csv


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
        if list_dictionaries is None:
            return "[]"
        if len(list_dictionaries) == 0:
            return "[]"
        if type(list_dictionaries) is not list:
            raise TypeError("list_dictionaries must be a list of dictionaries")
        for i in list_dictionaries:
            if type(i) is not dict:
                raise TypeError("list must be a list of dictionaries")
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """write the json string representation of an object to a file"""
        if list_objs is None or len(list_objs) == 0:
            with open(f"{cls.__name__}.json", "w") as my_file:
                my_file.write("[]")
        elif type(list_objs) is not list:
            raise TypeError("list_objs must be a list of objects")
        else:
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
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                dummy_inst = cls(1, 1)
            else:
                dummy_inst = cls(1)
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
            return []
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

    @classmethod
    def load_from_file(cls):
        """Return a list of classes instantiated from a file of JSON strings.
        Reads from `<cls.__name__>.json`.
        Returns:
            If the file does not exist - an empty list.
            Otherwise - a list of instantiated classes.
        """
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Write the CSV serialization of a list of objects to a file.
        Args:
            list_objs (list): A list of inherited Base instances.
        """
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Return a list of classes instantiated from a CSV file.
        Reads from `<cls.__name__>.csv`.
        Returns:
            If the file does not exist - an empty list.
            Otherwise - a list of instantiated classes.
        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []
