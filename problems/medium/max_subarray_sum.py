# Problem Statement: Given an integer array arr, find the contiguous subarray (containing at least one number) which has the largest sum and returns its sum and prints the subarray.
from math import floor
from typing import List
import sys


def kadane_s_algo(nums: List[int]):
    max_sum = -sys.maxsize - 1
    sum = 0
    imin = 0
    imax = 0
    for i in range(len(nums)):
        if sum + nums[i] < 0:
            sum = 0  # Every time the sum becomes 0, it means a new subarray is getting started
            imin = i + 1
        else:
            sum += nums[i]
        if sum > max_sum:
            max_sum = sum
            imax = i
    print(nums[imin : imax + 1])
    return max_sum


if __name__ == "__main__":
    nums = [-2, -3, 4, -1, -2, 1, 5, -3]
    print(kadane_s_algo(nums))
