# Problem Statement: You are given a sorted array containing N integers and a number X, you have to find the occurrences of X in the given array.
from typing import List

def count_occurrences(nums: List[int], target: int):
  lb = 0
  ub = len(nums)
  first_occurrence = -1
  while lb < ub:
    mid = (lb + ub) // 2
    if nums[mid] == target:
      first_occurrence = mid
      ub = mid - 1
    elif nums[mid] > target:
      ub = mid - 1 
    else:
      lb = mid + 1

  if first_occurrence != -1:
    count_index = first_occurrence + 1
    count = 1
    while count_index < len(nums) and nums[count_index] == target:
      count_index +=1
      count += 1
    return count - first_occurrence
  else:
    return first_occurrence

if __name__ == "__main__":
  nums = [1, 2, 2, 2, 2, 2]
  target = 2
  print(count_occurrences(nums,target))
