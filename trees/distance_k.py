# Given the root of a binary tree, the value of a target node target, and an integer k. Return an array of the values of all nodes that have a distance k from the target node.
# The answer can be returned in any order (N represents null).
# Note: Although input shows target as a value, internally it refers to the TreeNode with that value.
from collections import defaultdict, deque

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.data = val
        self.left = left
        self.right = right

class Solution:
  
  def distanceK(self, root, target, k):       
    parent_map = defaultdict(int)
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
    ans = []
    while queue:
      if distance == k:
        for i in range(len(queue)):
         ans.append(queue.popleft().data)
        break
      else:
        for i in range(len(queue)):
          node = queue.popleft()
          visited[node] = True

          if parent := parent_map[node]:            
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

    return ans



if __name__ == "__main__":
  target = TreeNode(5,TreeNode(6),TreeNode(2,TreeNode(7),TreeNode(4)))
  k = 2
  root1 = TreeNode(
      3,
      target,
      TreeNode(1,TreeNode(0),TreeNode(8)),
  )

  print(Solution().distanceK(root1,target,k))
