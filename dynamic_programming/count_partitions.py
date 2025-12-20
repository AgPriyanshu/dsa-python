# Given an array arr of n integers and an integer diff, count the number of ways to partition the array into two subsets S1 and S2 such that:
#     ∣S1−S2∣ = diff and S1 ≥ S2
#     Where |S1| and |S2| are sum of Subsets S1 and S2 respectively.
# Return the result modulo 109 + 7.
# Note: A partition means that the union of S1 and S2 is the original array, and no element is left out or used twice — every element of the array belongs to exactly one of the two subsets.

class Solution:
  def recur(self,n,diff,arr,i,s1,s2,dp):
    if i >= n:
      if s1 - s2 == diff and s1 >= s2:
        return 1
      return 0

    if dp.get(f'{i}-{s1}-{s2}') is not None:
      return dp.get(f'{i}-{s1}-{s2}')
    
    pick_s1 = self.recur(n,diff,arr,i+1,s1+arr[i],s2,dp)
    pick_s2 = self.recur(n,diff,arr,i+1,s1,s2+arr[i],dp)
    dp[f'{i}-{s1}-{s2}'] = pick_s1 + pick_s2
    return pick_s1 + pick_s2

  def countPartitions(self, n, diff, arr):
    dp = {}
    mod = (10**9 + 7)
    return self.recur(n,diff,arr,0,0,0,dp) % mod

if __name__ == "__main__":
  arr = [1, 2, 3, 4]
  diff = 2
  n = len(arr)
  print(Solution().countPartitions(n,diff,arr))