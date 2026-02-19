# Given an array of non-negative integers, height representing the elevation of ground. Calculate the amount of water that can be trapped after rain.
class Solution:
  def trap(self, height):
    l,r = 0,len(height)-1
    lmax,rmax = 0,0
    total = 0
    while l < r:
      left_val =height[l]
      right_val =height[r]

      if left_val <= right_val:
        l += 1
        if lmax > left_val:
          total += lmax - left_val
        elif lmax < left_val:
          lmax = left_val
      else:
        r -=1
        if rmax > right_val:
          total += rmax - right_val
        elif rmax < right_val:
          rmax = right_val
    
    return total


height= [4, 2, 0, 3, 2, 5]
print(Solution().trap(height))
