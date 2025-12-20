# Given an integer n, return the first n (1-Indexed) rows of Pascal's triangle.
# In Pascal's triangle:
#     The first row has one element with a value of 1.
#     Each row has one more element in it than its previous row.
#     The value of each element is equal to the sum of the elements directly above it when arranged in a triangle format.

class Solution:
    def pascalTriangleII(self, r):
      ans = 1
      result = []
      result.append(ans)
      for i in range(1,r):
        ans = ans * (r - i)
        ans = ans // i
        result.append(ans)
      return result

    def pascalTriangleIII(self, n):
      ans = []
      for i in range(1,n+1):
        ans.append(self.pascalTriangleII(i))
      return ans


if __name__ == "__main__":
  r = 6
  print(Solution().pascalTriangleIII(r))
