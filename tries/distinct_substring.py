# Given a string s, determine the number of distinct substrings (including the empty substring) of the given string.
# A string B is a substring of a string A if B can be obtained by deleting several characters (possibly none) from the start of A and several characters (possibly none) from the end of A.
# Two strings X and Y are considered different if there is at least one index i such that the character of X at index i is different from the character of Y at index i (X[i] != Y[i]).

class Node:
  def __init__(self):
    self.links = [None]*26

  def insert(self,character):
    newNode = Node()
    self.links[self._ctoi(character)] = newNode
    return newNode
  
  def get(self,character):
    return self.links[self._ctoi(character)]

  def contains(self,character):
    return self.links[self._ctoi(character)] is not None
  
  def _ctoi(self,character):
    return ord(character) - ord('a')


class Trie:
    def __init__(self):
      self.root = Node()      
      self.distinctStrings = 0

    def insert(self, word):
      current = self.root
      for letter in word:
        if not current.contains(letter):
          current.insert(letter)
          self.distinctStrings += 1
        
        current = current.get(letter)
      
      current.flag = True


    def search(self, word):
      current = self.root
      for letter in word:
        if current.contains(letter):
          current = current.get(letter)
      
      return current.isEnd()      

    def startsWith(self, prefix):
      current = self.root
      for letter in prefix:
        if current.contains(letter):
          current = current.get(letter)
        else:
          return False
      return True

class Solution:
    def countDistinctSubstring(self, s):
      trie = Trie()
      for i in range(len(s)):
        for j in range(i,len(s)):
          trie.insert(s[i:j+1])

      return trie.distinctStrings + 1

if __name__ == "__main__":
  print(Solution().countDistinctSubstring("aba"))