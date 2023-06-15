#!/usr/bin/python3
"""Base Module"""
import json


class Base:
    """Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """class constructor"""
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns JSON string representation of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes JSON string representation of list_objs to a file"""
        filename = f"{cls.__name__}.json"
        if list_objs is None:
            list_objs = []
        dict_list = []
        for obj in list_objs:
            if isinstance(obj, Base):
                dict_list.append(obj.to_dictionary())
            else:
                pass
        json_str = cls.to_json_string(dict_list)
        with open(filename, "w") as file:
            file.write(json_str)

    @staticmethod
    def from_json_string(json_string):
        """returns list of JSON string representation json_string"""
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            dummy_instance = cls(1, 1)
        if cls.__name__ == "Square":
            dummy_instance = cls(1)
        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        filename = f"{cls.__name__}.json"
        try:
            with open(filename, "r") as file:
                json_str = file.read()
                dict_list = cls.from_json_string(json_str)
                instances = []
                for data in dict_list:
                    instances.append(cls.create(**data))
                return instances
        except FileNotFoundError:
            return []
