# Given an array nums and an integer k. R﻿eturn true if there exist subsequences such that the sum of all elements in subsequences is 
# equal to k else false.

def subseq_with_k_sum(nums,sub_seq_sum,k,index,prev):
  if sub_seq_sum == k:
    return True

  if index == len(nums):
    return False  
  temp = sub_seq_sum
  return subseq_with_k_sum(nums,temp + nums[index],k,index + 1,temp) or subseq_with_k_sum(nums,temp,k,index + 1,prev)
  
if __name__ == "__main__":
  nums = [1, 10, 4, 5]
  k = 16

  print(subseq_with_k_sum(nums,0,8,0,0))
