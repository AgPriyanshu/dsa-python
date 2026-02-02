# Given the root of a binary search tree (BST), where the values of exactly two nodes of the tree were swapped by mistake.
# Recover the tree without changing its structure.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.data = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        # Initialize the pointers
        self.first = None
        self.first_next = None
        self.last = None
        self.previous_node = TreeNode(float('-inf'))  # Previous node initialized to negative infinity

    def inorderTraversal(self, root: TreeNode):
        if not root:
            return
        
        # Traverse the left subtree
        self.inorderTraversal(root.left)

        # Identify misplaced nodes
        if self.previous_node and root.data < self.previous_node.data:
            if not self.first:
                self.first = self.previous_node  # First out-of-order node
                self.first_next = root  # Node next to the first out-of-order node
            else:
                self.last = root  # Second out-of-order node

        # Update previous node to current node
        self.previous_node = root

        # Traverse the right subtree
        self.inorderTraversal(root.right)

    def recoverTree(self, root: TreeNode):
        # Reset the pointers
        self.first = self.first_next = self.last = None
        self.previous_node = TreeNode(float('-inf'))
        
        # Perform the inorder traversal to find the two nodes
        self.inorderTraversal(root)

        # Correct the BST by swapping the misplaced nodes
        if self.first and self.last:
            self.first.data, self.last.data = self.last.data, self.first.data  # Non-adjacent nodes
        elif self.first and self.first_next:
            self.first.data, self.first_next.data = self.first_next.data, self.first.data  # Adjacent nodes