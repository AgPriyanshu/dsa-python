# You are given a matrix mat of size N x M where each cell contains either 'O' or 'X'.

# Your task is to replace all 'O' cells that are completely surrounded by 'X' with 'X'.


# Rules:

#     An 'O' (or a group of connected 'O's) is considered surrounded if it is not connected to any border of the matrix.
#     Two 'O' cells are considered connected if they are adjacent horizontally or vertically (not diagonally).
#     A region of connected 'O's that touches the border (i.e., first row, last row, first column, or last column) is not surrounded and should not be changed.
from collections import deque
class Solution:
  def __init__(self):
    self.dirRow = [-1,0,1,0]
    self.dirCol = [0,-1,0,1]

  def isValid(self,i,j,row,col):
    if i < 0 or i >= row:
      return False
    elif j < 0 or j >= col:
      return False
    return True

  def bfs(self,q,mat,visited):
    row, col = len(mat),len(mat[0])
    
    while q:
      i,j = q.popleft()
      visited[i][j] = True
      for move in range(4):
        i2 = i + self.dirRow[move]
        j2 = j + self.dirCol[move]

        if self.isValid(i2,j2,row,col)and  not visited[i2][j2] and mat[i2][j2] == 'O':
          visited[i2][j2] = True
          q.append((i2,j2))

  def fill(self, mat):
    row, col = len(mat),len(mat[0])
    q = deque()
    visited = [[False]*col for _ in range(row)]
    for i in range(row):
      for j in range(col):
        if (i== 0 or i == row-1 or j==0 or j==col-1) and mat[i][j] == 'O':
          q.append((i,j))

    self.bfs(q,mat,visited)

    for i in range(row):
      for j in range(col):
        if not visited[i][j] and mat[i][j] == 'O':
          mat[i][j] = 'X'

    return mat

if __name__ == "__main__":
  mat = [ ["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "O", "X", "X"] ]
  print(Solution().fill(mat))