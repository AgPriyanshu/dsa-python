# Given an integer k and a string s, any character in the string can be selected and changed to any other uppercase English character. This operation can be performed up to k times. After completing these steps, return the length of the longest substring that contains the same letter.

class Solution:
  def get_count_apart_max_key(self,letter_map,max_key):
    count = 0
    for key in letter_map:
      if key != max_key:
        count += letter_map[key]
    return count

  def characterReplacement_opt(self, s: str, k: int) -> int:
    l = 0
    r = 0
    n = len(s)
    max_len = 0
    letter_map = {}
    s_l = None
    while r < n:     
      letter = s[r]
      letter_map[letter] = letter_map.get(letter,0) + 1
      window_count = r-l+1
      if s_l == None:
        s_l = letter
      elif letter != s_l and letter_map[letter] >= letter_map[s_l]:
        s_l = letter
    
      if window_count - letter_map[s_l] > k:
        letter_map[s[l]] -= 1
        if letter_map[s[l]] == 0:
          del letter_map[s[l]]
        l +=1   

      elif window_count - letter_map[s_l] <=k:
        max_len = max(max_len,window_count)

      r += 1
    return max_len

  def characterReplacement(self, s: str, k: int) -> int:
    l = 0
    r = 0
    n = len(s)
    max_len = 0
    letter_map = {}
    while r < n:
     
      letter = s[r]
      letter_map[letter] = letter_map.get(letter,0) + 1
      
      max_key = max(letter_map, key=letter_map.get)
      count_apart_max_key = self.get_count_apart_max_key(letter_map,max_key)    
      print(letter_map,max_key,count_apart_max_key)
      if count_apart_max_key > k:
        letter_map[s[l]] -= 1
        if letter_map[s[l]] == 0:
          del letter_map[s[l]]
        l +=1   
      elif count_apart_max_key <=k:
        max_len = max(max_len,r-l+1)

      r += 1
    return max_len

if __name__ == "__main__":
  s = "CCACE"
  k = 3
  print(Solution().characterReplacement_opt(s,k))   