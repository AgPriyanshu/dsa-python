# Given a string array nums of length n. A string is called a complete string if every prefix of this string is also present in the array nums.
# Find the longest complete string in the array nums.
# If there are multiple strings with the same length, return the lexicographically smallest one and if no string exists, return "None" (without quotes).


class Node:
  def __init__(self):
    self.links = [None]*26
    self.flag = False

  def insert(self,character):
    newNode = Node()
    self.links[self._ctoi(character)] = newNode
    return newNode
  
  def get(self,character):
    return self.links[self._ctoi(character)]

  def contains(self,character):
    return self.links[self._ctoi(character)] is not None

  def isEnd(self):
    return self.flag

  
  def _ctoi(self,character):
    return ord(character) - ord('a')


class Trie:
    def __init__(self):
      self.root = Node()      

    def insert(self, word):
      current = self.root
      for letter in word:
        if not current.contains(letter):
          current.insert(letter)
        
        current = current.get(letter)
      
      current.flag = True


    def search(self, word):
      current = self.root
      for letter in word:
        if current.contains(letter):
          current = current.get(letter)
      
      return current.isEnd()      
    
    def checkAllPrefixExists(self,word):
      current = self.root
      for letter in word:
        if current.contains(letter):
          current = current.get(letter)
        if not current.isEnd():
          return False
      return True

    def startsWith(self, prefix):
      current = self.root
      for letter in prefix:
        if current.contains(letter):
          current = current.get(letter)
        else:
          return False
      return True

class Solution:
    def completeString(self, nums):
      trie = Trie()
      for num in nums:
        trie.insert(num)
      
      max_len = 0
      max_val = None
      for num in nums:
        if trie.checkAllPrefixExists(num): 
          if len(num) > max_len:
            max_len = len(num)
            max_val = num
          elif max_len == len(num) and max_val > num:
            max_val = num

      return max_val

if __name__ == "__main__":
  nums = ["z","y","a"]
  print(Solution().completeString(nums))
