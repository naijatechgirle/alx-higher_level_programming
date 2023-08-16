#!/usr/bin/python3
'''
Returns a list of intergers representing pascal_triangle.
'''


def pascal_triangle(n):
    """ The Pascal Triangle """

    triangle = []
    if n <= 0:
        return triangle

    triangle = [[1]]
    for b in range(n - 1):
        line = triangle[-1]
        ben = [1]
        for b in range(len(line) - 1):
            ben.append(line[b] + line[b + 1])
        ben.append(1)
        triangle.append(ben)
    return triangle
