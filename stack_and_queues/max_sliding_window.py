# Given an array of integers arr, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position. Return the max sliding window.
from collections import deque

class Solution:
  def maxSlidingWindow(self, arr, k):
    q = deque()
    ans = []
    for i in range(len(arr)):
      if q and q[0] <= (i-k):
        q.popleft()

      while q and arr[q[-1]] < arr[i]:
        q.pop()

      q.append(i)
      
      if i >= (k-1) and q:
        ans.append(arr[q[0]])


    return ans
     
  
arr = [4, 0, -1, 3, 5, 3, 6, 8] 
k = 3
print(Solution().maxSlidingWindow(arr,k))