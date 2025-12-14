# Given a n x m 2d integer array called matrix where matrix[i][j] represents the number of cherries you can pick up from the (i, j) cell.Given two robots that can collect cherries, one is located at the top-leftmost (0, 0) cell and the other at the top-rightmost (0, m-1) cell.
# Return the maximum number of cherries that can be picked by the two robots in total, following these rules:
#     Robots that are standing on (i, j) cell can only move to cell (i + 1, j - 1), (i + 1, j), or (i + 1, j + 1), if it exists in the matrix.
#     A robot will pick up all the cherries in a given cell when it passes through that cell.
#     If both robots come to the same cell at the same time, only one robot takes the cherries.
#     Both robots must reach the bottom row in matrix.

import sys
class Solution:
  def dfs(self,matrix,i,j1,j2,dp):
    if i >= len(matrix) or j1>= len(matrix[0]) or j2>= len(matrix[0]) or j1 < 0 or  j2 < 0 or i < 0:
      return '-1'

    if i == len(matrix)-1:
      if j1 == j2:
        return matrix[i][j1]
      else:
        return matrix[i][j1] + matrix[i][j2]

    if dp[i][j1][j2] != -1:
      return dp[i][j1][j2]
    maxi = -sys.maxsize

    for dj1 in [-1,0,1]:
      for dj2 in [-1,0,1]:
        temp = self.dfs(matrix,i+1,j1+dj1,j2+dj2,dp)
        if temp != '-1':
          if j1 == j2:
              maxi = max(maxi,matrix[i][j1] + temp)
          else:
            if temp != '-1':
              maxi = max(maxi,matrix[i][j1] + matrix[i][j2] + temp)

    dp[i][j1][j2] = maxi
    return maxi



  def cherryPickup(self, matrix):
    n,m = len(matrix),len(matrix[0])
    dp = [[[-1 for j in range(m)] for i in range(m)] for k in range(n)]
    return self.dfs(matrix,0,0,m-1,dp)

if __name__ == "__main__":
  matrix = [[2, 1, 3], [4, 2, 5], [1, 6, 2], [7, 2, 8]]
  print(Solution().cherryPickup(matrix))