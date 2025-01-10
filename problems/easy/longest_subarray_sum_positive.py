# Problem Statement: Given an integer N and an array of size N-1 containing N-1 numbers between 1 to N. Find the number(between 1 to N), that is not present in the given array.
from typing import List


def longest_subarray_sum(nums: List[int], k: int):
    sum = 0
    count = 0
    j = 0
    while j < len(nums):
        sum = 0
        p = j
        while sum != k and p < len(nums):
            sum += nums[p]
            p += 1
        if sum == k:
            print(f"p: {p}, j:{j}")
            count = max(count, p - j)
        j += 1

    return count


if __name__ == "__main__":
    nums = [-1, 1, 1]
    print(longest_subarray_sum(nums, 1))
