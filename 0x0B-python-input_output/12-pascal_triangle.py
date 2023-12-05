#!/usr/bin/python3
""" Module pascal triangle """


def pascal_triangle(n):
    '''
    Returns a list of lists of integers representing Pascal's Triangle.

    Args:
        n (int): The number of rows to generate in Pascal's Triangle.

    Returns:
        list: A list of lists where each inner list represents a
        row in Pascal's Triangle.
              The triangle starts from the first row (n=1) up to
              the specified number of rows.
              If n is less than or equal to 0, an empty list is returned.
    '''
    if n <= 0:
        return []
    pascal = []
    for i in range(1, n + 1):
        row = [0 for _ in range(i)]
        for num in range(len(row)):
            if num == 0 or num == len(row) - 1:
                row[num] = 1
            else:
                row[num] += pascal[len(row) - 2][num] + \
                    pascal[len(row) - 2][num - 1]
        pascal.append(row)
    return pascal
