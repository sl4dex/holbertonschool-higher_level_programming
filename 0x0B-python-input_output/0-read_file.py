#!/usr/bin/python3
""" print file module """


def read_file(filename=""):
    """ prints file on CLI """
    with open(filename, encoding='utf-8') as f:
        print(f.read(), end="")
