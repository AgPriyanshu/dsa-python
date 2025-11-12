# Problem Statement: Given a string s, return the longest palindromic substring in s.

def check_palindrome_from_center(s:str,left: int,right:int,maxLength: int):
  ans = ''
  while left >= 0 and right < len(s) and s[left] == s[right]: 

    if (right - left + 1) > maxLength:
      maxLength = right - left + 1       
      ans = s[left:right+1]
    left -= 1
    right += 1
  return ans


def longest_palindromic_substr(s: str):
  ans = ""
  maxLength = 0
  n = len(s)
  for index in range(n):
    left,right = index,index
    odd_string = check_palindrome_from_center(s,left,right,maxLength)
    even_string = check_palindrome_from_center(s,left,right+1,maxLength)
    maxLength = max(len(odd_string),len(even_string),maxLength)
 
    if len(odd_string) == maxLength:
      ans = odd_string
    elif len(even_string) == maxLength:
      ans = even_string
    
  
  return ans

if __name__ == "__main__":
  s = "bb"
  print(longest_palindromic_substr(s))