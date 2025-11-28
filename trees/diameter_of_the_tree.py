# Given the root of a binary tree, return the length of the diameter of the tree.


# The diameter of a binary tree is the length of the longest path between any two nodes in the tree. It may or may not pass through the root.


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import sys
class Solution:
    def dfs(self,root,maxi):
        if root is None:
            return 0
        
        left = max(0,self.dfs(root.left,maxi))
        right = max(0,self.dfs(root.right,maxi))
        
        maxi[0] = max(maxi[0],left+right+root.val)

        return root.val + max(left,right)
 
    def maxPathSum(self, root):
        #your code goes here
        maxi = [-sys.maxsize]
        self.dfs(root,maxi)
        return maxi[0]
