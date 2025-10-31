# Problem Statement: Given a string s, representing a large integer, the task is to return the largest-valued odd integer (as a string) that is a substring of the given string s.
# The number returned should not have leading zero's. But the given input string may have leading zero. 
import sys

def largest_odd_substring(num: str):
  s2 = num.strip('0')
  ans = -1
  for i in range(len(s2)-1,-1,-1):
    print(i,len(s2))
    if int(s2[i]) % 2 == 1:
      ans = i
      break
  return s2[:ans+1]




if __name__ == "__main__":
  print(largest_odd_substring('12')) 