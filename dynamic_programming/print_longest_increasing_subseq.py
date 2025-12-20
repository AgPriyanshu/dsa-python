# Given an array of n integers arr, return the Longest Increasing Subsequence (LIS) that is Index-wise Lexicographically Smallest.
# The Longest Increasing Subsequence (LIS) is the longest subsequence where all elements are in strictly increasing order.
# A subsequence A1 is Index-wise Lexicographically Smaller than another subsequence A2 if, at the first position where A1 and A2 differ, the element in A1 appears earlier in the array arr than corresponding element in S2.
# Your task is to return the LIS that is Index-wise Lexicographically Smallest from the given array.

class Solution:
    def recur(self,nums,i,prev_i,dp):
        if i >= len(nums):
            return 0
        
        if dp[i][prev_i+1] != -1:
            return dp[i][prev_i+1]
        not_pick = 0 + self.recur(nums,i+1,prev_i,dp)
        pick = 0
        if nums[i] > nums[prev_i] or prev_i == -1:
            pick = 1 + self.recur(nums,i+1,i+1,dp)

        dp[i][prev_i+1] = max(not_pick,pick)      
        return max(not_pick,pick)       

    def table(self,nums):
        n = len(nums)
        dp = [[0] * (n+1) for _ in range(n+1)]        

        for i in range(n-1,-1,-1):
            for prev_i in range(i - 1,-2,-1):
                not_pick = 0 + dp[i+1][prev_i+1]

                if prev_i == -1 or nums[i] > nums[prev_i]: 
                   pick = 1 + dp[i+1][i+1]
                
                dp[i][prev_i+1] = max(not_pick,pick)

        return dp[0][0]
    
    def optimal(self,nums): 
        n = len(nums)
        dp = [1] * n
        prev = list(range(n))
        maxi = 0  
        max_index = -1  
        for i in range(n):
            for j in range(0,i):
                if nums[j] < nums[i] and dp[i] < dp[j] + 1:
                    dp[i] = dp[j]+1
                    prev[i] = j
            if maxi < dp[i]:
                maxi = dp[i]
                max_index = i
        j = max_index
        ans = [nums[j]]
        while j != 0:
            j = prev[j]
            ans.append(nums[j])
        return list(reversed(ans))
        


    def longestIncreasingSubsequence(self, nums):
        # n = len(nums)
        # dp = [[-1] * (n + 1) for _ in range(n)]
        # return self.recur(nums,0, -1,  dp)
        return self.optimal(nums)



if __name__ == "__main__":
  nums = [10, 22, 9, 33, 21, 50, 41, 60, 80]
  print(Solution().longestIncreasingSubsequence(nums))