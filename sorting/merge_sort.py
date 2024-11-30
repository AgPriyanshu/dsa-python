from typing import List


def merge(nums, low: int, mid: int, high: int):
    temp = []
    left = low
    right = mid + 1

    while left <= mid and right <= high:
        if nums[left] <= nums[right]:
            temp.append(nums[left])
            left = left + 1
        elif nums[right] < nums[left]:
            temp.append(nums[right])
            right = right + 1

    while left <= mid:
        temp.append(nums[left])
        left = left + 1

    while right <= high:
        temp.append(nums[right])
        right = right + 1

    for i in range(len(temp)):
        nums[low + i] = temp[i]


def merge_sort(nums: List[int], low: int, high: int):
    mid = (low + high) // 2
    if low < high:
        merge_sort(nums, low, mid)
        merge_sort(nums, mid + 1, high)
        merge(nums, low, mid, high)


if __name__ == "__main__":
    nums = [7, 8, 9, 2, 3, 1, 4]
    merge_sort(nums, 0, len(nums) - 1)
    print(nums)
