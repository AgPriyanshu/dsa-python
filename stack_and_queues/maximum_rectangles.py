# Given a m x n binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.
class Solution:
    def get_max_area(self,arr):
      stack = []
      max_area = 0
      for i in range(len(arr)):

        while stack and arr[stack[-1]] >= arr[i]:
          height = arr[stack.pop()]
          nse = i
          pse = stack[-1] if stack else -1
          max_area = max(max_area,height * (nse - pse - 1))
        
        stack.append(i)

      while stack:
        height = arr[stack.pop()]
        nse = len(arr)
        pse = stack[-1] if stack else -1
        max_area = max(max_area,height * (nse - pse - 1))

      return max_area      

    def maximalAreaOfSubMatrixOfAll1(self, matrix):
      # Compute prefix sums to create historgram for each row.
      n = len(matrix)
      m = len(matrix[0])
      largest_rectangle = 0

      for j in range(m):
        prefix_sum = 0
        for i in range(n):
          if matrix[i][j] != 0:
            prefix_sum += matrix[i][j]
            matrix[i][j] = prefix_sum
          else:
            prefix_sum = 0

      for i in range(n):
        largest_rectangle = max(largest_rectangle,self.get_max_area(matrix[i]))
      return largest_rectangle

matrix =[[1,1,0,0,0,0,0,1,1,0,1,0,1,1,0,1,1],[1,1,1,1,1,0,1,1,1,0,1,1,1,0,1,0,1],[1,1,0,0,0,1,1,1,1,0,1,1,1,1,1,1,1],[1,1,0,1,1,0,1,1,0,1,1,0,1,0,0,0,0],[1,1,0,0,0,1,1,0,0,0,0,1,0,1,1,0,1],[0,1,0,1,1,1,0,1,1,1,0,0,0,1,0,1,1],[1,1,0,1,0,0,0,0,1,0,0,1,0,1,1,1,0],[0,1,1,0,1,1,1,1,1,1,1,0,0,1,1,0,1],[1,1,1,1,1,1,0,0,0,1,1,1,1,0,0,1,1],[0,0,0,1,1,1,1,1,1,1,1,0,1,1,1,0,0],[0,1,1,1,1,1,1,1,0,0,0,0,0,0,1,1,1],[0,1,1,0,1,1,0,0,1,1,1,0,0,1,1,1,1],[0,0,0,1,0,1,1,1,0,0,1,1,0,0,0,0,1],[1,0,0,1,0,1,0,0,0,1,1,1,1,0,1,0,1],[1,0,1,0,1,1,1,0,0,0,1,1,0,1,1,0,1],[0,1,0,0,1,1,1,1,0,1,0,0,0,1,1,1,0],[1,0,0,0,1,1,1,1,0,1,1,1,0,0,0,1,0],[0,1,0,0,0,1,0,1,1,0,0,0,1,0,1,1,1],[1,0,0,1,1,1,0,0,1,1,0,1,0,1,1,1,0],[1,1,1,1,0,0,1,0,1,1,0,0,1,1,0,1,1],[1,1,1,1,0,0,0,0,1,1,1,0,1,0,1,1,0],[1,1,1,0,1,1,0,0,0,1,0,0,1,0,1,1,0],[0,1,0,0,1,0,0,0,0,0,0,1,1,0,0,0,1],[0,1,0,1,0,0,1,0,0,1,1,0,0,1,1,0,1],[0,1,1,0,0,0,0,0,0,1,0,0,0,1,1,0,0],[0,0,1,0,1,1,0,1,1,1,1,0,1,0,0,1,0],[0,0,1,1,1,1,1,1,1,1,0,1,1,1,0,1,1],[0,0,1,0,0,1,1,1,1,1,0,1,0,1,1,0,0],[1,1,1,0,1,0,1,1,0,1,0,0,1,0,0,1,0]]
print(Solution().maximalAreaOfSubMatrixOfAll1(matrix))