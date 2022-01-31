#!/usr/bin/python3
""" Square Module """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Square subclass """
    def __init__(self, size):
        super().integer_validator("size", size)
        self.__size = size

    def area(self):
        """ Returns area """
        return self.__size ** 2

    def __str__(self):
        return "[Square] {}/{}".format(self.__size, self.__size)
