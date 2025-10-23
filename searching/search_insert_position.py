# Problem Statement: You are given a sorted array arr of distinct values and a target value x. You need to search for the index of the target value in the array.
# If the value is present in the array, then return its index. Otherwise, determine the index where it would be inserted in the array while maintaining the sorted order.


from typing import List

def find_or_get_insert_position(nums: List[int], x: int):
  lb = 0
  ub = len(nums) - 1
  ans = len(nums)
  while lb <= ub:
    mid = (lb+ub) // 2
    if nums[mid] >= x:
      ans = mid 
      ub = mid - 1
    else:
      lb = mid + 1
  return ans

    

if __name__ == "__main__":
  nums = [1,5,7,8,9,12,14]
  x = 6
  print(find_or_get_insert_position(nums,x))