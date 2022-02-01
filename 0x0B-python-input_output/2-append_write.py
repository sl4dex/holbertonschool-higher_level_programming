#!/usr/bin/python3
""" count appended module """


def append_write(filename="", text=""):
    """ counts characters appended """
    with open(filename, encoding='utf-8', mode='a') as f:
        f.write(text)
        return len(text)
