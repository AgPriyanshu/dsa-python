# Provided with a goal integer target and an array of unique integer candidates, provide a list of all possible combinations of candidates in which the selected numbers add up to the target. The combinations can be returned in any order.
# A candidate may be selected from the pool an infinite number of times. There are two distinct combinations if the frequency of at least one of the selected figures differs.
# The test cases are created so that, for the given input, there are fewer than 150 possible combinations that add up to the target.
# If there is no possible subsequences then return empty vector.

def combination_sum(nums,target,subseq_arr,ans,index):
  if index == len(nums) and target == 0:
    ans.append(subseq_arr[:])
    return
  if index == len(nums) or target < 0:
    return 

  subseq_arr.append(nums[index])
  combination_sum(nums,target-nums[index],subseq_arr,ans,index)
  subseq_arr.pop()
  combination_sum(nums,target,subseq_arr,ans,index+1)


  return ans

if __name__ == "__main__":
  nums = [2, 3, 5, 4]
  target = 7
  print(combination_sum(nums,target,[],[],0))