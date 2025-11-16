# Given a grid of size N x M (N is the number of rows and M is the number of columns in the grid) consisting of '0's (Water) and ‘1's(Land). Find the number of islands.
# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically or diagonally i.e., in all 8 directions.

directions = [[[-1,-1],[-1,0],[-1,1]],
              [[0,-1],[0,0],[0,1]],
              [[1,-1],[1,0],[1,1]]
              ]

class Solution:
  def dfs(self,i,j,grid,visited):
    visited[i][j] = 1
    col,rows = len(grid[0]),len(grid)
    for k in range(3):
      for l in range(3):
        i2 = i + directions[k][l][0]
        j2 = j + directions[k][l][1]
        if (i2 > -1 and i2 < rows) and (j2 > -1 and j2 < col) and visited[i2][j2] == 0 and grid[i2][j2] == '1':
          self.dfs(i2,j2,grid,visited)


  def numIslands(self, grid):
    row,col = len(grid), len(grid[0])
    visited = [ [0]*col for _ in range(row)]
    count = 0
    for i in range(row):
      for j in range(col):
        if (visited[i][j]==0) and grid[i][j] == '1':
          self.dfs(i,j,grid,visited)
          count +=1
    return count



if __name__ == "__main__":
  s = Solution()
  grid = [ ['1', '1', '1', '0', '1'], ['1', '0', '0', '0', '0'], ['1', '1', '1', '0', '1'], ['0', '0', '0', '1', '1'] ]
  print(s.numIslands(grid))