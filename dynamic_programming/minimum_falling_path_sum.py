# Given a 2d array called matrix consisting of integer values. Return the minimum path sum that can be obtained by starting at any cell in the first row and ending at any cell in the last row.
# Movement is allowed only to the bottom, bottom-right, or bottom-left cell of the current cell.

import sys
class Solution:
  def dfs(self,matrix,i,j,dp):
    if i >= len(matrix) or j>= len(matrix[0]) or j < 0 or i < 0:
      return '-1'

    if i == len(matrix)-1:
      return matrix[i][j]

    if dp[i][j] != -1:
      return dp[i][j]

    mini = sys.maxsize

    for k in [-1,0,1]:
      temp = self.dfs(matrix,i+1,j+k,dp)
      if temp != '-1':
        val = matrix[i][j] + temp 
        if val < mini:
          mini = val

    dp[i][j] = mini


    return mini



  def minFallingPathSum(self, matrix):
    mini = sys.maxsize
    dp = [[-1 for i in range(len(matrix[0]))] for j in range(len(matrix))]
    # self.dfs(matrix,0,0)
    for j in range(len(matrix[0])):
      val =  self.dfs(matrix,0,j,dp)
      # print(val)
      if  val < mini:
        mini = val

    return mini
if __name__ == "__main__":
  matrix = [[1, 2, 10, 4], [100, 3, 2, 1], [1, 1, 20, 2], [1, 2, 2, 1]]
  print(Solution().minFallingPathSum(matrix))