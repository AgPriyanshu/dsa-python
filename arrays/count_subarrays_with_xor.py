# Given an array of integers nums and an integer k, return the total number of subarrays whose XOR equals to k.
from collections import defaultdict
class Solution:
  def subarraysWithXorK(self, nums, k):
    xor_till_i = defaultdict(int)
    prev = 0
    xor_till_i[prev] =  1
    count = 0

    for ind in range(len(nums)):
      prev = prev ^ nums[ind]
      x_to_remove_from_subarray_to_get_k = prev ^ k
      count += xor_till_i[x_to_remove_from_subarray_to_get_k]
      xor_till_i[prev] += 1
    return count




if __name__ == "__main__":
  nums = [5, 6, 7, 8, 9]
  k = 5
  print(Solution().subarraysWithXorK(nums,k))