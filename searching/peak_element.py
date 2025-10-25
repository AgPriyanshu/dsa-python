# Problem Statement: Given an array of length N, peak element is defined as the element greater than both 
# of its neighbors. Formally, if arr[i] is the peak element, arr[i - 1] < arr[i] and arr[i + 1] < arr[i]. Find the index(0-based) of a peak element in the array. If there are multiple peak numbers, return the index of any peak number. 

from typing import List
def peak_element(nums: List[int]):
  lb = 0
  ub = len(nums) - 1
  
  while lb < ub:
    mid = (lb + ub) // 2
    if nums[mid - 1] < nums[mid] and nums[mid + 1 ] < nums[mid]:
      return mid
    elif nums[mid+1] > nums[mid]:
      lb = mid + 1
    else:
      ub = mid
  return lb


if __name__ == "__main__":
  nums = [1,2,1,3,5,6,4]
  print(peak_element(nums))