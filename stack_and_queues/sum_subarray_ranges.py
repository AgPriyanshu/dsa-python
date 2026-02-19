
# Given an integer array nums, determine the range of a subarray, defined as the differen`ce between the largest and smallest elements within the subarray. Calculate and return the sum of all subarray ranges of nums.

# A subarray is defined as a contiguous, non-empty sequence of elements within the array.`

class Solution:
    def nextGreaterElementIndex(self,arr):
        st = []
        n = len(arr)
        ans = [-1]*n

        for i in range(len(arr)-1,-1,-1):
            while st and arr[st[-1]] <= arr[i]:
                st.pop()
            
            ans[i] = st[-1] if st else n
            st.append(i)
        return ans


    def previousGreaterElementIndex(self,arr):
        st = []
        n = len(arr)
        ans = [-1]*n
        for i in range(n):
            while st and arr[st[-1]] < arr[i]:
                st.pop()
            
            ans[i] = st[-1] if st else -1
            st.append(i)
        return ans

        
    def sumSubarrayMax(self, arr):
        ngei = self.nextGreaterElementIndex(arr)
        pgei = self.previousGreaterElementIndex(arr)
        sum = 0
        mod = int(1e9 + 7)  # Mod value
        for i in range(len(arr)):
            left = i - pgei[i]
            right = ngei[i] - i
            freq = right*left
            sum  += (freq*arr[i])% mod
        return sum

    def findNSE(self, arr):
        
        # Size of array
        n = len(arr)
        
        # To store the answer
        ans = [0] * n
        
        # Stack 
        st = []
        
        # Start traversing from the back
        for i in range(n - 1, -1, -1):
            
            # Get the current element
            currEle = arr[i]
            
            # Pop the elements in the stack until 
            # the stack is not empty and the top 
            # element is not the smaller element
            while st and arr[st[-1]] >= arr[i]:
                st.pop()
            
            # Update the answer
            ans[i] = st[-1] if st else n
            
            # Push the index of current 
            # element in the stack
            st.append(i)
        
        # Return the answer
        return ans
    
    def findPSEE(self, arr):
        
        # Size of array
        n = len(arr)
        
        # To store the answer
        ans = [0] * n
        
        # Stack 
        st = []
        
        # Traverse on the array
        for i in range(n):
            
            # Get the current element
            currEle = arr[i]
            
            # Pop the elements in the stack until 
            # the stack is not empty and the top 
            # elements are greater than the current element
            while st and arr[st[-1]] > arr[i]:
                st.pop()
            
            # Update the answer
            ans[i] = st[-1] if st else -1
            
            # Push the index of current 
            # element in the stack
            st.append(i)
        
        # Return the answer
        return ans

    def sumSubarrayMins(self, arr):
        
        nse = self.findNSE(arr)
        psee = self.findPSEE(arr)
        
        # Size of array
        n = len(arr)
        
        mod = int(1e9 + 7)  # Mod value
        
        # To store the sum
        total_sum = 0
        
        # Traverse on the array
        for i in range(n):
            
            # Count of first type of subarrays
            left = i - psee[i]
            
            # Count of second type of subarrays
            right = nse[i] - i
            
            # Count of subarrays where 
            # current element is minimum
            freq = left * right * 1
            
            # Contribution due to current element 
            val = (freq * arr[i]) % mod
            
            # Updating the sum
            total_sum = (total_sum + val) % mod
        
        # Return the computed sum
        return total_sum

    def subArrayRanges(self, nums):
      return self.sumSubarrayMax(nums) - self.sumSubarrayMins(nums)


nums = [1, 2, 3]
print(Solution().subArrayRanges(nums))
     