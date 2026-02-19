# Given an array of integers heights representing the histogram's bar height where the width of each bar is 1 return the area of the largest rectangle in the histogram.

class Solution:
  def get_nse(self,arr):
    stack = []
    ans = [len(arr)]*len(arr)
    for i in range(len(arr)-1,-1,-1):
      while stack and arr[stack[-1]] >= arr[i]:
        stack.pop()
      ans[i] = stack[-1] if stack else len(arr)
      stack.append(i)
    return ans
      

  def get_pse(self,arr):
    stack = []
    ans = [-1]*len(arr)
    for i in range(len(arr)):
      while stack and arr[stack[-1]] >= arr[i]:
        stack.pop()

      ans[i] = stack[-1] if stack else len(arr)

      stack.append(i)
    return ans

  def largestRectangleArea(self, heights):
    nse = self.get_nse(heights)
    pse = self.get_pse(heights)
    max_height = 0
    for i in range(len(heights)):
      max_height = max(max_height,(nse[i] - pse[i] - 1 )*heights[i])
    return max_height

  def largestRectangleAreaOptimal(self, heights):
    stack = []
    max_area = 0
    for i in range(len(heights)):
      while stack and heights[stack[-1]] >= heights[i]:
        element = stack.pop()
        nse = i
        pse = stack[-1] if stack else -1
        area = heights[element] * (nse - pse - 1 )
        max_area = max(max_area,area)

      stack.append(i)

    while stack:
      element = stack.pop()
      nse = len(heights)
      pse = stack[-1] if stack else -1
      area = heights[element] * (nse - pse - 1 )
      max_area = max(max_area,area)


    return max_area

heights = [3, 5, 1, 7, 5, 9]



print(Solution().largestRectangleAreaOptimal(heights))