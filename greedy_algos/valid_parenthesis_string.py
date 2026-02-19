class Solution(object):
    def isValid(self, s):
      min = 0
      max = 0
      for letter in s:
        if letter == '(':
          min += 1
          max += 1
        elif letter == ')':
          if min != 0:
            min -= 1
        else:
          if min != 0 :
            min -= 1
          max += 1
      return min == 0
