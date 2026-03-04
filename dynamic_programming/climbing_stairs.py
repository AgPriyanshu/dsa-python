# Problem Statement: Given a number of stairs. Starting from the 0th stair we need to climb to the “Nth” stair.
# At a time we can climb either one or two steps. We need to return the total number of distinct ways to reach from 0th to Nth stair.


dp = {}
class Solution:

    def climbStairs(self, n):
        if dp.get(n):
            return dp.get(n)
        elif n <= 1:
            return 1
        else:
            dp[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)

        return dp[n]
