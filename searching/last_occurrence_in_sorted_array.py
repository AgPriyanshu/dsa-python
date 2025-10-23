# Given a sorted array of N integers, write a program to find the index of the last occurrence of the target key. If the target is not found then return -1.
# Note: Consider 0 based indexing
from typing import List


def find_first_occurrence(nums: List[int], target: int):
    result = -1
    lb = 0
    ub = len(nums) - 1
    while lb <= ub:
      mid = (lb + ub) // 2
      if nums[mid] == target:
        result = mid
        ub = mid - 1
      elif nums[mid] > target:
        ub = mid - 1
      else:
        lb = mid + 1


    return result

def find_last_occurrence(nums: List[int], target: int):
    result = -1
    lb = 0
    ub = len(nums) - 1
    while lb <= ub:
      mid = (lb + ub) // 2
      if nums[mid] == target:
        result = mid
        lb = mid + 1
      elif nums[mid] > target:
        ub = mid - 1
      else:
        lb = mid + 1


    return result


if __name__ == "__main__":
    nums = [3,4,13,13,13,20,40]
    target = 13
    print(find_first_occurrence(nums, target))
