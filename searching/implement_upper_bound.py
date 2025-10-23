from typing import List

def get_upper_bound(nums: List[int], target):
  lb = 0
  ub = len(nums) - 1
  ans = len(nums)
  while lb <= ub:
    mid = (lb+ub)//2
    if nums[mid] > target:
      ans = mid
      ub = mid - 1
    else:
      lb = mid + 1
  return ans

if __name__ == "__main__":
  nums = [3,5,8,9,15,19]
  target = 9
  print(get_upper_bound(nums,target))