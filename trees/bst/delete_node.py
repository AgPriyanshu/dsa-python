# Given the root node of a binary search tree (BST) and a value key. Return the root node of the BST after the deletion of the node with the given key value.
# Note: As there can be many correct answers, the compiler returns true if the answer is correct, otherwise false.

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.data = val
        self.left = left
        self.right = right


class Solution:
    def connect(self,root):
      if root.left is None:
        return root.right
      
      if root.right is None:
        return root.left

      left_subtree_rightmost = root.left
      while left_subtree_rightmost.right:
        left_subtree_rightmost = left_subtree_rightmost.right

      left_subtree_rightmost = root.right

      return root.left

    def deleteNode(self, root, key):
      if root is None:
        return root

      if root.data == key:
        return self.connect(root)

      current = root

      while current:
        if current.data > key:
          if current.left and current.left.data == key:
            current.left = self.connect(current.left)
          else:
            current = current.left
        elif current.data < key:
          if current.right and current.right.data == key:
            current.right = self.connect(current.right)
            break
          else:
            current = current.right

      return root



if __name__ == "__main__":
    # Create a sample binary search tree
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(8)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)

    sol = Solution()
    # Delete node with key 3 from the tree
    root = sol.deleteNode(root, 3)