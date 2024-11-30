from typing import List


def partition(nums, low: int, high: int):
    i = low
    j = high
    pivot = nums[low]
    while i < j:
        while nums[i] <= pivot and i <= high - 1:
            i += 1
        while nums[j] > pivot and j >= low + 1:
            j -= 1

        if i < j:
            nums[i], nums[j] = nums[j], nums[i]

    nums[low], nums[j] = nums[j], nums[low]
    print(nums)
    return j


def quick_sort(nums: List[int], low: int, high: int):
    if low < high:
        pivotIndex = partition(nums, low, high)

        quick_sort(nums, low, pivotIndex - 1)

        quick_sort(nums, pivotIndex + 1, high)


if __name__ == "__main__":
    nums = [7, 8, 9, 2, 3, 1, 4]
    quick_sort(nums, 0, len(nums) - 1)
    print(nums)
