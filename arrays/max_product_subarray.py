# Problem Statement:Problem Statement: Given an array that contains both negative and positive integers, find the maximum product subarray.
from math import floor
from typing import List
import sys


def max_product_subarray(nums: List[int]):
    prefix = 1
    suffix = 1
    result = float("-inf")
    for i in range(len(nums)):
        if prefix == 0:
            prefix = 1
        elif suffix == 0:
            suffix = 1
        prefix *= nums[i]
        suffix *= nums[len(nums) - i - 1]
        result = max(result, max(prefix, suffix))

    return result


if __name__ == "__main__":
    nums = [-2, -3, 4, -1, -2, 1, 5, -3]
    print(max_product_subarray(nums))
