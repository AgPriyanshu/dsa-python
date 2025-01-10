# Problem Statement: Given an integer N and an array of size N-1 containing N-1 numbers between 1 to N. Find the number(between 1 to N), that is not present in the given array.
from typing import List


def missing_num(N, nums: List[int]):
    n = len(nums)
    low = 0
    high = n - 1
    while low < high:
        mid = (low + high) // 2
        if low + 1 == mid + 1 and high == mid + 1:
            return nums[mid] + 1
        elif nums[mid] == mid + 1:
            low = mid
        elif nums[mid] > mid + 1:
            high = mid

    return mid + 1


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6, 7]
    import random

    # Generate a sequence from 1 to 10,000,000
    sequence = list(range(1, 10000001))

    # Randomly select a number to remove
    missing_number = random.choice(sequence)
    sequence.remove(missing_number)

    print(missing_num(nums))

    # Print the missing number (for verification)
    # print(f"The missing number is(verification): {missing_number}")
