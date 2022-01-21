#!/usr/bin/python3
"""Not importing any module"""


class Square:
    """Initiates a Square object"""
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """returns area of the square"""
        return(self.__size ** 2)

    def my_print(self):
        if self.__size == 0:
            print()
            return
        for i in range(self.__size):
            for i in range(self.__size):
                print("#", end="")
            print()

    @property
    def size(self):
        """size getter and setter below"""
        return self.__size

    @size.setter
    def size(self, size):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
