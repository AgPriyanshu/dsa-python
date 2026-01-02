# Given two strings s and t. Find the smallest window substring of s that includes all characters in t (including duplicates) , in the window. Return the empty string "" if no such substring exists.

class Solution:
  def check_maps(self,letter_map,substring_map):
    # print(letter_map)
    for substring_letter in substring_map:
      if letter_map.get(substring_letter,-1) < substring_map[substring_letter]:
        return False
    return True

  def minWindow(self, string: str, t: str) -> str:
    l,r = 0,0
    letter_map = {}
    substring_map = {}
    for lt in t:
      substring_map[lt] = substring_map.get(lt,0) + 1
    min_substr = ''

    while r < len(string):
      letter = string[r]
      letter_map[letter] = letter_map.get(letter,0) + 1

      while self.check_maps(letter_map,substring_map) and l <= r:
        substr = string[l:r+1] 
        if min_substr == '':
          min_substr = substr
        elif len(substr) < len(min_substr):
          min_substr = substr
        
        letter_map[string[l]] -= 1
        if letter_map[string[l]] == 0:
          del letter_map[string[l]] 
        l += 1
      r += 1
    return min_substr


if __name__ == "__main__":
  input_s = "a"
  t = "a"
  print(Solution().minWindow(input_s,t))