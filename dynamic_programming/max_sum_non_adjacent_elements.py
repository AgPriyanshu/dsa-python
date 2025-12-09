# from time import time


# # Given an array of ‘N’  positive integers, we need to return the maximum sum of the subsequence such that no two elements of the subsequence are adjacent elements in the array.
# def max_sum_non_adjacent(arr, i):
#     if i >= len(arr):
#         return 0
#     pick = arr[i] + max_sum_non_adjacent(arr, i + 2)
#     not_pick = 0 + max_sum_non_adjacent(arr, i + 1)
#     return max(pick, not_pick)


# def max_sum_non_adjacent_dp(arr, n, dp):
#     if n < 0:
#         return 0
#     if n == 0:
#         return arr[n]

#     if dp.get(n) is not None:
#         return dp[n]

#     pick = max_sum_non_adjacent_dp(arr, n - 2, dp) + arr[n]
#     not_pick = max_sum_non_adjacent_dp(arr, n - 1, dp) + 0

#     dp[n] = max(pick, not_pick)

#     return dp[n]


# def max_sum_table(arr):
#     n = len(arr)
#     dp = []
#     dp[0] = 0
#     for i in range(1, n):
#         pick = arr[i]

#         if i > 1:
#             pick += dp[i - 2]

#         # Calculate the maximum value when not picking the current element
#         non_pick = 0 + dp[i - 1]

#         # Store the maximum of the two choices in the DP table
#         dp[i] = max(pick, non_pick)

#     return dp[n]


# if __name__ == "__main__":
#     start = time()
#     print(max_sum_non_adjacent_dp([1, 8, 7, 2, 3, 4], 5, []))
#     # print(max_sum_non_adjacent([1, 8, 7, 2, 3, 4], 0))
#     end = time()
#     print("Time Taken:", end - start)


class Solution:
    def non_adjacent(self, nums, i, dp):
        if i < 0:
            return 0
        if i in dp:
            return dp[i]
        # pick current
        pick = nums[i] + self.non_adjacent(nums, i-2, dp)
        # don't pick current
        not_pick = self.non_adjacent(nums, i-1, dp)
        dp[i] = max(pick, not_pick)
        return dp[i]

    def nonAdjacent(self, nums):
        if not nums:
            return 0
        dp = {}
        return self.non_adjacent(nums, len(nums)-1, dp)

if __name__ == "__main__":
    print(Solution().nonAdjacent( [1,1000,1,1000,1,1000]))

