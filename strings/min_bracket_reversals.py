# Given a string s consisting of only opening and closing brackets '(' and ')', find out the minimum number of reversals required to convert the string into a balanced expression.


# If it is not possible to make the brackets balanced, return -1. A reversal means changing '(' to ')' or vice-versa.

class Solution:
    def countRev(self, s: str) -> int:
        if len(s) % 2 != 0:
          return -1

        open,close = 0,0

        for bracket in s:
          if bracket == '(':
            open += 1
          elif bracket == ')' and open > 0:
            open -= 1
          else:
            close += 1

        ans = int(close/2) + int(close%2) + int(open/2) + int(open%2)
        return ans            


s = ")(())((("
print(Solution().countRev(s))