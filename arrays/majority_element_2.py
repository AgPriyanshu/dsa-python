# Given an integer array nums of size n. Return all elements which appear more than n/3 times in the array. The output can be returned in any order.
import math
class Solution:
    def majorityElementTwo(self, nums):
        n = len(nums)
        el1,c1,el2,c2 = 0,0,0,0
        for num in nums:
            if c1 == 0  and num != el2:
                el1 = num
                c1 = 1

            elif c2 == 0 and num != el1:
                el2 = num
                c2 = 1
            
            elif num == el1:
                c1 += 1
            elif num == el2:
                c2 += 1
            else:
                c1 -= 1
                c2 -= 1
        
        # To confirm.
        c1 = 0
        for num in nums:
            if num == el1:
                c1 += 1
            
        c2 = 0
        for num in nums:
            if num == el2:
                c2 += 1
        ans = []
        # print(el1,el2)
        if c1 > math.floor(n/3):
            ans.append(el1) 
        if c2 > math.floor(n/3):
            ans.append(el2)
        return ans         


if __name__ == "__main__":
    nums = [1,1,1,3,3,2,2,2]
    print(Solution().majorityElementTwo(nums))