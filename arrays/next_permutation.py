# A permutation of an array of integers is an arrangement of its members into a sequence or linear order.


# For example, for arr = [1,2,3], the following are all the permutations of arr:

# [1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1].


# The next permutation of an array of integers is the next lexicographically greater permutation of its integers.

# More formally, if all the permutations of the array are sorted in lexicographical order, then the next permutation of that array is the permutation that follows it in the sorted order.


# If such arrangement is not possible (i.e., the array is the last permutation), then rearrange it to the lowest possible order (i.e., sorted in ascending order).


# You must rearrange the numbers in-place and use only constant extra memory.
class Solution:
  def nextPermutation(self, nums):
    break_point = None
    for i in range(len(nums)-2,-1,-1):
      if nums[i] < nums[i+1]:
        break_point = i
        break

    if  break_point is None:
      nums.reverse()
      return nums

    for i in range(len(nums)-1,break_point,-1):
      if nums[i] > nums[break_point]:
        print(nums[i])
        nums[i],nums[break_point] = nums[break_point],nums[i] 
        break

    nums[break_point+1:] = reversed(nums[break_point+1:])
    return nums

nums = [1,3,2]
print(Solution().nextPermutation(nums))
