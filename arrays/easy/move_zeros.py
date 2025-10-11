# Problem Statement: You are given an array of integers, your task is to move all the zeros in the array to the end of the array and move non-negative integers to the front by maintaining their order.
from typing import List


def move_zeros(nums: List[int]):
    i = 0
    j = 1
    while j < len(nums) and i < len(nums):
        if nums[i] == 0 and nums[j] == 0:
            j+=1
            continue
        elif nums[i] == 0 and nums[j] != 0:
            nums[i],nums[j] = nums[j], nums[i]

        i +=1
        j +=1



if __name__ == "__main__":
    nums = [4,2,4,0,0,3,0,5,1,0]
    move_zeros(nums)
    print(nums)

