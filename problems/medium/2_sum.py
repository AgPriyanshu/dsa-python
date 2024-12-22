from typing import List


def find_2_sum(nums: List[int], target: int):
    complement_set = {}
    for i in range(len(nums)):
        number = nums[i]
        complement = target - number

        if complement in complement_set:
            return (complement, number)
        else:
            complement_set[number] = i

    return False


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6]
    print(find_2_sum(nums, 7))
