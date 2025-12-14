# Given an array arr of n integers and an integer target, determine if there is a subset of the given array with a sum equal to the given target.

class Solution:
  def check_subset_sum(self,arr,target,i,dp):
    if i >= len(arr):
      return False

    if dp.get(f'{i}-{target}') is not None:
      return dp.get(f'{i}-{target}')

    temp = target - arr[i]

    if temp == 0:
      return True 


    pick = self.check_subset_sum(arr,temp,i+1,dp)
    not_pick = self.check_subset_sum(arr,target,i+1,dp)

    dp[f'{i}-{target}'] = pick  or not_pick
    return pick or not_pick

  def isSubsetSum(self, arr, target):
    dp = {}
    if target == 0:
      return True
    return self.check_subset_sum(arr,target,0,dp)

if __name__ == "__main__":
  arr = [1, 2, 3]
  target = 0
  print(Solution().isSubsetSum(arr,target))