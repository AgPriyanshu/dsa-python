# Given an n x m grid, where each cell has the following values : 
# 2 - represents a rotten orange
# 1 - represents a Fresh orange
# 0 - represents an Empty Cell
# Every minute, if a fresh orange is adjacent to a rotten orange in 4-direction ( upward, downwards, right, and left ) it becomes rotten. 
# Return the minimum number of minutes required such that none of the cells has a Fresh Orange. If it's not possible, return -1.

from collections import deque           

class Solution:
    delRow = [-1, 0, 1, 0]
    delCol = [0, 1, 0, -1]

    def isValid(self,nRow,nCol,i,j):
      if nRow <= i or i < 0:
        return False
      
      if nCol <= j or j < 0:
        return False

      return True
    
    def orangesRotting(self, grid):
      n,m = len(grid), len(grid[0])
      q = deque()
      time = 0
      total = 0
      count = 0
      for i in range(n):
        for j in range(m):            
            # If cell contains orange, 
            # increment total
            if grid[i][j] != 0:
                total += 1
                
            # If cell contains rotten 
            # orange, push in queue
            if grid[i][j] == 2:
                q.append((i, j))

      while q:
        k = len(q)
        count += k
        for _ in range(k):
          row, col = q.popleft()
          for i in range(4):
            row2 = row + self.delRow[i]
            col2 = col + self.delCol[i]
            if self.isValid(n,m,row2,col2) and grid[row2][col2] == 1:
              grid[row2][col2] = 2
              q.append((row2,col2))

        if q:
            time += 1
      if total == count:
          return time
      return -1

if __name__ == '__main__':
  image = [[2,1,1,0,1,1,0,1,1,2,1,1,0,1,1,0,1,1,2,1],[1,0,1,1,0,1,1,2,1,1,0,1,1,0,1,1,2,1,1,0],[1,1,0,1,1,2,1,1,0,1,1,0,1,1,2,1,1,0,1,1],[0,1,1,2,1,1,0,1,1,0,1,1,2,1,1,0,1,1,0,1],[1,2,1,1,0,1,1,0,1,1,2,1,1,0,1,1,0,1,1,2],[1,1,0,1,1,0,1,1,2,1,1,0,1,1,0,1,1,2,1,1],[0,1,1,0,1,1,2,1,1,0,1,1,0,1,1,2,1,1,0,1],[1,0,1,1,2,1,1,0,1,1,0,1,1,2,1,1,0,1,1,0],[1,1,2,1,1,0,1,1,0,1,1,2,1,1,0,1,1,0,1,1],[2,1,1,0,1,1,0,1,1,2,1,1,0,1,1,0,1,1,2,1],[1,0,1,1,0,1,1,2,1,1,0,1,1,0,1,1,2,1,1,0],[1,1,0,1,1,2,1,1,0,1,1,0,1,1,2,1,1,0,1,1],[0,1,1,2,1,1,0,1,1,0,1,1,2,1,1,0,1,1,0,1],[1,2,1,1,0,1,1,0,1,1,2,1,1,0,1,1,0,1,1,2],[1,1,0,1,1,0,1,1,2,1,1,0,1,1,0,1,1,2,1,1],[0,1,1,0,1,1,2,1,1,0,1,1,0,1,1,2,1,1,0,1],[1,0,1,1,2,1,1,0,1,1,0,1,1,2,1,1,0,1,1,0],[1,1,2,1,1,0,1,1,0,1,1,2,1,1,0,1,1,0,1,1],[2,1,1,0,1,1,0,1,1,2,1,1,0,1,1,0,1,1,2,1],[1,0,1,1,0,1,1,2,1,1,0,1,1,0,1,1,2,1,1,0]]
  print(Solution().orangesRotting(image))