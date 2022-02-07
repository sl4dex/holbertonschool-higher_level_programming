#!/usr/bin/python3
""" Base module """
import json


class Base:
    """ Base Class """
    __nb_objects = 0

    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns the JSON string representation of list_dictionaries """
        if not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ writes the JSON string representation of list_objs to a file """
        lst=[]
        if list_objs is None:
            with open(cls.__name__ +".json", encoding='utf-8', mode='w') as f:
                f.write(lst)
        for obj in list_objs:
            lst.append(cls.to_dictionary(obj))
            with open(cls.__name__ +".json", encoding='utf-8', mode='w') as f:
                f.write(Base.to_json_string(lst))

    @staticmethod
    def from_json_string(json_string):
        """ returns the list of the JSON string representation json_string """
        if not json_string:
            lst = []
            return lst
        return json.loads(json_string)

    def __init__(self, id=None):
        if id is not None and type(id) is not int:
            raise TypeError
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
