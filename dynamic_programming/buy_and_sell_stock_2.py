# Given an array arr of n integers, where arr[i] represents price of the stock on the ith day. Determine the maximum profit achievable by buying and selling the stock any number of times.
# Holding at most one share of the stock at any given time is allowed, meaning buying and selling the stock can be done any number of times, but the stock must be sold before buying it again. Buying and selling the stock on the same day is permitted.

class Solution:
  def recur(self,arr,n,i,buy,dp):
    if i >= n:
      return 0

    if dp[i][buy] != -1:
      return dp[i][buy]

    profit = 0
    
    if buy == 0:    
      profit = max(0 + self.recur(arr,n,i+1,0,dp),(-1)*arr[i] + self.recur(arr,n,i+1,1,dp))
    else:
      profit = max(0 + self.recur(arr,n,i+1,1,dp), arr[i] + self.recur(arr,n,i+1,0,dp))

    dp[i][buy] = profit

    return profit

  def stockBuySell(self, arr, n):
    dp = [[-1 for i in range(2)] for i in range(n)]
    return self.recur(arr,n,0,0,dp)

if __name__ == "__main__":
  arr = [9, 2, 6, 4, 7, 3]
  n  = len(arr)
  print(Solution().stockBuySell(arr,n))
