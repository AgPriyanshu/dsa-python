# Given an array arr of n integers, return true if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal else return false.

class Solution:
  def min_diff(self,n,arr,i,sum1,sum2,dp):
    if i >= n:
      return abs(sum1-sum2)

    if dp.get(f'{i}-{sum1}-{sum2}') is not None:
      return dp.get(f'{i}-{sum1}-{sum2}')

    pick_sum1 = self.min_diff(n,arr,i+1,sum1+arr[i],sum2,dp)
    pick_sum2 = self.min_diff(n,arr,i+1,sum1,sum2+arr[i],dp)

    minDiff = min(pick_sum1,pick_sum2)

    dp[f'{i}-{sum1}-{sum2}'] = minDiff

    return minDiff
    
  def minDifference(self, arr,n):
    dp = {}
    return self.min_diff(n,arr,0,0,0,dp) 
  
if __name__ == "__main__":
  arr =  [3, 1, 6, 2, 2]
  n = len(arr)
  print(Solution().minDifference(arr,n))

