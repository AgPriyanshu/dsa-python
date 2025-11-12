# Given collection of candidate numbers (candidates) and a integer target.Find all unique combinations in candidates where the sum is equal to the target.There can only be one usage of each number in the candidates combination and return the answer in sorted order.
# e.g : The combination [1, 1, 2] and [1, 2, 1] are not unique.

def combination_sum2(nums,target,subseq_arr,ans,index):
  if index == len(nums) and target == 0:
    ans.append(subseq_arr[:])
    return
  if index == len(nums) or target < 0:
    return 

  subseq_arr.append(nums[index])
  combination_sum2(nums,target-nums[index],subseq_arr,ans,index+1)
  subseq_arr.pop()

  j = index + 1
  while j < len(nums) and nums[j] == nums[index]:
    j+=1
  combination_sum2(nums,target,subseq_arr,ans,j)


  return ans

if __name__ == "__main__":
  nums = [2, 1, 2, 7, 6, 1, 5]
  target = 8
  nums2 = sorted(nums)
  print(combination_sum2(nums2,target,[],[],0))