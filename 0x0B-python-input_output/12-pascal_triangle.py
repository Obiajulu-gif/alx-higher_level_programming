#!/usr/bin/python3
"""module for pascal triangle"""


def pascal_triangle(n):
    """
    generate paschal triangle

    Args:
    n: the number of step to be meet

    Return:
    return a list of the paschal triangle
    """
    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        row = [1] * (i + 1)
        if i >= 2:
            for j in range(1, i):
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)

    return triangle
