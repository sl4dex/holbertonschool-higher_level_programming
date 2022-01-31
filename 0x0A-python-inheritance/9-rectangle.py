#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
""" Rectangle Module """


class Rectangle(BaseGeometry):
    """ Rectangle subclass """
    def __init__(self, width, height):
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """ Returns area """
        return self.__width * self.__height

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
