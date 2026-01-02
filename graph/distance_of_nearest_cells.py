# Given a binary grid of N x M. Find the distance of the nearest 1 in the grid for each cell.
# The distance is calculated as |i1 - i2| + |j1 - j2|, where i1, j1 are the row number and column number of the current cell, and i2, j2 are the row number and column number of the nearest cell having value 1.
from collections import deque

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

  def bfs(self,q,grid,visited,distance):
    row,col = len(grid),len(grid[0])
    while q:
    
      i,j,d = q.popleft()
      distance[i][j] = d
      for move in range(4):
        i2 = i + self.dirRow[move]
        j2 = j + self.dirCol[move]

        if self.isValid(i2,j2,row,col) and visited[i2][j2] == 0:
          visited[i2][j2] = 1
          q.append((i2,j2,d+1))


  def nearest(self, grid):
    row,col = len(grid),len(grid[0])
    visited = [[0]*col for _ in range(row)]
    distance = [[0]*col for _ in range(row)]
    q = deque()

    for i in range(row):
      for j in range(col):
        if grid[i][j] == 1:
          q.append((i,j,0))
          visited[i][j] = 1

    self.bfs(q,grid,visited,distance)
    

    return distance

if __name__ == "__main__":
  grid = [ [1, 0, 1], [1, 1, 0], [1, 0, 0] ]
  print(Solution().nearest(grid))

  