from typing import List


def largest_element(nums: List[int]):
    max = nums[0]
    for i in range(len(nums)):
        if nums[i] > max:
            max = nums[i]

    return max


def largest_element_recur(nums: List[int], i: int, n: int, max: int):
    if i == n:
        return max
    if nums[i] > max:
        max = nums[i]
    return largest_element_recur(nums, i + 1, n, max)


if __name__ == "__main__":
    nums = [10, 5, 8, 2, 15, 7]
    largest = largest_element_recur(nums, 0, len(nums) - 1, nums[0])
    print(f"The largest element in the list is: {largest}")
