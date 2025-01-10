# Problem Statement: Given an array of N integers, write a program to return an element that occurs more than N/2 times in the given array. You may consider that such an element always exists in the array.
from math import floor
from typing import List


def moore_voting_algo(nums: List[int], exists: bool = True):
    count = 0
    element = 0
    for i in range(len(nums)):
        current_element = nums[i]
        if count == 0:
            element = current_element

        if element == current_element:
            count += 1
        else:
            count -= 1

    # If it is not stated that the majority element will definitely exist then confirm by looping and checking for the selected element.
    if not exists:
        for i in range(len(nums)):
            if nums[i] == element:
                count += 1
        if count > floor(len(nums) / 2):
            return element
    return element


def majority_element_more_than_Nby2(nums: List[int]):
    hash_map = dict()
    for i in range(len(nums)):
        if hash_map.get(nums[i]) is None:
            hash_map[nums[i]] = 1
        else:
            hash_map[nums[i]] += 1
    for key in hash_map.keys():
        if hash_map[key] > len(nums) / 2:
            return key


if __name__ == "__main__":
    nums = [4, 4, 2, 4, 3, 4, 4, 3, 2]
    print(moore_voting_algo(nums))
