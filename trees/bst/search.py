# Given the root of a binary search tree (BST) and an integer val.


# Find the node in the BST that the node's value equals val and return the subtree rooted with that node. If such a node does not exist, return null.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.data = val
#         self.left = left
#         self.right = right

class Solution:
  def searchBST(self, root, val):
    pass

if __name__ == "__main__":
  root = [4, 2, 7, 1, 3]
  val = 2
  print(Solution().searchBST(root,val))