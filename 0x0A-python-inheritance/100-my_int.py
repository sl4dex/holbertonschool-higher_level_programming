#!/usr/bin/python3
""" Rebel Module """


class MyInt(int):
    """ Rebel Class """
    def __eq__(self, other):
        return int.__ne__(self, other)

    def __ne__(self, other):
        return int.__eq__(self, other)
