# Given a target node data and a root of binary tree. If the target is set on fire, determine the shortest amount of time needed to burn the entire binary tree.
# It is known that in 1 second all nodes connected to a given node get burned. That is its left child, right child, and parent.

from collections import defaultdict, deque

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.data = val
        self.left = left
        self.right = right

class Solution:
  def timeToBurnTree(self, root, target):       
    parent_map = defaultdict()
    queue = deque()
    queue.append(root)

    while queue:
      for i in range(len(queue)):
        node = queue.popleft()
        if node.left:
          parent_map[node.left] = node
          queue.append(node.left)

        if node.right:
          parent_map[node.right] = node
          queue.append(node.right)

    queue = deque()
    queue.append(target)
    visited = defaultdict(bool)
    
    distance = 0
 
    while queue:
      for i in range(len(queue)):
        node = queue.popleft()
        visited[node] = True

        if parent := parent_map.get(node):            
          if not visited[parent]:
            queue.append(parent)
            visited[parent] = True

        if node.left and not visited[node.left]:
          queue.append(node.left)
          visited[node.left] = True

        if node.right and not visited[node.right]:
          queue.append(node.right)
          visited[node.right] = True
      distance += 1

    return distance



if __name__ == "__main__":
  target = TreeNode(5,TreeNode(6),TreeNode(2,TreeNode(7),TreeNode(4)))
  root1 = TreeNode(
      3,
      target,
      TreeNode(1,TreeNode(0),TreeNode(8)),
  )

  print(Solution().timeToBurnTree(root1,target))
