#!/usr/bin/python3
""" class to JSON module """


def class_to_json(obj):
    """ returns JSON serialization of an object """
    return obj.__dict__
