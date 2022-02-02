#!/usr/bin/python3
""" student module """


class Student:
    """ student class """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ retrieves a dictionary representation of a Student """
        allstrings = 1
        result = {}
        if type(attrs) is list:
            for i in range(len(attrs)):
                if type(attrs[i]) is not str:
                    allstrings = 0
                else:
                    try:
                        result.update({attrs[i]: getattr(self, attrs[i])})
                    except Exception:
                        pass
        if allstrings == 0 or attrs is None:
            return self.__dict__
        return result

    def reload_from_json(self, json):
        """ replaces all attributes of the Student instance """
        for k, v in json.items():
            setattr(self, k, v)
