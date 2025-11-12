# Given an integer array nums, which can have duplicate entries, provide the power set.
# Duplicate subsets cannot exist in the solution set. Return the answer in any sequence.

def subset_sum2(nums,subarr,ans,index):
    if index == len(nums):
        ans.append(subarr[:])
        return
    subarr.append(nums[index])
    subset_sum2(nums,subarr,ans,index + 1)
    subarr.pop()
    j = index + 1
    while j < len(nums) and nums[j] == nums[index]:
        j += 1
    subset_sum2(nums,subarr,ans,j)

    return ans

if __name__ == "__main__":
    nums = [1, 2, 2]
    nums2 = sorted(nums)
    print(subset_sum2(nums2,[],[],0))