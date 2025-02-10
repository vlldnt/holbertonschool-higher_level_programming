#!/usr/bin/python3
'''Returns a list of integers representing the pascal's triangle'''


def pascal_triangle(n):
    '''Returns a Pascal's triangle'''
    if n <= 0:
        return []

    triangle = [[1]]
    for i in range(1, n):
        line = [1]
        for j in range(1, i):
            line.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        line.append(1)
        triangle.append(line)
    return triangle
