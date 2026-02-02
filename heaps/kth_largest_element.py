# Given an array nums, return the kth largest element in the array.
import random

class Solution:
    # Function to get the Kth largest element
    def kthLargestElement(self, nums, k):
        # Return -1, if the Kth largest element does not exist
        if k > len(nums):
            return -1
        
        # Pointers to mark the part of working array 
        left, right = 0, len(nums) - 1
        
        # Until the Kth largest element is found
        while True:
            # Get the pivot index
            pivotIndex = self.randomIndex(left, right)
            
            # Update the pivotIndex
            pivotIndex = self.partitionAndReturnIndex(nums, pivotIndex, left, right)
            
            # If Kth largest element is found, return
            if pivotIndex == k - 1:
                return nums[pivotIndex]
            
            # Else adjust the end pointers in array 
            elif pivotIndex > k - 1:
                right = pivotIndex - 1
            else:
                left = pivotIndex + 1
                
    # Function to get a random index 
    def randomIndex(self, left, right):
        # Length of the array 
        length = right - left + 1
        
        # Return a random index from the array 
        return random.randint(left, right)

    # Function to perform the partition and return the updated index of pivot
    def partitionAndReturnIndex(self, nums, pivotIndex, left, right):
        pivot = nums[pivotIndex]  # Get the pivot element
        
        # Swap the pivot with the left element
        nums[left], nums[pivotIndex] = nums[pivotIndex], nums[left]
        
        ind = left + 1  # Index to mark the start of right portion
        
        # Traverse on the array 
        for i in range(left + 1, right + 1):
            # If the current element is greater than the pivot
            if nums[i] > pivot:
                # Place the current element in the left portion
                nums[ind], nums[i] = nums[i], nums[ind]
                
                # Move the right portion index
                ind += 1
        
        # Place the pivot at the correct index
        nums[left], nums[ind - 1] = nums[ind - 1], nums[left]
        
        return ind - 1  # Return the index of pivot now