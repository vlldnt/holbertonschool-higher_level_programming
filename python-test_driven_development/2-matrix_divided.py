#!/usr/bin/python3
'''
Function that divides each number in the matrix
Divided by div
return a new list of divided matrix
'''


def matrix_divided(matrix, div):
    '''Divide each number in the matrix by div'''

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    if not all(isinstance(num, (int, float)) for row in matrix for num in row):
        raise TypeError("matrix must be a matrix"
                        "(list of lists) of integers/floats")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    return [[round(num / div, 2) for num in row] for row in matrix]
