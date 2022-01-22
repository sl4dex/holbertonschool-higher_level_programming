#!/usr/bin/python3
""" Module to say name """


def say_my_name(first_name, last_name=""):
    """ prints the name of the person """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
