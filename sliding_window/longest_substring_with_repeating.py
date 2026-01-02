# Given a string, S. Find the length of the longest substring without repeating characters.
class Solution:
  def longestNonRepeatingSubstring(self, s):
    char_map = {}
    l = 0
    r = 0
    max_len = 0
    while r < len(s):
      if char_map.get(s[r]) and char_map.get(s[r]) >=l:
        l = char_map[s[r]] + 1
      
      char_map[s[r]] = r
      max_len = max(max_len,r-l+1)
      r += 1
    return max_len

if __name__ == "__main__":
  s = "aaabbbccc"
  print(Solution().longestNonRepeatingSubstring(s))
