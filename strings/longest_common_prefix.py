# Problem Statement: Write a function to find the longest common prefix string amongst an array of strings. 
# If there is no common prefix, return an empty string "".
import sys

def lcp(strs: str):
  to_match = strs[0]
  ans = ''
  min_count = sys.maxsize


  for index in range(1,len(strs),1):
    s = strs[index]

    if len(s) >= 1 and len(to_match) >= 1 and s[0] != to_match[0]:
      return ""
    else:
      i = 0
      j = 0
      s_len = len(s)
      count = 0
      str_temp = ''
      while i < s_len and j < len(to_match):
        if s[i] == to_match[j]:
          count += 1
          str_temp += s[i]
        else:
          break
        i +=1
        j +=1

      
      if count < min_count: 
        min_count = count
        ans = str_temp
  return ans

if __name__ == "__main__":
  strs =  ["aaa","aa","aaa"]
  print(lcp(strs))