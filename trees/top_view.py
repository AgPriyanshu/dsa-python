# Given the root of a binary tree, return the top view of the binary tree.
# Top view of a binary tree is the set of nodes visible when the tree is viewed from the top. Return nodes from the leftmost node to the rightmost node. Also if 2 nodes are outside the shadow of the tree and are at the same position then consider the left ones only(i.e. leftmost). 

from collections import deque,defaultdict

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.data = val
        self.left = left
        self.right = right

class Solution:
    def topView(self, root):   
      if root is None:
        return []
      q = deque([(root,0)])

      vertical_map = defaultdict(int)
      ans = []
      while q:
        for i in range(len(q)):
          node,x = q.popleft()

          if not vertical_map.get(x):
            vertical_map[x] = node.data
          
          if node.left:
            q.append((node.left,x-1))

          if node.right:
            q.append((node.right,x+1))

      for x in sorted(vertical_map):
        ans.append(vertical_map[x])
      return ans

if __name__ == "__main__":
  root1 = TreeNode(
      1,
      TreeNode(2,TreeNode(4),TreeNode(5)),
      TreeNode(3,TreeNode(6),TreeNode(7)),
  )

  print(Solution().topView(root1))