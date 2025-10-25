# Problem Statement:
# Given an integer array arr of size N, sorted in ascending order (with distinct values), the array 
# is rotated at any index which is unknown. Find the minimum element in the array. 

from typing import List

def min_in_sorted_array(nums: List[int]):
  lb = 0
  ub = len(nums) - 1

  while lb < ub:
    mid = (lb + ub) // 2
    if nums[mid] > nums[ub]:
      lb = mid + 1
    else:
      ub = mid - 1

  return nums[lb]
 

if __name__ == "__main__":
  nums = [4,5,6,7,0,1,2,3]
  print(min_in_sorted_array(nums))