# Given an integer array nums, return the length of the longest strictly increasing subsequence.
# A subsequence is a sequence derived from an array by deleting some or no elements without changing the order of the remaining elements. For example, [3, 6, 2, 7] is a subsequence of [0, 3, 1, 6, 2, 2, 7].
# The task is to find the length of the longest subsequence in which every element is greater than the previous one.

class Solution:
    # Helper function to find the length of LIS
    def func(self, i, prevInd, arr, dp):
        
        # base case
        if i == len(arr) - 1:
            if prevInd == -1 or arr[prevInd] < arr[i]:
                return 1
            return 0
        
        # If subproblem is already calculated
        if dp[i][prevInd + 1] != -1:
            return dp[i][prevInd + 1]
        
        # Not Take case
        notTake = self.func(i + 1, prevInd, arr, dp)
        
        take = 0  # Take case
        
        # If no element is chosen till now
        if prevInd == -1:
            take = self.func(i + 1, i, arr, dp) + 1
        
        # Else the current element can be 
        # taken if it is strictly increasing
        elif arr[i] > arr[prevInd]:
            take = self.func(i + 1, i, arr, dp) + 1
        
        # Return the maximum length obtained from both cases
        dp[i][prevInd + 1] = max(take, notTake)
        return dp[i][prevInd + 1]

    # Function to find the longest increasing 
    # subsequence in the given array
    def LIS(self, nums):
        n = len(nums)

        # DP array
        dp = [[-1] * (n + 1) for _ in range(n)]

        return self.func(0, -1, nums, dp)



if __name__ == "__main__":
  nums = [-39,-14,94,34,-19,-70,-1,-62,-64,28,99,-24,74,-71,13,78,-85,51,-70,-70,-63,51,42,71,31,-70,100,-47]
  print(Solution().LIS(nums))