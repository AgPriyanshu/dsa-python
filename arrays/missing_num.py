from typing import List

class Solution:
    # Function to find the missing number
    def missingNumber(self, nums: List[int]) -> int:
        xor1 = 0
        xor2 = 0

        # Calculate XOR of all array elements
        for i in range(len(nums)):
            xor1 ^= (i + 1)  # XOR up to [1...N]
            xor2 ^= nums[i]  # XOR of array elements

        # XOR of xor1 and xor2 gives missing number
        return xor1 ^ xor2