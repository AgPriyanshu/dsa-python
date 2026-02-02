# You are given a 2D matrix grid of size N × M, where each cell contains either 0 or 1. Find the number of distinct islands where a group of connected 1s (horizontally or vertically) forms an island. Two islands are considered to be same if and only if one island is equal to another (not rotated or reflected).
class Solution:
  def __init__(self):
    self.dirRow = [-1, 0, 1, 0]
    self.dirCol = [0, 1, 0, -1]
  
  def isValid(self,i,j,row,col):
    if i < 0 or i >= row:
      return False
    if j < 0 or j >= col:
      return False
    return True

  def dfs(self,i,j,grid,visited,path,start):
    row, col = len(grid), len(grid[0])
    visited[i][j] = True
    path.append(f'{i-start[0]},{j-start[1]}')
    for move in range(4):
      i2 = i + self.dirRow[move]
      j2 = j + self.dirCol[move]

      if self.isValid(i2,j2,row,col) and not visited[i2][j2] and grid[i2][j2] == 1:
        self.dfs(i2,j2,grid,visited,path,start)
     

    return path

  def countDistinctIslands(self, grid):
    row, col = len(grid), len(grid[0])
    visited = [[False]*col for _ in range(row)]
    islands = set()
    for i in range(row):
      for j in range(col):
        if not visited[i][j] and grid[i][j] == 1:
          shape = []
          self.dfs(i,j,grid,visited,shape,(i,j))
          islands.add(''.join(shape))

    return len(islands)

if __name__ == "__main__":
  grid = [[0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0], [1, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1], [1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0], [0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0], [1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1], [0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0], [1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1], [1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0], [1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1], [1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0], [0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1], [1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0], [0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0], [0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0], [1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1], [1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1], [0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0], [1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0], [0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], [0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1]]
  print(Solution().countDistinctIslands(grid))  