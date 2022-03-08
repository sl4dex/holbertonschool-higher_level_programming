#!/usr/bin/python3
""" Rectangle Module """
from models.base import Base


class Rectangle(Base):
    """ Rectangle Class """
    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @width.setter
    def width(self, width):
        """ sets wifth of rectangle """
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @height.setter
    def height(self, height):
        """ sets height of rectangle """
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @x.setter
    def x(self, x):
        """ sets x of rectangle """
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @y.setter
    def y(self, y):
        """ sets y of rectangle """
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """ returns area of rectangle """
        return self.__width * self.__height

    def display(self):
        """ prints rectangle with #s """
        for y in range(self.__y):
            print()
        for a in range(self.__height):
            for x in range(self.__x):
                print(" ", end="")
            for b in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} " \
               f"- {self.__width}/{self.__height}"

    def update(self, *args, **kwargs):
        """ updates instance attributes listed in args """
        lst = ["id", "width", "height", "x", "y"]
        if args:
            for idx in range(len(args)):
                if idx < 5:
                    setattr(self, lst[idx], args[idx])
        else:
            for k, v in kwargs.items():
                if k in lst:
                    setattr(self, k, v)

    def to_dictionary(self):
        """ returns dictionary representation of Rectangle attributes """
        lst = ["id", "width", "height", "x", "y"]
        dct = {}
        for attr in lst:
            if hasattr(self, attr):
                dct.update({attr: getattr(self, attr)})
        return dct

    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)
