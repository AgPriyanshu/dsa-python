# A ninja has planned a n-day training schedule. Each day he has to perform one of three activities - running, stealth training, or fighting practice. The same activity cannot be done on two consecutive days and the ninja earns a specific number of merit points, based on the activity and the given day.
# Given a n x 3-sized matrix, where matrix[i][0], matrix[i][1], and matrix[i][2], represent the merit points associated with running, stealth and fighting practice, on the (i+1)th day respectively. Return the maximum possible merit points that the ninja can earn.
class Solution:
    def findMax(self, matrix, day, last, dp):
        n = len(matrix)
        if day == n:
            return 0

        # map last (-1 for "no previous") to dp column index 3
        last_idx = 3 if last == -1 else last
        if dp[day][last_idx] != -1:
            return dp[day][last_idx]

        best = 0
        for act in range(3):
            if act != last:
                points = matrix[day][act] + self.findMax(matrix, day + 1, act, dp)
                if points > best:
                    best = points

        dp[day][last_idx] = best
        return best

    def ninjaTraining(self, matrix):
        if not matrix:
            return 0
        n = len(matrix)
        # dp rows = days, cols = 4 (3 activities + 1 sentinel for "no last")
        dp = [[-1] * 4 for _ in range(n)]
        return self.findMax(matrix, 0, -1, dp)


if __name__ == "__main__":
    matrix = [[10, 40, 70],
              [20, 50, 80],
              [30, 60, 90]]
    print(Solution().ninjaTraining(matrix))  # prints 240
