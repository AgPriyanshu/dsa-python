# Problem Statement: Given an integer N and an array of size N-1 containing N-1 numbers between 1 to N. Find the number(between 1 to N), that is not present in the given array.
from typing import List


def max_consecutive_ones(nums: List[int]):
    count = 0
    i = 0
    j = 0
    while j < len(nums):
        if nums[j] == 1:
            i += 1
        else:
            i = 0
        count = max(count, i)
        j += 1

    return count


if __name__ == "__main__":
    nums = [
        1,
        0,
        1,
        0,
        0,
        0,
        1,
        1,
        1,
    ]
    print(max_consecutive_ones(nums))
