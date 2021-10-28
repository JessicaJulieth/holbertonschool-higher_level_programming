#!/usr/bin/python3
""" Divide a matrix """


def matrix_divided(matrix, div):
    """ function that divides all elements of a matrix """

    if not isinstance(matrix, list) or matrix == []:
        raise TypeError("matrix must be a matrix (list of lists) of \
integers/floats")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    for i in range(len(matrix)):
        if type(matrix[i]) is not list:
            raise TypeError("matrix must be a matrix (list of lists) of \
integers/floats")
        List = []
        NewM = []
        for j in range(len(matrix[i])):
            if type(matrix[i][j]) not in [int, float]:
                raise TypeError("matrix must be a matrix (list of lists) of \
integers/floats")
        if len(matrix[0]) is not len(matrix[i]):
            raise TypeError("Each row of the matrix must have the same size")
        List.append(round(matrix[i][j] / div, 2))
        NewM.append(List)
    return NewM
