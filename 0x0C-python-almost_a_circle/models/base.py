#!/usr/bin/python3
""" Base module """
import json
import csv


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
        lst = []
        with open(cls.__name__ + ".json",
                  encoding='utf-8', mode='w') as f:
            if list_objs is None:
                f.write(cls.to_json_string(lst))
            else:
                for obj in list_objs:
                    lst.append(cls.to_dictionary(obj))
                f.write(cls.to_json_string(lst))

    @staticmethod
    def from_json_string(json_string):
        """ returns the list of the JSON string representation json_string """
        if not json_string:
            lst = []
            return lst
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ returns an instance with all attributes already set """
        if cls.__name__ == "Rectangle":
            instance = cls(1, 1)
        elif cls.__name__ == "Square":
            instance = cls(1)
        instance.update(**dictionary)
        return instance

    @classmethod
    def load_from_file(cls):
        """ returns a list of instances """
        lst = []
        try:
            with open(cls.__name__ + ".json", encoding='utf-8') as f:
                json_str = f.read()
        except Exception:
            return lst
        deserialized = cls.from_json_string(json_str)
        for dct in deserialized:
            lst.append(cls.create(**dct))
        return lst

    def save_to_file_csv(cls, list_objs):
        """ writes CVS representation of list_objs to a file """
        with open(cls.__name__ + '.csv', encoding='utf-8', mode='w') as f:
            writer = csv.writer(f)
            for obj in list_objs:
                if cls.__name__ == "Rectangle":
                    writer.writerow([obj.id,
                                    obj.width, obj.height, obj.x, obj.y])
                elif cls.__name__ == "Square":
                    writer.writerow([obj.id, obj.size, obj.x, obj.y])

    def load_from_file_csv(cls):
        """ returns a list of instances """
        with open(cls.__name__ + '.csv', encoding='utf-8') as f:
            reader = csv.reader(f)
            return reader

    def __init__(self, id=None):
        if id is not None and type(id) is not int:
            raise TypeError
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
