
# Given a root of Binary Tree, where the nodes have integer values. Return the size of the largest subtree of the binary tree which is also a BST.
# A binary search tree (BST) is a binary tree data structure which has the following properties.
#     The left subtree of a node contains only nodes with data less than the node’s data.
#     The right subtree of a node contains only nodes with data greater than the node’s data.
#     Both the left and right subtrees must also be binary search trees.

class Solution:
    # Helper class to store information about a subtree.
    class NodeValue:
        def __init__(self, minNode, maxNode, maxSize):
            self.minNode = minNode
            self.maxNode = maxNode
            self.maxSize = maxSize

    # Helper function to recursively find the largest BST subtree.
    def largestBSTSubtreeHelper(self, node):
        # Base case: if the node is null, return a default NodeValue.
        if not node:
            return self.NodeValue(float('inf'), float('-inf'), 0)

        # Recursively get values from the left and right subtrees.
        left = self.largestBSTSubtreeHelper(node.left)
        right = self.largestBSTSubtreeHelper(node.right)

        # Check if the current node is a valid BST node.
        if left.maxNode < node.data < right.minNode:
            # Current subtree is a valid BST.
            return self.NodeValue(
                min(node.data, left.minNode),
                max(node.data, right.maxNode),
                left.maxSize + right.maxSize + 1
            )

        # Current subtree is not a valid BST.
        return self.NodeValue(float('-inf'), float('inf'), max(left.maxSize, right.maxSize))

    def largestBST(self, root):
        # Initialize the recursive process and return the size of the largest BST subtree.
        return self.largestBSTSubtreeHelper(root).maxSize