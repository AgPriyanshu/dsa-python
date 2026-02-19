# Given an array arr of size n containing elements, find the next greater element for each element in the array in the order of their appearance.


# The next greater element of an element in the array is the nearest element on the right that is greater than the current element.


# If there does not exist a next greater element for the current element, then the next greater element for that element is -1.

class Solution:
    def nextLargerElement(self, arr):
      stack = []
      ans = [-1]*len(arr)

      for i in range(len(arr)-1,-1,-1):
        while len(stack) > 0 and stack[-1] <= arr[i]:
            stack.pop()
                
        if len(stack) > 0:
            ans[i] = stack[-1]
        
        stack.append(arr[i])

      return ans


arr = [818,809,65,563,300,428,32,706,286,874,181,980,974,461,316,106,974,624,313]


print(Solution().nextLargerElement(arr))
# 874 874 563 706 428 706 706 874 874 980 980 -1 974 974 974 974 -1 -1 -1
# 874 874 563 706 428 706 706 874 874 980 980 -1 -1 974 974 974 -1 -1 -1