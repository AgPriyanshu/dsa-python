# Given the root node of a binary tree. Return true if the given binary tree is a binary search tree(BST) else false.


# A valid BST is defined as follows:


#     The left subtree of a node contains only nodes with key strictly less than the node's key.


#     The right subtree of a node contains only nodes with key strictly greater than the node's key.


#     Both the left and right subtrees must also be binary search trees.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.data = val
        self.left = left
        self.right = right

class Solution:
  def inorder(self,root,range):
    if root is None:
      return True

    isValid = False
    if root.data < range[1] and root.data > range[0]:
      isValid = True

    left = self.inorder(root.left,[range[0],root.data])    
    right = self.inorder(root.right,[root.data,range[1]])

    return isValid and left and right

  def isBST(self, root):
    range = [float('-inf'),float('inf')]
    return self.inorder(root,range)



if __name__ == "__main__":
  # Creating a sample BST
  root = TreeNode(8)
  root.left = TreeNode(4)
  root.right = TreeNode(1)
  root.left.left = TreeNode(2)
  root.left.right = TreeNode(6)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(14)

  sol = Solution()

  result = sol.isBST(root)
  print(result)
