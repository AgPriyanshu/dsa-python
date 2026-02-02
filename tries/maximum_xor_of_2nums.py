# Given an integer array nums, return the maximum result of nums[i] XOR nums[j], where 0 <= i <= j < n.

class Node:
    def __init__(self):
        self.links = [None, None]

class BitsTrie:
    def __init__(self):
        self.root = Node()

    def insert(self, num):
        node = self.root
        for i in range(31, -1, -1):
            bit = (num >> i) & 1
            if not node.links[bit]:
                node.links[bit] = Node()
            node = node.links[bit]

    def get_max_xor(self, num):
        node = self.root
        ans = 0
        for i in range(31, -1, -1):
            bit = (num >> i) & 1
            toggled = 1 - bit
            if node.links[toggled]:
                ans |= (1 << i)
                node = node.links[toggled]
            else:
                node = node.links[bit]
        return ans

class Solution:
  def findMaximumXOR(self, nums):
    trie = BitsTrie()
    for num in nums:
      trie.insert(num)
    
    max_val = 0
    for num in nums:
      max_val = max(trie.get_max_xor(num),max_val)

    return max_val

if __name__ == "__main__":
  nums = [26, 49, 30, 15, 69]
  print(Solution().findMaximumXOR(nums))