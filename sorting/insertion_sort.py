from typing import List


def insertion_sort(nums: List[int]):
    n = len(nums)
    for i in range(n):
        key = nums[i]
        j = i - 1
        while j >= 0 and key < nums[j]:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = key

        print(
            f"After pass {i+1}, the sorted array is: {nums}"
        )  # print sorted array after each


if __name__ == "__main__":
    insertion_sort([64, 34, 25, 12, 22, 11, 90])
