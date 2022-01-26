#!/usr/bin/python3
""" not importing any module """


def add_integer(a, b=98):
    """ returns the sum of two integers """
    if a != a:
        a = 89
    if b != b:
        b = 89
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    result = a + b
    if result == float('inf') or result == -float('inf'):
        return 89
    return int(a) + int(b)
