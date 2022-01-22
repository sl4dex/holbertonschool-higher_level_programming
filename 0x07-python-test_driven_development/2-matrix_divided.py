#!/usr/bin/python3
""" This module divides a matrix """


def matrix_divided(matrix, div):
    """ returns a new matrix with all elements divided by div """
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    i, j = 0, 0
    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix "
                        "(list of lists) of integers/floats")
    nm = matrix
    for i in range(len(nm)):
        if type(nm[i]) is not list:
            raise TypeError("matrix must be a matrix "
                            "(list of lists) of integers/floats")
        lenM = len(matrix[0])
        if len(nm[i]) is not lenM:
            raise TypeError("Each row of the matrix must have the same size")
        for j in range(len(nm[i])):
            if type(nm[i][j]) is not int and type(nm[i][j]) is not float:
                raise TypeError("matrix must be a matrix "
                                "(list of lists) of integers/floats")
            nm[i][j] = round(nm[i][j] / div, 2)
    return nm
