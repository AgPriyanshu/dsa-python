# Given a root of binary search tree and a key(node) value, find the floor and ceil value for that particular key value.


#     Floor Value Node: Node with the greatest data lesser than or equal to the key value. 


#     Ceil Value Node: Node with the smallest data larger than or equal to the key value.


# If a particular floor or ceil value is not present then output -1.

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.data = val
        self.left = left
        self.right = right

class Solution:
  def search(self,root,key,floor,ceil):
    if not root:
      return None

    if root.data == key:
      floor[0] = root.data
      ceil[0] = root.data

    if root.data > key:
      ceil[0] = root.data
      return self.search(root.left,key,floor,ceil)

    if root.data < key:
      floor[0] = root.data
      return self.search(root.right,key,floor,ceil)

  def floorCeilOfBST(self, root, key):
    floor = [-1]
    ceil = [-1]
    self.search(root,key,floor,ceil)
    return [floor[0],ceil[0]]

if __name__ == "__main__":
  # Creating a sample BST
  root = TreeNode(8)
  root.left = TreeNode(4)
  root.right = TreeNode(12)
  root.left.left = TreeNode(2)
  root.left.right = TreeNode(6)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(14)

  sol = Solution()
  key = 11  # Key to find floor and ceil for

  # Find and print floor and ceil values
  result = sol.floorCeilOfBST(root, key)
  print(result)
  # print(f"Floor: {result[0]}, Ceil: {result[1]}")