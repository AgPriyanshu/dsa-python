
# Given two integers m and n, representing the number of rows and columns of a 2d array named matrix. Return the number of unique ways to go from the top-left cell (matrix[0][0]) to the bottom-right cell (matrix[m-1][n-1]).
# Movement is allowed only in two directions from a cell: right and bottom.


class Solution:
  def dfs(self,matrix,i,j,dp):
    if (i >= len(matrix) or j >= len(matrix[0])) or matrix[i][j] == 1:
      return 0
    if i == len(matrix) -1  and j == len(matrix[0]) -1 :
      return 1
    elif dp[i][j] != -1:
      return dp[i][j]

    right = self.dfs(matrix,i,j+1,dp)
    bottom = self.dfs(matrix,i+1,j,dp)

    dp[i][j] = right + bottom

    return dp[i][j]

  def uniquePathsWithObstacles(self, matrix):
    dp = [[-1 for j in range(len(matrix[0]))] for i in range(len(matrix))]
    return self.dfs(matrix,0,0,dp)

if __name__ == "__main__":
  matrix = [[0, 0, 0], [0, 0, 1], [0, 1, 0]]
  print(Solution().uniquePathsWithObstacles(matrix))