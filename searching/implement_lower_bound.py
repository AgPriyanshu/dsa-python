from typing import List

def get_lower_bound(nums: List[int], target):
  lb = 0
  ub = len(nums) - 1
  ans = len(nums)
  while lb <= ub:
    mid = (lb+ub)//2
    if nums[mid] >= target:
      ans = mid
      ub = mid - 1
    else:
      lb = mid + 1
  return ans

if __name__ == "__main__":
  nums = [1,2,2,3]
  target = 2
  print(get_lower_bound(nums,target))