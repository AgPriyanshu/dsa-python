# Given a string s, sort it in decreasing order based on the frequency of the characters.
# The frequency of a character is the number of times it appears in the string.

def sort_by_frequency(s: str):
  if len(s) == 0 or len(s) == 1:
    return s

  hash_map = {}

  for letter in s:
    if count := hash_map.get(letter):
      hash_map[letter] = count + 1
    else:
      hash_map[letter] = 1
  
  sorted_keys = sorted(hash_map.keys(),key=lambda x: hash_map[x], reverse=True)

  ans = ''

  for key in sorted_keys:
    count = hash_map[key]
    while count != 0:
      ans += key
      count -= 1

  return ans

if __name__ == "__main__":
  s = 'tree'
  print(sort_by_frequency(s))