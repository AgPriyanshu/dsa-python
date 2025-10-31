# Problem Statement: You are given a string s and a positive integer k.
# Return the number of substrings that contain exactly k distinct characters.

def count_substrs(s: str,k: int):
  i = 0
  j = 0
  hash_map = {}
  count = 0
  while  j < len(s):
    hash_map[s[j]] = hash_map.get(s[j],0) + 1

    while len(hash_map) > k:      
      hash_map[s[i]] -= 1      
      if hash_map[s[i]] == 0:
        del hash_map[s[i]]
      i += 1

    count += (j - i) + 1
    j += 1

  return count

if __name__ == "__main__":
  s = "pqpqs"  
  k = 2  
  print(count_substrs(s,k))