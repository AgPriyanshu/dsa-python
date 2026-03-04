# A celebrity is a person who is known by everyone else at the party but does not know anyone in return. Given a square matrix M of size N x N where M[i][j] is 1 if person i knows person j, and 0 otherwise, determine if there is a celebrity at the party. Return the index of the celebrity or -1 if no such person exists.

class Solution:
  def celebrity(self, M):
    top = 0
    right = len(M)-1
    while top != right:
      if M[top][right] == 1:
        top += 1
      elif M[right][top] == 1:
        right -=1
      else:
        top +=1 
        right -=1



    all_zeroes = True
    for j in range(len(M)):
      if top != j and M[top][j] != 0:
        all_zeroes =False
        break

    if not all_zeroes:
      return -1
    
    all_ones = True
    for i in range(len(M)):
      if i != right and M[i][right] != 1:
        all_ones = False
        break
    if not all_ones:
      return -1
    
    return top
M = [ [0, 1], [1, 0] ]
print(Solution().celebrity(M))