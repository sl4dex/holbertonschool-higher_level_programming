#!/usr/bin/python3
""" count written module """


def write_file(filename="", text=""):
    """ counts characters written """
    with open(filename, encoding='utf-8', mode='w') as f:
        f.write(text)
        return f.tell()
