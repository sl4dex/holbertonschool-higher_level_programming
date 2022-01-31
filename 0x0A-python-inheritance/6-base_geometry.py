#!/usr/bin/python3
""" Excpetion class module """


class BaseGeometry():
    """ Class that raises exception """
    def area(self):
        """ raises excpetion """
        raise Exception("area() is not implemented")
