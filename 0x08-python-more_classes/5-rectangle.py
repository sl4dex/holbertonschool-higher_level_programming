#!/usr/bin/python3
""" Module for defining a rectanlgle """


class Rectangle:
    """ Defines a square with width and height """
    def __init__(self, width=0, height=0):
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    def __str__(self):
        rect = ""
        if self.__width == 0 or self.__height == 0:
            return rect
        for row in range(self.__height - 1):
            rect += "#" * self.__width + "\n"
        rect += "#" * self.__width
        return rect

    def __repr__(self):
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        print("Bye rectangle...")

    def area(self):
        """ returns area of rectangle """
        return self.__width * self.__height

    def perimeter(self):
        """ returns perimeter of rectangle """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    @property
    def width(self):
        """ returns width """
        return self.__width

    @width.setter
    def width(self, width):
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    @property
    def height(self):
        """ returns height """
        return self.__height

    @height.setter
    def height(self, height):
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height
