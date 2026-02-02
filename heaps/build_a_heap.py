# Given an array nums representing a min-heap and two integers ind and val, set the value at index ind (0-based) to val and perform the heapify algorithm such that the resulting array follows the min-heap property.

# Modify the original array in-place, no need to return anything.
class Solution:
    def heapifyDown(self, arr, ind):
        n = len(arr) # Size of the array

        smallest_Ind = ind

        leftChild_Ind = 2*ind + 1
        rightChild_Ind = 2*ind + 2
        
        if leftChild_Ind < n and arr[leftChild_Ind] < arr[smallest_Ind]:
            smallest_Ind = leftChild_Ind

        if rightChild_Ind < n and arr[rightChild_Ind] < arr[smallest_Ind]:
            smallest_Ind = rightChild_Ind

        if smallest_Ind != ind:
            arr[smallest_Ind], arr[ind] = arr[ind], arr[smallest_Ind]
            self.heapifyDown(arr, smallest_Ind)

        return


    def buildMinHeap(self, nums):
        n = len(nums) 
        for i in range((n//2)-1,-1,-1):
            self.heapifyDown(nums, i)
        return

# Driver code
def main():
    nums = [6, 5, 2, 7, 1, 7]

    # Input array
    print("Input array:", end=" ")
    for it in nums:
        print(it, end=" ")

    # Creating an object of the Solution class
    sol = Solution()

    # Function call to heapify the array
    sol.buildMinHeap(nums)

    # Output array
    print("\nModified array after heapifying:", end=" ")
    for it in nums:
        print(it, end=" ")

if __name__ == "__main__":
    main()
