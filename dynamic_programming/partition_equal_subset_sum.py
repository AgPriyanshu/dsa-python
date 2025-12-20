# Given an array arr of n integers, return true if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal else return false.

class Solution:
  def check_equal_partition(self,n,arr,i,sum1,sum2,dp):
    if i >= n:
      if sum1 == sum2:
        return True
      return False

    if dp.get(f'{i}-{sum1}-{sum2}') is not None:
      return dp.get(f'{i}-{sum1}-{sum2}')

    pick_sum1 = self.check_equal_partition(n,arr,i+1,sum1+arr[i],sum2,dp)
    pick_sum2 = self.check_equal_partition(n,arr,i+1,sum1,sum2+arr[i],dp)

    dp[f'{i}-{sum1}-{sum2}'] = pick_sum1 or pick_sum2
    
    return pick_sum1 or pick_sum2 
    
  def equalPartition(self, n, arr):
    dp = {}
    return self.check_equal_partition(n,arr,0,0,0,dp) 
  
if __name__ == "__main__":
  arr = [1, 2, 3, 5]
  n = len(arr)
  print(Solution().equalPartition(n,arr))

