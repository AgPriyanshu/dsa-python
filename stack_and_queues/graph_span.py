# Given an array arr of size n, where each element arr[i] represents the stock price on day i. Calculate the span of stock prices for each day.
# The span Si for a specific day i is defined as the maximum number of consecutive previous days (including the current day) for which the stock price was less than or equal to the price on day i.

class Solution:
  def stockSpan(self, arr, n):
    stack = []
    ans = [0] * n
    ans[0] = 1
    stack.append(0)
    for i in range(1,n):
      while stack and arr[stack[-1]] <= arr[i]:
        stack.pop()
      ans[i] = (i-stack[-1]) if stack else i+1
      stack.append(i)
    return ans


    

n = 6
arr = [15, 13, 12, 14, 16, 20]
print(Solution().stockSpan(arr,n))
