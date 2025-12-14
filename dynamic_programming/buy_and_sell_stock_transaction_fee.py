# Given an array arr where arr[i] represents the price of a given stock on the ith day. Additionally, you are given an integer fee representing a transaction fee for each trade. The task is to determine the maximum profit you can achieve such that you need to pay a transaction fee for each buy and sell transaction. The Transaction Fee is applied when you sell a stock.
# You may complete as many transactions. You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before buying again).

class Solution:
  def recur(self,arr,n,i,buy,dp,fee):
    if i >= n:
      return 0
      

    if dp[i].get(buy) is not None:
      return dp[i].get(buy)

    profit = 0
    
    if buy == 0:    
      profit = max(0 + self.recur(arr,n,i+1,0,dp,fee),(-1)*arr[i] + self.recur(arr,n,i+1,1,dp,fee))
    else:
      profit = max(0 + self.recur(arr,n,i+1,1,dp,fee), arr[i] - fee + self.recur(arr,n,i+1,0,dp,fee))

    dp[i][buy] = profit

    return profit

  def stockBuySell(self, arr, n,fee):
    dp = [{} for i in range(n)]
    return self.recur(arr,n,0,0,dp,fee)

if __name__ == "__main__":
  arr = [1, 3, 4, 0, 2]
  n  = len(arr)
  fee = 1
  print(Solution().stockBuySell(arr,n,fee))
