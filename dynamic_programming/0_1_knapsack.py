# Given two integer arrays, val and wt, each of size N, which represent the values and weights of N items respectively, and an integer W representing the maximum capacity of a knapsack, determine the maximum value achievable by selecting a subset of the items such that the total weight of the selected items does not exceed the knapsack capacity W.
# Each item can either be picked in its entirety or not picked at all (0-1 property). The goal is to maximize the sum of the values of the selected items while keeping the total weight within the knapsack's capacity.

class Solution:
  def recur(self,wt,val,n,W,i,w,dp):
    if i == n:
      return 0

    if dp.get(f'{i}-{w}'):
      return dp.get(f'{i}-{w}')

    sum_w = w + wt[i]
    pick = 0

    if sum_w <= W:
      pick = val[i] + self.recur(wt,val,n,W,i+1,sum_w,dp)
    not_pick = 0 + self.recur(wt,val,n,W,i+1,w,dp)

    dp[f'{i}-{w}'] = max(pick,not_pick)

    return max(pick,not_pick)

  def knapsack01(self, wt, val, n, W):
    dp = {}
    return self.recur(wt,val,n,W,0,0,dp)

if __name__ == "__main__":
  # val = [34, 71, 6, 60, 54, 66, 48, 24, 51, 58, 83, 40, 78, 35, 78, 50, 36, 99, 50, 62, 8, 66, 89, 70, 57, 86, 76, 36, 27]
  # wt = [36, 64, 29, 58, 37, 8, 68, 85, 60, 66, 59, 8, 15, 41, 40, 76, 32, 39, 45, 71, 39, 100, 60, 21, 29, 15, 28, 21, 56]
  # W = 650

  val =[10, 40, 30, 50]
  wt =  [5, 4, 6, 3]
  W = 10
  n = len(wt)
  print(Solution().knapsack01(wt,val,n,W))