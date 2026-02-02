# Given an array of integers nums, sort the array in non-decreasing order using the heap sort algorithm. Sort the given array itself, there is no need to return anything.


# A sorted array in non-decreasing order is one in which each element is either greater than or equal to all the elements to its left in the array.

class Solution:
  def heapifyMaxDown(self,nums,index,last):
    left = 2*index + 1
    right = 2*index + 2
    smallest_index = index

    if left <= last and nums[left] > nums[smallest_index]:
      smallest_index = left

    if right <= last and nums[right] > nums[smallest_index]:
      smallest_index = right
    
    if smallest_index != index:
      nums[smallest_index], nums[index] = nums[index], nums[smallest_index]
      self.heapifyMaxDown(nums,smallest_index,last)

  def heapifyMinDown(self,nums,index,last):
    left = 2*index + 1
    right = 2*index + 2
    smallest_index = index

    if left <= last and nums[left] < nums[smallest_index]:
      smallest_index = left

    if right <= last and nums[right] < nums[smallest_index]:
      smallest_index = right
    
    if smallest_index != index:
      nums[smallest_index], nums[index] = nums[index], nums[smallest_index]
      self.heapifyMinDown(nums,smallest_index,last)

  def buildMinHeap(self, nums):
          n = len(nums) 
          for i in range((n//2)-1,-1,-1):
              self.heapifyMinDown(nums, i,n-1)
          return

  def buildMaxHeap(self, nums):
          n = len(nums) 
          for i in range((n//2)-1,-1,-1):
              self.heapifyMaxDown(nums, i,n-1)
          return

  def heapSortReverse(self, nums):
    last = len(nums) - 1
    self.buildMinHeap(nums)

    while last != 0:
      nums[0],nums[last] = nums[last],nums[0]
      last -= 1
      self.heapifyMinDown(nums,0,last)

    return nums

  def heapSort(self, nums):
    last = len(nums) - 1
    self.buildMaxHeap(nums)

    while last != 0:
      nums[0],nums[last] = nums[last],nums[0]
      last -= 1
      self.heapifyMaxDown(nums,0,last)

    return nums

if __name__ == "__main__":
  nums = [7, 4, 1, 5, 3]
  print(Solution().heapSortReverse(nums))