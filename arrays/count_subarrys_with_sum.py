# Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.
from collections import defaultdict
class Solution:
  def subarraySum(self, nums, k):
    prefix_sum = defaultdict(int)
    prefix_sum[0] = 1
    sum = 0
    count = 0
    for num in nums:
      sum += num      
      subarray_sum_to_remove = sum - k
      count += prefix_sum[subarray_sum_to_remove]
      prefix_sum[sum] += 1

    return count    



if __name__ == "__main__":
  nums = [-5,-3,0,-9,-6,1,5,-7,-1,0,3,5,9]
  k = 0
  print(Solution().subarraySum(nums,k))