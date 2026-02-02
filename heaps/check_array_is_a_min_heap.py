# Given an array of integers nums. Check whether the array represents a binary min-heap or not. Return true if it does, otherwise return false.
# A binary min-heap is a complete binary tree where the key at the root is the minimum among all keys present in a binary min-heap and the same property is recursively true for all nodes in a Binary Tree.

class Solution:
  def check(self,nums,index):    
    if index > len(nums):
      return True
    
    left_child = 2*index + 1
    right_child = 2*index + 2
    left,right = True,True

    if left_child < len(nums):
      if nums[left_child] < nums[index]:
        return False

      left = self.check(nums,left_child)

    if right_child < len(nums):
      if nums[right_child] < nums[index]:
        return False
      right = self.check(nums,right_child)
    
    return left and right

  def isHeap(self, nums):
    return self.check(nums,0)

  def isHeapInternalNodeSolution(self, nums):
      n = len(nums)  # Size of the array
      
      # Iterate on the non-leaf nodes from the back
      for i in range(n//2 - 1, -1, -1):
          leftChildInd = 2*i + 1
          rightChildInd = 2*i + 2
          
          # If left child has a smaller value than the parent
          if leftChildInd < n and nums[leftChildInd] < nums[i]:
              return False
              
          # If right child has a smaller value than parent
          if rightChildInd < n and nums[rightChildInd] < nums[i]:
              return False
      
      return True


if __name__ == "__main__":
  nums = [10, 20, 30, 21, 23]
  print(Solution().isHeap(nums))
