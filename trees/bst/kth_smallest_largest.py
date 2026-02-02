# Given the root node of a binary search tree (BST) and an integer k.
# Return the kth smallest and largest value (1-indexed) of all values of the nodes in the tree.
# Return the 1st integer as kth smallest and 2nd integer as kth largest in the returned array.

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.data = val
        self.left = left
        self.right = right

class Solution:
  def inorder(self,root,arr):
    if root is None:
      return None
    
    self.inorder(root.left,arr)
    arr.append(root.data)
    self.inorder(root.right,arr)

  def kLargesSmall(self, root, k):
    arr = []
    self.inorder(root,arr)
    return [arr[k-1],arr[-k]]



if __name__ == "__main__":
  # Creating a sample BST
  root = TreeNode(8)
  root.left = TreeNode(4)
  root.right = TreeNode(12)
  root.left.left = TreeNode(2)
  root.left.right = TreeNode(6)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(14)

  sol = Solution()
  key =  1

  # Find and print floor and ceil values
  result = sol.kLargesSmall(root, key)
  print(result)
  # print(f"Floor: {result[0]}, Ceil: {result[1]}")