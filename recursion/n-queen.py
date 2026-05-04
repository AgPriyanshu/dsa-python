# The challenge of arranging n queens on a n × n chessboard so that no two queens attack one another is known as the "n-queens puzzle."


# Return every unique solution to the n-queens puzzle given an integer n. The answer can be returned in any sequence.


# # Every solution has a unique board arrangement for the placement of the n-queens, where 'Q' and '.' stand for a queen and an empty space, respectively.


class Solution:
    def isSafe(self, board, row, col):
        r, c = row, col

        # Check for upper left diagonal
        while r >= 0 and c >= 0:
            if board[r][c] == 'Q':
                return False
            r -= 1
            c -= 1

        # Reset to the original position
        r, c = row, col

        # Check for top
        while r >= 0:
            if board[r][c] == 'Q':
                return False
            r -= 1

        # Reset to the original position
        r, c = row, col

        # Check for top right diagonal
        while r >= 0 and c < len(board[0]):
            if board[r][c] == 'Q':
                return False
            r -= 1
            c += 1

        # If no queens are found, it's safe
        return True


    def recur(self,i,board,ans):
      if i == len(board):
        ans.append(board)

      for j in range(len(board)):
        if self.isSafe(board,i,j):
          board[i][j] = 1
          self.recur(i+1,board,ans)
          board[i][j] = 0

      return 




    def solveNQueens(self, n):
       board = [[0]*n]*n
       ans = []
       self.recur(0,board,ans)
       return ans



if __name__ == "__main__":
  print(Solution().solveNQueens(4))