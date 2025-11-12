def count_all_substring_with_sum_k(nums,k,index,sums,prev):
  if sums == k:
    return 1
  if index == len(nums):
    return 0

  return count_all_substring_with_sum_k(nums,k,index+1,sums + nums[index],sums) + count_all_substring_with_sum_k(nums,k,index+1,sums,prev)

if __name__ == "__main__":
  nums = [4, 2, 10, 5, 1, 3]
  k = 5
  print(count_all_substring_with_sum_k(nums,k,0,0,0))