#!/usr/bin/python3
""""Module contains rotate_2d_matrix"""


def rotate_2d_matrix(matrix):
    """Given an n x n 2D matrix, rotate it 90 degrees clockwise
    Do not return anything. The matrix must be edited in-place.
    """
    length = len(matrix)
    for i in range(length // 2):
        for j in range(i, length - i - 1):
            temp = matrix[i][j]
            matrix[i][j] = matrix[length - 1 - j][i]
            matrix[length - 1 - j][i] = matrix[length - 1 - i][length - 1 - j]
            matrix[length - 1 - i][length - 1 - j] = matrix[j][length - 1 - i]
            matrix[j][length - 1 - i] = temp
