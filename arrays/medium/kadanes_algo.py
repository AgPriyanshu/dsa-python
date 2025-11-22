# Given an integer array nums, find the subarray with the largest sum and return the sum of the elements present in that subarray.
# A subarray is a contiguous non-empty sequence of elements within an array.
import sys

class Solution:
    def maxSubArray(self, nums):
      maxVal = -sys.maxsize
      sum = 0
      for index,value in enumerate(nums):
        if sum < 0:
            sum = 0
        sum += value
        if sum > maxVal:
          maxVal = sum

      return maxVal


if __name__ == "__main__":
  nums =  [2, 3, 5, -2, 7, -4]
  print(Solution().maxSubArray(nums))