from typing import List


def recursive_insertion_sort(nums: List[int], i: int, n: int):
    if i == n:
        return
    j = i
    while j > 0 and nums[j] < nums[j - 1]:
        nums[j], nums[j - 1] = nums[j - 1], nums[j]
        j -= 1

    print(nums)
    recursive_insertion_sort(nums, i + 1, n)


if __name__ == "__main__":
    nums = [64, 34, 25, 12, 22, 11, 90]
    recursive_insertion_sort(nums, 0, len(nums))
