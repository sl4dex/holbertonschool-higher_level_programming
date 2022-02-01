#!/usr/bin/python3
""" JSON deserialize module """
import json


def from_json_string(my_str):
    """ Deserialize string containing JSON doc to a Python object """
    return json.loads(my_str)
