from typing import List


def move_zeros(nums: List[int]):
    i = 0
    j = 1
    while j < len(nums):
        print(f"i:{i}, j:{j}, nums[i]:{nums[i]}, nums[j]:{nums[j]}")
        if nums[j] != 0 and nums[i] == 0:
            nums[i], nums[j] = nums[j], nums[i]
        if nums[i] != 0:
            i += 1
        j += 1


if __name__ == "__main__":
    nums = [1, 2, 0, 1, 0, 4, 0]
    move_zeros(nums)
    print(nums)
