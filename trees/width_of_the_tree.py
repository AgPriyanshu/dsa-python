# Given the root of a binary tree, return the maximum width of the given tree.
# The maximum width of a tree is the maximum width among all levels. The width of a level is determined by measuring the distance between its end nodes, which are the leftmost and rightmost non-null nodes. The length calculation additionally takes into account the null nodes that would be present between the end nodes if a full binary tree were to stretch down to that level.
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.data = val
        self.left = left
        self.right = right

class Solution:
    # Function widthOfBinaryTree to find the 
    # maximum width of the Binary Tree
    def widthOfBinaryTree(self, root):
        # If the root is null,
        # the width is zero
        if not root:
            return 0

        # Initialize a variable 'ans'
        # to store the maximum width
        ans = 0

        # Create a queue to perform level-order
        # traversal, where each element is a pair
        # of TreeNode* and its position in the level
        q = deque([(root, 0)])

        # Perform level-order traversal
        while q:
            # Get the number of
            # nodes at the current level
            size = len(q)
            # Get the position of the front
            # node in the current level
            mmin = q[0][1]

            # Store the first and last positions 
            # of nodes in the current level
            first = last = 0

            # Process each node
            # in the current level
            for i in range(size):
                # Calculate current position relative
                # to the minimum position in the level
                cur_id = q[0][1] - mmin
                # Get the current node
                node = q[0][0]
                # Pop the front node from the queue
                q.popleft()

                # If this is the first node in the level, 
                # update the 'first' variable
                if i == 0:
                    first = cur_id

                # If this is the last node in the level,
                # update the 'last' variable
                if i == size - 1:
                    last = cur_id

                # Enqueue the left child of the 
                # current node with its position
                if node.left:
                    q.append((node.left, cur_id * 2 + 1))

                # Enqueue the right child of the
                # current node with its position
                if node.right:
                    q.append((node.right, cur_id * 2 + 2))

            # Update the maximum width by calculating
            # the difference between the first and last
            # positions, and adding 1
            ans = max(ans, last - first + 1)

        # Return the maximum
        # width of the binary tree
        return ans