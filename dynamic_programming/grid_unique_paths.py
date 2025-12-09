# Given two integers m and n, representing the number of rows and columns of a 2d array named matrix. Return the number of unique ways to go from the top-left cell (matrix[0][0]) to the bottom-right cell (matrix[m-1][n-1]).
# Movement is allowed only in two directions from a cell: right and bottom.


class Solution:
  def dfs(self,m,n,i,j,dp):
    if i >= m or j >=n:
      return 0
    if i == m-1 and j == n-1:
      return 1
    elif dp[i][j] != -1:
      return dp[i][j]

    right = self.dfs(m,n,i,j+1,dp)
    bottom = self.dfs(m,n,i+1,j,dp)

    dp[i][j] = right + bottom

    return dp[i][j]

  def uniquePaths(self, m, n):
    dp = [[-1 for j in range(n)] for i in range(m)]
    return self.dfs(m,n,0,0,dp)

if __name__ == "__main__":
  m,n = 2,4
  print(Solution().uniquePaths(m,n))