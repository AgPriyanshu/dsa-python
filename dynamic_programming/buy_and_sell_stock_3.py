# Given an array, arr, of n integers, where arr[i] represents the price of the stock on an ith day, determine the maximum profit achievable by completing at most two transactions in total.
# Holding at most one share of the stock at any time is allowed, meaning buying and selling the stock twice is permitted, but the stock must be sold before buying it again. Buying and selling the stock on the same day is allowed.

class Solution:
  def recur(self,arr,n,i,buy,dp,cap):
    if i >= n:
      return 0
      
    if cap == 0:
      return 0

    if dp[i].get(f'{buy}{cap}') is not None:
      return dp[i].get(f'{buy}{cap}')

    profit = 0
    
    if buy == 0:    
      profit = max(0 + self.recur(arr,n,i+1,0,dp,cap),(-1)*arr[i] + self.recur(arr,n,i+1,1,dp,cap))
    else:
      profit = max(0 + self.recur(arr,n,i+1,1,dp,cap), arr[i] + self.recur(arr,n,i+1,0,dp,cap-1))

    dp[i][f'{buy}{cap}'] = profit

    return profit

  def stockBuySell(self, arr, n):
    dp = [{} for i in range(n)]
    return self.recur(arr,n,0,0,dp,2)

if __name__ == "__main__":
  arr = [4, 2, 7, 1, 11, 5]
  n  = len(arr)
  print(Solution().stockBuySell(arr,n))
