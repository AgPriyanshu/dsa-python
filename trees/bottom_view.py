# Given root of binary tree, return the bottom view of the binary tree.
# The bottom view of a binary tree is the set of nodes visible when the tree is viewed from the bottom. Return nodes from the leftmost node to the rightmost node. Also if 2 nodes are outside the shadow of the tree and are at the same position then consider the node that appears later in level traversal.

from collections import deque,defaultdict

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.data = val
        self.left = left
        self.right = right

class Solution:
    def rightView(self, root):   
      if root is None:
        return []
      q = deque([(root,0)])

      vertical_map = defaultdict(int)
      ans = []
      while q:
        for i in range(len(q)):
          node,y = q.popleft()

          vertical_map[y] = node.data          
          if node.left:
            q.append((node.left,y+1))

          if node.right:
            q.append((node.right,y+1))

      for y in sorted(vertical_map):
        ans.append(vertical_map[y])
      return ans


    # def rightView(self, root):   
    #   if root is None:
    #     return []
    #   q = deque([(root,0,0)])

    #   vertical_map = defaultdict(lambda: defaultdict(list))
    #   ans = []
    #   while q:
    #     for i in range(len(q)):
    #       node,x,y = q.popleft()

    #       if  vertical_map.get(x,{}).get(y) is None and x >= 0:
    #         vertical_map[x][y] = node.data
          
    #       if node.left:
    #         q.append((node.left,x-1,y+1))

    #       if node.right:
    #         q.append((node.right,x+1,y+1))

    #   for x in sorted(vertical_map):
    #     for y in vertical_map[x]:
    #       ans.append(vertical_map[x][y])
    #   return ans

if __name__ == "__main__":
  root1 = TreeNode(
      1,
      TreeNode(2,TreeNode(6),TreeNode(5)),
      TreeNode(3,TreeNode(8,TreeNode(9)),TreeNode(4)),
  )

  print(Solution().rightView(root1))