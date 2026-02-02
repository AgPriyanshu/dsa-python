# Given the root node of a binary search tree (BST) and two node values p,q.
# Return the lowest common ancestors(LCA) of the two nodes in BST.

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.data = val
        self.left = left
        self.right = right

class Solution:
    def lca(self, root, p, q):
      if root is None:
        return None
      current = root 
      ans = None

      while current:
        if current.data > p and current.data > q:
          current = current.left
        elif current.data < p and current.data < q:
          current = current.right
        elif (current.data > p and current.data < q) or (current.data < p and current.data > q):
          ans = current
          break
        else:
          ans = current
          break
      
      return ans

if __name__ == "__main__":
  # Creating a sample BST
  root = TreeNode(8)
  root.left = TreeNode(4)
  root.right = TreeNode(12)
  root.left.left = TreeNode(2)
  root.left.right = TreeNode(6)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(14)
  p = 6
  q = 14
  
  sol = Solution()

  result = sol.lca(root, p,q)
  print(result.data)
