# Given a root of binary tree, find the lowest common ancestor (LCA) of two given nodes (p, q) in the tree.
# The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).

from collections import deque
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.data = val
        self.left = left
        self.right = right

class Solution:
    def dfs(self,root,p,q):
      if root is None or root == p or root == q :
        return root

      left = self.dfs(root.left,p,q)
      right = self.dfs(root.right,p,q)

      if left == None:
        return right
      if right == None:
        return left
      return root
        

    def lowestCommonAncestor(self, root, p, q):
      return self.dfs(root,p,q)

if __name__ == "__main__":
  root1 = TreeNode(
      3,
      TreeNode(5,TreeNode(6),TreeNode(2,TreeNode(7),TreeNode(4))),
      TreeNode(1,TreeNode(0),TreeNode(8)),
  )

  print(Solution().lowestCommonAncestor(root1,5,1))
