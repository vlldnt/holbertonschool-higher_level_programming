#!/usr/bin/python3
'''Returns a list of integers representing the pascal's triangle'''


def pascal_triangle(n):
    if n <= 0:
        return []

    triangle = [[1]]
    for i in range(1, n):
        line = [1]
        for li in range(1, i):
            line.append(triangle[i - 1][li - 1] + triangle[i - 1][li])
        line.append(1)
        triangle.append(line)
    return triangle
