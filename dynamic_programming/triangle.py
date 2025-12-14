# Given a 2d integer array named triangle with n rows. Its first row has 1 element and each succeeding row has one more element in it than the row above it.
# Return the minimum falling path sum from the first row to the last.
# Movement is allowed only to the bottom or bottom-right cell from the current cell.
import sys
class Solution:
  def dfs(self,matrix,i,j,dp):
    if i >= len(matrix) or j>= len(matrix[i]):
      return '-1'

    if i == len(matrix)-1:
      return matrix[i][j]

    if dp[i][j] != -1:
      return dp[i][j]

    mini = sys.maxsize

    for k in [0,1]:
      temp = self.dfs(matrix,i+1,j+k,dp)
      if temp != '-1':
        val = matrix[i][j] + temp 
        if val < mini:
          mini = val

    dp[i][j] = mini


    return mini

  def minTriangleSum(self, matrix):
    dp = [[-1 for i in range(len(matrix[-1]))] for j in range(len(matrix))]
    return self.dfs(matrix,0,0,dp)

if __name__ == "__main__":
  matrix = [[1], [4, 7], [4,10, 50], [-50, 5, 6, -100]]
  print(Solution().minTriangleSum(matrix))