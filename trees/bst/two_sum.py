# Given the root of a binary search tree and an integer k.Return true if there exist two elements in the BST such that their sum is equal to k otherwise false.

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.data = val
        self.left = left
        self.right = right
    
    def __repr__(self):
      return f'Node({self.data})'

class Solution:
    def createIterator(self,root):
      self.next_stack = []
      self.before_stack = []

      next_itr = root
      prev_itr = root

      while next_itr:
        self.next_stack.append(next_itr)
        next_itr = next_itr.left
      
      while prev_itr:
        self.before_stack.append(prev_itr)
        prev_itr = prev_itr.right

    def twoSumBST(self, root, k):
      self.createIterator(root)
      nextVal = self.next()
      beforeVal = self.before()

      while self.hasNext() and self.hasBefore() and nextVal <= beforeVal:
        sumVal = nextVal + beforeVal  
        
        if sumVal == k:
          return True
        elif sumVal > k:
          beforeVal = self.before()
        else:
          nextVal = self.next()          

      return False

    def hasNext(self):
      return True if len(self.next_stack) > 0 else False 

    def hasBefore(self):
      return True if len(self.before_stack) > 0 else False 

    def next(self):
      node = self.next_stack.pop()
      val = node.data
      if node.right:
        node = node.right
        while node:
          self.next_stack.append(node)
          node = node.left

      return val
    
    def before(self):
      node = self.before_stack.pop()
      val = node.data
      if node.left:
        node = node.left
        while node:
          self.before_stack.append(node)
          node = node.right

      return val
    
    
def main():
    # Create the tree
    root = TreeNode(-5)
    root.right = TreeNode(-4)
    root.right.right = TreeNode(-3)
    root.right.right.right = TreeNode(-2)

    # Create solution instance
    solution = Solution()
    k = -6
    
    # Check if there exist two elements in the BST such that their sum is equal to k
    result = solution.twoSumBST(root, k)
    print("True" if result else "False")

if __name__ == "__main__":
    main()