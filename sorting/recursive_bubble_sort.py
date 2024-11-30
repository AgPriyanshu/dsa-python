from typing import List


def recursive_bubble_sort(nums: List[int], n: int):
    if n == 1:
        return

    for i in range(n - 1):
        if nums[i] > nums[i + 1]:
            nums[i], nums[i + 1] = nums[i + 1], nums[i]
    recursive_bubble_sort(nums, n - 1)


if __name__ == "__main__":
    nums = [2, 3, 4, 5, 61, 7, 8, 4, 5, 6, 7, 98]
    recursive_bubble_sort(nums, len(nums))
    print(nums)
