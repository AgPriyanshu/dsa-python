# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.data = val
        self.left = left
        self.right = right

class Solution:
  def solve(self, node, val):
    # If the current node is None, create a new TreeNode with the given value
    if node is None:
        return TreeNode(val)
    
    # Traverse the tree to find the correct insertion point
    if val < node.data:
        # Move to the left subtree
        node.left = self.solve(node.left, val)
    elif val > node.data:
        # Move to the right subtree
        node.right = self.solve(node.right, val)
    
    # Return the (potentially modified) node
    return node
    
  def insertIntoBST(self, root, val):
    current = root
    prev = None
    while current:
      if current is None:
        return root
      if current.data > val:
        prev = current
        current = current.left
      elif current.data < val:
        prev = current
        current = current.right 
    
    if prev.data > val:
      prev.left = TreeNode(val)
    else:
      prev.right = TreeNode(val)
    return root

  

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
  key = 11  # Key to find floor and ceil for

  # Find and print floor and ceil values
  result = sol.floorCeilOfBST(root, key)
  print(result)
  # print(f"Floor: {result[0]}, Ceil: {result[1]}")