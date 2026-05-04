# Given an integer array nums of size N, sorted in ascending order with distinct values, and then rotated an unknown number of times (between 1 and N), find the minimum element in the array.
class Solution:
    def findMin(self, arr):
        # Initialize low and high indices
        low, high = 0, len(arr) - 1
        
        # Initialize ans to maximum integer value
        ans = float('inf')
        while low <= high:
            mid = (low + high) // 2
            
            # Check if left part is sorted
            if arr[low] <= arr[mid]:
                """ Update ans with minimum 
                    of ans and arr[low] """
                ans = min(ans, arr[low])
                
                # Move to the right part
                low = mid + 1
            else:
                """ Update ans with minimum 
                    of ans and arr[mid] """
                ans = min(ans, arr[mid])
                
                # Move to the left part
                high = mid - 1
        
        # Return the minimum element found
        return ans

if __name__ == "__main__":
    arr = [4, 5, 6, 7, 0, 1, 2, 3]
    
    #Create an instance of the Solution class
    sol = Solution()
    
    ans = sol.findMin(arr)
    
    print("The minimum element is:", ans)
