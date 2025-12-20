# Problem Statement: Given a Matrix, print the given matrix in spiral order.

import math


def spiral_tranverse(nums):
    n = len(nums)
    m = len(nums[0])

    top = 0
    left = 0
    right = m - 1
    bottom = n - 1

    while top <= bottom and left <= right:
        # First Row.
        for j in range(left, right + 1):
            print(nums[top][j])
        top += 1

        # Last Column.
        for i in range(top, bottom + 1):
            print(nums[i][right])
        right -= 1

        # Last Row.
        if top <= bottom:
            for j in range(right, left - 1, -1):
                print(nums[bottom][j])
            bottom -= 1

        # First Column.
        if left <= right:
            for i in range(bottom, top - 1, -1):
                print(nums[i][left])
            left += 1


if __name__ == "__main__":
    # spiral_tranverse([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
    # spiral_tranverse([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    spiral_tranverse([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
    # 1 2 3 4
    # 5 6 7 8
    # 9 10 11 12
