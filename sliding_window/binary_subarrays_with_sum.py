# Given a binary array nums and an integer goal. Return the number of non-empty subarrays with a sum goal.
# A subarray is a continuous part of the array.

class Solution:
  def helper(self,nums,goal):
    sum = 0
    l,r = 0,0
    count = 0
    if goal < 0:
      return 0
    while r < len(nums):
      sum += nums[r]

      while sum > goal:
        sum -= nums[l]
        l += 1

      count += r-l+1
      r += 1
    return count

  def numSubarraysWithSum(self, nums, goal):
    return self.helper(nums,goal) - self.helper(nums,goal-1)
    

if __name__ == "__main__":
  nums = [1, 1, 0, 1, 0, 0, 1] 
  goal = 3
  print(Solution().numSubarraysWithSum(nums,goal))