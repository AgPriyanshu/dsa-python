# Given the root of a binary tree. Return all the root-to-leaf paths in the binary tree.
# A leaf node of a binary tree is the node which does not have a left and right child.

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.data = val
        self.left = left
        self.right = right

class Solution:
  def dfs(self,root,path,ans):
      if root is None:
        return

      path2 = [*path,root.data]
      
      if not root.left and not root.right:
        ans.append([*path2])
        return

      self.dfs(root.left,path2,ans)
      self.dfs(root.right,path2,ans)

      return 

  def allRootToLeaf(self, root):
    ans = []
    path = []
    self.dfs(root,path,ans)
    return ans

if __name__ == "__main__":
  root1 = TreeNode(
      1,
      TreeNode(2,TreeNode(4),TreeNode(5)),
      TreeNode(3,TreeNode(8)),
  )

  print(Solution().allRootToLeaf(root1))
