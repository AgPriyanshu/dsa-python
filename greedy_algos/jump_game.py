# Given an array of integers nums, each element in the array represents the maximum jump length at 
# that position. Initially starting at the first index of the array, determine if it is possible to reach 
# the last index. Return true if the last index can be reached, otherwise return false.
class Solution:
  def canJump(self, nums):
    maxIndex = 0
    for i in range(len(nums)-1):
      if maxIndex < i:
        return False
      maxIndex = max(i+nums[i],maxIndex)
    
    return maxIndex >= (len(nums) - 1)



if __name__ == "__main__":
  nums =[3,7,8,4,7,8,4,0,3,7,4,0,7,9,4,9,2,5,4,3,6,2,6,5,3,6,0,0,4,0,4,8,6,0,3,8,2,2,0,9,8,3,1,2,9,4,0,2,0,5,2,2,0,1,0,6,6,3,9,4,2,6,4,8]
  print(Solution().canJump(nums))