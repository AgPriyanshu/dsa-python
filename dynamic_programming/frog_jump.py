# A frog wants to climb a staircase with n steps. Given an integer array heights, where heights[i] contains the height of the ith step, and an integer k.


# To jump from the ith step to the jth step, the frog requires abs(heights[i] - heights[j]) energy, where abs() denotes the absolute difference. The frog can jump from the ith step to any step in the range [i + 1, i + k], provided it exists.


# Return the minimum amount of energy required by the frog to go from the 0th step to the (n-1)th step.

class Solution:
    def jump(self,heights,k,n,dp):
        if n <= 0:
            return 0
        if dp.get(n) is not None:
            return dp[n]

        energies = []

        for i in range(1,k+1):
            dp[n-i] = self.jump(heights,k,n-i,dp)
            energies.append(abs(heights[n] - heights[n-i]) + dp[n-i])
        
        dp[n] = 0 if len(energies) == 0 else min(energies) 
        return dp[n]

    def frogJump(self, heights, k):
        dp = {}
        dp[0] = 0
        return self.jump(heights,k,len(heights)-1,dp)


if __name__ == "__main__":
    print(Solution().frogJump([10,5,20,0,15],2))