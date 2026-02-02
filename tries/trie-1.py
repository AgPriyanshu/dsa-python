# Implement the Trie class:
#     Trie(): Initializes the trie object.
#     void insert (String word): Inserts the string word into the trie.
#     boolean search (String word): Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
#     boolean startsWith (String prefix): Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.

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

    def startsWith(self, prefix):
      current = self.root
      for letter in prefix:
        if current.contains(letter):
          current = current.get(letter)
        else:
          return False
      return True
