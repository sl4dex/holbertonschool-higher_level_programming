#!/usr/bin/python3
""" list module """


class MyList(list):
    """ prints the list, but sorted (ascending sort) """
    def print_sorted(self):
        print(sorted(self))
