#!/usr/bin/python3
""" inherited class module """


def inherits_from(obj, a_class):
    """ inherited class class """
    if type(obj) == a_class:
        return False
    return issubclass(type(obj), a_class)
