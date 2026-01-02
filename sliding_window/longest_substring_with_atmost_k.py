# Given a string s and an integer k.Find the length of the longest substring with at most k distinct characters.

class Solution:
  def kDistinctChar(self, s, k):
    letter_map = {}
    l,r = 0,0
    max_len = 0
    while r < len(s):
      letter_map[s[r]] = letter_map.get(s[r],0) + 1
      if len(letter_map) > k:
        letter_map[s[l]] -= 1
        if letter_map[s[l]] == 0:
          del letter_map[s[l]]          
        l += 1
      elif len(letter_map) <=k:
        max_len = max(max_len,r-l+1)

      r += 1
    return max_len

if __name__ == "__main__":
  # s = "aababbcaacc" 
  # k = 2
  s = "abcddefg"
  k = 3
  print(Solution().kDistinctChar(s,k))