# Given an integer r, return all the values in the rth row (1-indexed) in Pascal's Triangle in correct order.
# In Pascal's triangle:
#     The first row has one element with a value of 1.
#     Each row has one more element in it than its previous row.
#     The value of each element is equal to the sum of the elements directly above it when arranged in a triangle format.


class Solution:
    def pascalTriangleII(self, r):
      ans = 1
      print(ans,end=' ')
      for i in range(1,r):
        ans = ans * (r - i)
        ans = ans // i
        print(ans,end=' ')

if __name__ == "__main__":
  r = 6
  Solution().pascalTriangleII(r)
