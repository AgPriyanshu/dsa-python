# Given a string nums representing a non-negative integer, and an integer k, find the smallest possible integer after removing k digits from num.
# Note: If removing k digits deletes all digits, return "0". The result must be a valid non-negative integer without leading zeros.

class Solution:
    def removeKdigits(self, nums: str, k: int) -> str:
      if k >= len(nums):
        return '0'
      stack = []
      for i in range(len(nums)):
        while stack and k > 0 and stack[-1] > nums[i]:
          stack.pop()
          k -= 1
        stack.append(nums[i])
      
      while k > 0 and stack:
        stack.pop()
        k -= 1


      ans = "".join(stack)
      
      ans = ans.lstrip('0')
      if ans == '':
        return '0'
      return ans
      
nums = "541892"
k = 2
print(Solution().removeKdigits(nums,k))
          
       
