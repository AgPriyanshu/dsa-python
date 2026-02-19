# Given a circular integer array arr, return the next greater element for every element in arr.


# The next greater element for an element x is the first element greater than x that we come across while traversing the array in a clockwise manner.


# If it doesn't exist, return -1 for that element.

class Solution:
    def nextGreaterElements(self, arr):
      stack = []
      ans = [-1]*len(arr)
      n = len(arr)  
      for i in range((2*n)-1,-1,-1):
        element = arr[i%n]
        while len(stack) > 0 and stack[-1] <= element:
            stack.pop()
                
        if len(stack)  > 0:
            ans[i%n] = stack[-1]
        
        stack.append(element)

      return ans


arr = [3, 10, 4, 2, 1, 2, 6, 1, 7, 2, 9]


print(Solution().nextGreaterElements(arr))
# 874 874 563 706 428 706 706 874 874 980 980 -1 974 974 974 974 -1 -1 -1
# 874 874 563 706 428 706 706 874 874 980 980 -1 -1 974 974 974 -1 -1 -1