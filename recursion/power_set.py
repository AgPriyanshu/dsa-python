# Given an array of integers nums of unique elements. Return all possible subsets (power set) of the array.
# Do not include the duplicates in the answer.
from copy import copy
def power_set(nums,ans,result,j):
  if j == len(nums):
    ans.append(result[:])
    return 

  result.append(nums[j])
  power_set(nums,ans,result,j+1)
  result.pop()
  power_set(nums,ans,result,j+1)
 

if __name__ == "__main__":
  nums = [1,2,3]
  ans = []
  power_set(nums,ans,[],0)
  print(ans)