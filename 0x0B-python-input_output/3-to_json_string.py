#!/usr/bin/python3
""" serialize JSON module """
import json


def to_json_string(my_obj):
    """ Serialize obj to a JSON formatted str """
    return json.dumps(my_obj)
