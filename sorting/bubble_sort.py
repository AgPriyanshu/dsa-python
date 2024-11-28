from typing import List


def bubble_sort(nums: List[int]):
    n = len(nums)
    for i in range(n):
        for j in range(0, n - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
        print(
            f"After pass {i+1}, the sorted array is: {nums}"
        )  # print sorted array after each


if __name__ == "__main__":
    bubble_sort([2, 3, 4, 5, 61, 7, 8, 4, 5, 6, 7, 98])
