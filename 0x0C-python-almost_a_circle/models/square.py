#!/usr/bin/python3
""" Square module """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ square class """

    @property
    def size(self):
        return super().width

    @size.setter
    def size(self, size):
        """ size encapsulation """
        super(Square, type(self)).width.fset(self, size)
        super(Square, type(self)).height.fset(self, size)

    def update(self, *args, **kwargs):
        lst = ["id", "size", "x", "y"]
        if args:
            for idx in range(len(args)):
                setattr(self, lst[idx], args[idx])
        else:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return f"[Square] ({self.id}) {super().x}/{super().y} - {super().width}"
