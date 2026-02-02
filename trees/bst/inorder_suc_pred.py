# Given the root node of a binary search tree (BST) and an integer key. Return the Inorder predecessor and successor of the given key from the provided BST.
# Note: key will always present in given BST.
# If predecessor or successor is missing then return -1.

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.data = val
        self.left = left
        self.right = right

class Solution:
    def succPredBST(self, root: TreeNode, key: int):
        predecessor = None
        successor = None
        curr = root

        while curr:
            if key > curr.data:
                # Current node could be predecessor
                predecessor = curr
                curr = curr.right
            elif key < curr.data:
                # Current node could be successor
                successor = curr
                curr = curr.left
            else:
                # Found the node
                # Check left subtree for predecessor
                if curr.left:
                    temp = curr.left
                    while temp.right:
                        temp = temp.right
                    predecessor = temp

                # Check right subtree for successor
                if curr.right:
                    temp = curr.right
                    while temp.left:
                        temp = temp.left
                    successor = temp
                break

        predVal = predecessor.data if predecessor else -1
        succVal = successor.data if successor else -1

        return [predVal, succVal]

if __name__ == "__main__":
  # Creating a sample BST
  root = TreeNode(8)
  root.left = TreeNode(4)
  root.right = TreeNode(12)
  root.left.left = TreeNode(2)
  root.left.right = TreeNode(6)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(14)
  key = 10
  
  sol = Solution()

  result = sol.succPredBST(root, key)
  print(result)
