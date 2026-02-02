# Given a min-heap in array representation named nums, convert it into a max-heap and return the resulting array.
# A min-heap is a complete binary tree where the key at the root is the minimum among all keys present in a binary min-heap and the same property is recursively true for all nodes in the Binary Tree.
# A max-heap is a complete binary tree where the key at the root is the maximum among all keys present in a binary max-heap and the same property is recursively true for all nodes in the Binary Tree.
# Since there can be multiple answers, the compiler will return true if it's correct, else false.

class Solution:
  def buildMax(self,nums,index):
    left_child = 2*index + 1
    right_child = 2*index + 2
    max_index = index

    if left_child < len(nums) and nums[left_child] > nums[max_index]:
      max_index = left_child
    if right_child < len(nums) and nums[right_child] > nums[max_index]:
      max_index = right_child

    if max_index != index:
      nums[index],nums[max_index] = nums[max_index],nums[index]      
      self.buildMax(nums,max_index)
    

  def minToMaxHeap(self, nums):
    n = len(nums)
    for i in range(n//2 - 1,-1,-1):
      self.buildMax(nums,i)
    return nums

if __name__ == "__main__":
  nums = [-5, -4, -3, -2, -1]
  print(Solution().minToMaxHeap(nums))