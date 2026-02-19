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
        print(ngei,pgei)
        sum = 0

        for i in range(len(arr)):
            left = i - pgei[i]
            right = ngei[i] - i
            freq = right*left
            sum  += freq*arr[i]
        return sum

        
# Main function to test the solution
if __name__ == "__main__":
    arr = [3, 1, 2, 5]
    ngei = [3,2,3,4]
    pgei = [-1,0,0,-1]
    
    # Creating an instance of Solution class
    sol = Solution()
    
    # Function call to find the sum of the 
    # minimum value in each subarray
    ans = sol.sumSubarrayMax(arr)
    
    print("The sum of minimum value in each subarray is:", ans)
