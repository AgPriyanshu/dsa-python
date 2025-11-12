# Determine all possible set of k numbers that can be added together to equal n while meeting the following requirements:
#     There is only use of numerals 1 through 9.
#     A single use is made of each number.
# Return list of every feasible combination that is allowed. The combinations can be returned in any order, but the list cannot have the same combination twice.

def combination_sum3(nums,target,subseq_arr,ans,index,k):
  if index == len(nums) and target == 0 and len(subseq_arr) == k:
    ans.append(subseq_arr[:])
    return
  if index == len(nums) or target < 0 or len(subseq_arr) > k:
    return 

  subseq_arr.append(nums[index])
  combination_sum3(nums,target-nums[index],subseq_arr,ans,index+1,k)
  subseq_arr.pop()
  combination_sum3(nums,target,subseq_arr,ans,index+1,k)


  return ans

if __name__ == "__main__":
  k = 3
  n = 7
  nums = list(range(1,10))
  print(combination_sum3(nums,n,[],[],0,k))