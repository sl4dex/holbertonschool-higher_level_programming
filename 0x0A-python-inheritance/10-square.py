#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle
""" Square Module """


class Square(Rectangle):
    """ Square subclass """
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """ Returns area """
        return self.__size ** 2

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__size, self.__size)
