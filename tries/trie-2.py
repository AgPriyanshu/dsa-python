# Implement the Trie class:
#     Trie(): Initializes the trie object.
#     void insert (String word): Inserts the string word into the trie.
#     boolean search (String word): Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
#     boolean startsWith (String prefix): Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.

class Node:
  def __init__(self,wordCount=0,prefixCount=0):
    self.links = [None]*26
    self.wordCount = wordCount
    self.prefixCount = prefixCount

  def insert(self,character):
    newNode = Node(prefixCount=1)
    self.links[self._ctoi(character)] = newNode
    return newNode
  
  def get(self,character):
    return self.links[self._ctoi(character)]
  
  def getAndErase(self,character):
    node = self.links[self._ctoi(character)]
    node.prefixCount -= 1
    return node


  def getAndIncrementPrefixCount(self,character):
    node = self.links[self._ctoi(character)]
    node.prefixCount += 1
    return node

  def contains(self,character):
    return self.links[self._ctoi(character)] is not None

  def isEnd(self):
    return self.wordCount != 0

  
  def _ctoi(self,character):
    return ord(character) - ord('a')


class Trie:
    def __init__(self):
      self.root = Node()      

    def insert(self, word):
      current = self.root
      for letter in word:
        if not current.contains(letter):
          current = current.insert(letter)
        else:
          current = current.getAndIncrementPrefixCount(letter)
      
      current.wordCount += 1


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
    
    def countWordsEqualTo(self, word):
      current = self.root
      for letter in word:
        if current.contains(letter):
          current = current.get(letter)
        else:
          return 0
      return current.wordCount

    def countWordsStartingWith(self, prefix):
      current = self.root
      for letter in prefix:
        if current.contains(letter):
          current = current.get(letter)
        else:
          return 0
      return current.prefixCount

    def erase(self, word):
      current = self.root
      for letter in word:
        if current.contains(letter):
          current = current.getAndErase(letter)
      
      current.wordCount -= 1
      