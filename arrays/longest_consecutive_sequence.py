# Given an array nums of n integers.
# Return the length of the longest sequence of consecutive integers. The integers in this sequence can appear in any order.

class Solution:
  def sol1(self,nums):
    nums_sorted = sorted(nums)
    max_count = 0
    prev = nums_sorted[0]
    count= 1
    for ind in range(1,len(nums_sorted)):
      if prev == nums_sorted[ind]:
        continue
      elif prev + 1 == nums_sorted[ind]:
        count += 1
        max_count = max(count,max_count)
      else:
        count = 1
      prev = nums_sorted[ind]

    return max_count
  
  def optimal(self,nums):
    nums_set = set(nums)
    longest = 0
    for val in nums_set:
      if val - 1 in nums_set:
        continue
      x = val
      count = 1
      while x + 1 in nums_set:
        count += 1
        x = x + 1
      longest = max(count,longest)

    return longest

  def longestConsecutive(self, nums):
    return self.optimal(nums)

if __name__ == "__main__":
  nums = [-19,-9,15,2,7,16,11,-16,2,13,-8,2,1,16,18,-5,-13,-14,-9,-2,9,12,7,-1,15,-6,3,-9]
  print(Solution().longestConsecutive(nums))