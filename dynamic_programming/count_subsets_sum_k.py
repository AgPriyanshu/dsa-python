# Given an array arr of n integers and an integer K, count the number of subsets of the given array that have a sum equal to K. Return the result modulo (109 + 7).

class Solution:
  def find_sum(self,arr,target,i,dp):
    if i >= len(arr):
      if target == 0:
        return 1
      return 0

    if dp.get(f'{i}-{target}') is not None:
      return dp.get(f'{i}-{target}')

    temp = target - arr[i]

    pick = self.find_sum(arr,temp,i+1,dp)
    not_pick = self.find_sum(arr,target,i+1,dp)

    dp[f'{i}-{target}'] = pick + not_pick

    return pick + not_pick

  def perfectSum(self, arr, target):
    dp = {}
    mod = (10**9 + 7)
    return self.find_sum(arr,target,0,dp)  % mod

if __name__ == "__main__":
  arr = [13,3,6,14,3,7,2,3,4,15,20,7,15,5,14,1,2,10,15,6,1,20,7,15,14,7,20,15,16,17,12,16,16,13,13,12,8,15,2,3]
  K = 10
  print(Solution().perfectSum(arr,K))

     
