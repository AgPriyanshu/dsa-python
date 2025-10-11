from typing import List


def remove_duplicates(nums: List[int]):
    i = 0
    j = 1
    for j in range(len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]

    return i + 1


if __name__ == "__main__":
    nums = [2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 6]
    dups = remove_duplicates(nums)
    print(dups, nums[0:dups])
