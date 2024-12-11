from typing import List


def is_sorted(nums: List[int]):
    for i in range(len(nums) - 1):
        if nums[i] > nums[i + 1]:
            return False
    return True


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6]
    print(f"Original array: {nums}")
    print(f"Is the array sorted? {is_sorted(nums)}")
