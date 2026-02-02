# Given an array of integers preorder, which represents the preorder traversal of a BST (i.e., binary search tree), construct the tree and return its root.

# It is guaranteed that it is always possible to find a binary search tree with the given requirements for the given test cases.

# Note : As there can be many possible correct answers, the compiler outputs true if the solution is correct, else false.

# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.data = val
         self.left = left
         self.right = right

class Solution:
  def create(self,preorder,index,bound):
    if index[0] == len(preorder) or preorder[index[0]] > bound:
      return None

    root = TreeNode(preorder[index[0]])
    index[0] += 1

    root.left = self.create(preorder,index,root.data)
    root.right = self.create(preorder,index,bound)

    return root

  def bstFromPreorder(self, preorder):
    return self.create(preorder,[0],float('inf'))


# Example usage
if __name__ == "__main__":
    solution = Solution()
    preorder = [8, 5, 1, 7, 10, 12]
    bst = solution.bstFromPreorder(preorder)
    # Add code to print or use the bst as needed
