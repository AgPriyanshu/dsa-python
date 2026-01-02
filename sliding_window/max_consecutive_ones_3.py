# Given a binary array nums and an integer k, flip at most k 0's.

# Return the maximum number of consecutive 1's after performing the flipping operation.

class Solution:
  def longestOnes(self, nums, k):
    left = 0
    r = 0
    k2 = k
    max_len = 0
 
    while r < len(nums):
      if nums[r] == 1:
        r += 1
        max_len = max(max_len,r-left)
      elif nums[r] == 0 and k2 > 0:
        r += 1
        k2 -=1
        max_len = max(max_len,r-left)
      else:
        if nums[left] == 0:
          left += 1
          k2 += 1
        else:
          while left < r and nums[left] != 0:
            left += 1
          left += 1
          k2 +=1

    return max_len



if __name__ == "__main__":
  nums = [1,0,0,1,1,0,1,1,0,0,1,1,1,0,0,1,1,1,0,1,0,0,1,1,1,1,0,0,1,1,1,0,0,1,1,0,0,1,1,1,1,0,0,1,1,1,0,1,1,1,0,0,0,1,1,0,0,0,0,0,0,1,1,0,0,1,1,0,0,1,0,0,1,1,0,0,0,1,1,0,0,1,1,1,1,1,1,1,0,1,0,1,1,0,0,0,1,0,0,1,1,0,0,0,1,1,1,0,1,1,1,0,1,1,1,0,1,1,0,0,1,1,1,0,1,1,1,1,0,1,0,0,0,1,0,1,0,1,0,0,1,0,1,1,0,1,0,0,1,1,1,1,0,1,1,1,1,1,0,1,0,1,1,0,1,0,0,0,1,0,0,0,0,0,1,0,0,1,1,0,1,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,1,0,1,1,0,1,1,1,0,0,1,1,0,1,1,1,0,1,1,1,1,0,1,1,1,0,1,0,0,0,0,0,1,0,1,1,1,0,0,0,1,0,0,0,1,1,1,0,1,1,0,1,1,1,0,1,0,1,0,0,1,0,0,1,1,1,1,0,0,0,1,1,0,1,0,1,1,1,0,1,0,0,1,1,0,0,0,0,1,1,0,1,0,1,0,1,1,0,0]
  k = 197
  print(Solution().longestOnes(nums,k))
