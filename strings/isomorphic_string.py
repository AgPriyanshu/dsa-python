# Problem Statement: Given two strings s and t, determine if they are isomorphic. Two strings s and t are isomorphic if the characters in s can be replaced to get t.
# All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself. 

def are_isomorphic(s: str,t: str):
  if len(s) != len(t):
    return False
  
  hash_map = {}
  hash_map2 = {}

  for index in range(len(s)):
    s_value = hash_map.get(s[index])
    t_value = hash_map2.get(t[index])

    if s_value and t_value and (s_value != t[index] or t_value != s[index]):
      return False
    elif not s_value and t_value:
      return False
    elif not t_value and s_value:
      return False

    hash_map[s[index]] = t[index]
    hash_map2[t[index]] = s[index]      
  return True

if __name__ == "__main__":
  s = 'babc'
  t = 'bada'
  print(are_isomorphic(s,t))