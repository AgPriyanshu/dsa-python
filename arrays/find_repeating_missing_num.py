# Given an integer array nums of size n containing values from [1, n] and each value appears exactly once in the array, except for A, which appears twice and B which is missing.
# Return the values A and B, as an array of size 2, where A appears in the 0-th index and B in the 1st index.
# Note: You are not allowed to modify the original array.
class Solution:
    # Function to find repeating and missing numbers
    def findMissingRepeatingNumbers(self, nums):
        
        # Size of the array
        n = len(nums)

        # Sum of first n natural numbers
        SN = (n * (n + 1)) // 2

        # Sum of squares of first n natural numbers
        S2N = (n * (n + 1) * (2 * n + 1)) // 6

        """ Calculate actual sum (S) and sum 
            of squares (S2) of array elements """
        S = 0
        S2 = 0
        for num in nums:
            S += num
            S2 += num * num

        # Compute the difference values
        val1 = S - SN

        # S2 - S2n = X^2 - Y^2
        val2 = S2 - S2N

        # Calculate X + Y using X + Y = (X^2 - Y^2) / (X - Y)
        val2 = val2 // val1

        """ Calculate X and Y from X + Y and X - Y
            X = ((X + Y) + (X - Y)) / 2
            Y = X - (X - Y) """
        x = (val1 + val2) // 2
        y = x - val1

        # Return the results as [repeating, missing]
        return [int(x), int(y)]

nums = [3, 1, 2, 5, 4, 6, 7, 5]

# Create an instance of Solution class
sol = Solution()

result = sol.findMissingRepeatingNumbers(nums)

# Print the repeating and missing numbers found
print(f"The repeating and missing numbers are: {{{result[0]}, {result[1]}}}")
