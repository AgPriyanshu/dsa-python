# Given an array nums representing a min-heap and two integers ind and val, set the value at index ind (0-based) to val and perform the heapify algorithm such that the resulting array follows the min-heap property.

# Modify the original array in-place, no need to return anything.
class Solution:
    # Function to recursively heapify the array downwards
    def heapifyDown(self, arr, ind):
        n = len(arr) # Size of the array

        # Index of smallest element
        smallest_Ind = ind

        # Indices of the left and right children
        leftChild_Ind = 2*ind + 1
        rightChild_Ind = 2*ind + 2
        
        # If the left child holds smaller value, update the smallest index
        if leftChild_Ind < n and arr[leftChild_Ind] < arr[smallest_Ind]:
            smallest_Ind = leftChild_Ind

        # If the right child holds smaller value, update the smallest index
        if rightChild_Ind < n and arr[rightChild_Ind] < arr[smallest_Ind]:
            smallest_Ind = rightChild_Ind

        # If the smallest element index is updated
        if smallest_Ind != ind:
            # Swap the smallest element with the current index
            arr[smallest_Ind], arr[ind] = arr[ind], arr[smallest_Ind]

            # Recursively heapify the lower subtree
            self.heapifyDown(arr, smallest_Ind)

        return

    # Function to recursively heapify the array upwards
    def heapifyUp(self, arr, ind):
        parent_Ind = (ind - 1)//2

        # If current index holds smaller value than the parent
        if ind > 0 and arr[ind] < arr[parent_Ind]:
            # Swap the values at the two indices
            arr[ind], arr[parent_Ind] = arr[parent_Ind], arr[ind]

            # Recursively heapify the upper nodes
            self.heapifyUp(arr, parent_Ind)

        return

    # Function to implement the heapify algorithm for a min-heap
    def heapify(self, nums, ind, val):
        # If the current value is replaced with a smaller value
        if nums[ind] > val:
            nums[ind] = val
            self.heapifyUp(nums, ind)
        # Else if the current value is replaced with a larger value
        else:
            nums[ind] = val
            self.heapifyDown(nums, ind)

        return

# Driver code
def main():
    nums = [1, 4, 5, 5, 7, 6]
    ind = 5
    val = 2

    # Input array
    print("Input array:", end=" ")
    for it in nums:
        print(it, end=" ")

    # Creating an object of the Solution class
    sol = Solution()

    # Function call to heapify the array
    sol.heapify(nums, ind, val)

    # Output array
    print("\nModified array after heapifying:", end=" ")
    for it in nums:
        print(it, end=" ")

if __name__ == "__main__":
    main()
