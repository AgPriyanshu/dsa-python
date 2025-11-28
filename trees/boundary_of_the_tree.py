# Given a root of Binary Tree, perform the boundary traversal of the tree. 
# The boundary traversal is the process of visiting the boundary nodes of the binary tree in the anticlockwise direction, starting from the root.
# The boundary of a binary tree is the concatenation of the root, the left boundary, the leaves ordered from left-to-right, and the reverse order of the right boundary.
# The left boundary is the set of nodes defined by the following:
#     The root node's left child is in the left boundary. If the root does not have a left child, then the left boundary is empty.
#     If a node in the left boundary and has a left child, then the left child is in the left boundary.
#     If a node is in the left boundary, has no left child, but has a right child, then the right child is in the left boundary.
#     The leftmost leaf is not in the left boundary.
# The right boundary is similar to the left boundary, except it is the right side of the root's right subtree. Again, the leaf is not part of the right boundary, and the right boundary is empty if the root does not have a right child.


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.data = val
        self.left = left
        self.right = right

class Solution:
    def isLeaf(self,node):
      return node.left is None and node.right is None

    def addLeaves(self,root,ans):
      if root is None:
        return

      self.addLeaves(root.left,ans)
      self.addLeaves(root.right,ans)
      if self.isLeaf(root):
        ans.append(root.data)
 
    def addRightBoundary(self,root,ans):
      if root is None or self.isLeaf(root):
          return


      if root.right:
        self.addRightBoundary(root.right,ans)
      else:
        self.addRightBoundary(root.left,ans)

      ans.append(root.data)

    def addLeftBoundary(self,root,ans):
      if root is None or self.isLeaf(root):
          return

      ans.append(root.data)

      if root.left:
        self.addLeftBoundary(root.left,ans)
      else:
        self.addLeftBoundary(root.right,ans)
      

    def boundary(self, root):
      if not root:
        return []
      if self.isLeaf(root):
        return [root.data]
      ans = [root.data]
      self.addLeftBoundary(root.left,ans)
      self.addLeaves(root,ans)
      self.addRightBoundary(root.right,ans)
      return ans

if __name__ == "__main__":
  root1 = TreeNode(
      1,
      TreeNode(2,TreeNode(4),TreeNode(5,TreeNode(8),TreeNode(9))),
      TreeNode(3,TreeNode(6),TreeNode(7)),
  )

  print(Solution().boundary(root1))