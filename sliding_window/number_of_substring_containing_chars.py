# Given a string s , consisting only of characters 'a' , 'b' , 'c'.Find the number of substrings that contain at least one occurrence of all these characters 'a' , 'b' , 'c'.

class Solution:    
  def check_string_match(self,substring_map):
    for char_key in substring_map:
      if substring_map[char_key] == -1:
        return False
    return True

  def numberOfSubstrings(self, s: str) -> int:
    substring_map = {char:-1 for char in "abc"}
    r = 0
    count = 0
    while r < len(s):
      substring_map[s[r]] = r
      if self.check_string_match(substring_map):
        count += 1 + substring_map[min(substring_map,key=substring_map.get)] 
      r += 1

    return count
if __name__ == "__main__":
  s = "ccabcc"
  print(Solution().numberOfSubstrings(s))