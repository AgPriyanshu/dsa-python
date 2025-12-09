# Compute the binary tree's vertical order traversal given its root.
# The left and right children of a node at location (row, col) will be at (row + 1, col - 1) and (row + 1, col + 1), respectively. The tree's root is located at (0, 0).
# The vertical order traversal of a binary tree is a list of top-to-bottom orderings for each column index starting from the leftmost column and ending on the rightmost column. There may be multiple nodes in the same row and same column. In such a case, sort these nodes by their values. Return the binary tree's vertical order traversal.
from collections import deque,defaultdict

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.data = val
        self.left = left
        self.right = right

class Solution:
    def verticalTraversal(self, root):
        """
        Perform vertical order traversal of a binary tree.

        :param root: TreeNode - The root of the binary tree.
        :return: List[List[int]] - A list of lists containing the vertical order traversal.
        """
   
        if not root:
            return []

        # Dictionary to store the nodes at each vertical distance and level.
        # nodes_map[x][y] will hold a list of nodes at vertical distance x and level y.
        nodes_map = defaultdict(lambda: defaultdict(list))

        # Queue for BFS traversal (stores node along with its x and y coordinates)
        queue = deque([(root, 0, 0)])  # (node, x, y)

        # Perform BFS to populate nodes_map with nodes at each (x, y) coordinate.
        while queue:
            node, x, y = queue.popleft()

            # Add the node's value to the map at the correct x and y
            nodes_map[x][y].append(node.data)

            # Add the left child with updated coordinates to the queue
            if node.left:
                queue.append((node.left, x - 1, y + 1))

            # Add the right child with updated coordinates to the queue
            if node.right:
                queue.append((node.right, x + 1, y + 1))

        # Prepare the result by sorting keys and compiling nodes
        result = []
        for x in sorted(nodes_map):
            column = []
            for y in sorted(nodes_map[x]):
                # Sort the nodes at the same position to maintain the order
                column.extend(sorted(nodes_map[x][y]))
            result.append(column)

        return result

if __name__ == "__main__":
  root1 = TreeNode(
      3,
      TreeNode(9),
      TreeNode(20,TreeNode(15),TreeNode(7)),
  )

  print(Solution().verticalTraversal(root1))