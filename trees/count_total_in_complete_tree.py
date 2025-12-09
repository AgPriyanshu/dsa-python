# Return the number of nodes in a binary tree given its root.
# Every level in a complete binary tree possibly with the exception of the final one is fully filled, and every node in the final level is as far to the left as it can be. At the last level h, it can have 1 to 2h nodes inclusive.


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.data = val
        self.left = left
        self.right = right

class Solution:
    # Function to count nodes
    # in a binary tree
    def count_nodes(self, root):
        # Base case: If the root
        # is NULL, there are no nodes
        if root is None:
            return 0
        
        # Find the left height and
        # right height of the tree
        lh = self.find_height_left(root)
        rh = self.find_height_right(root)
        
        # Check if the last level
        # is completely filled
        if lh == rh:
            # If so, use the formula for
            # total nodes in a perfect
            # binary tree i.e. 2^h - 1
            return (1 << lh) - 1
        
        # If the last level is not completely
        # filled, recursively count nodes in
        # left and right subtrees
        return 1 + self.count_nodes(root.left) + self.count_nodes(root.right)
    
    # Function to find the left height of a tree
    def find_height_left(self, node):
        height = 0
        # Traverse left child until
        # reaching the leftmost leaf
        while node:
            height += 1
            node = node.left
        return height
    
    # Function to find the right height of a tree
    def find_height_right(self, node):
        height = 0
        # Traverse right child until
        # reaching the rightmost leaf
        while node:
            height += 1
            node = node.right
        return height    

if __name__ == "__main__":
  root1 = TreeNode(
      1,
      TreeNode(2,TreeNode(6),TreeNode(5)),
      TreeNode(3,TreeNode(8,TreeNode(9)),TreeNode(4)),
  )

  print(Solution().count_nodes(root1))