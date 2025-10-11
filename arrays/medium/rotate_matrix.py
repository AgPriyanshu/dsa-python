# Problem Statement: Given a matrix, your task is to rotate the matrix 90 degrees clockwise.


import copy
from typing import List


def rotate_by_90(matrix: List[int]):
    n = len(matrix)
    m = len(matrix[0])
    # Transpose the matrix.
    for i in range(n):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row.
    for i in range(n):
        matrix[i].reverse()


if __name__ == "__main__":

    rotate_by_90([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
