# Problem Statement: Given two strings, check if two strings are anagrams of each other or not.

def is_anagram(s: str,t: str):
  if len(s) != len(t):
    return False

  hash_map = {}
  for letter in s:
    if count := hash_map.get(letter):
      hash_map[letter] = count + 1
    else:
      hash_map[letter] = 1
  
  for letter in t:
    if count := hash_map.get(letter):
      count -=1 
      if count < 0:
        return False
      else:
        hash_map[letter] = count
    else:
      return False
      
  for value in hash_map.values():
    if value != 0:
      return False

  return True

if __name__ == "__main__":
  s = "anagraw" 
  t = "nagaram"
  print(is_anagram(s,t))