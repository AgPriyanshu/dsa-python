# Given an array nums of n integers. Return array of sum of all subsets of the array nums.
# Output can be returned in any order.

def subset_sum(nums,sum,ans,index):
    if index == len(nums):
        ans.append(sum)
        return
    subset_sum(nums,sum + nums[index],ans,index + 1)
    subset_sum(nums,sum,ans,index + 1)

    return ans

if __name__ == "__main__":
    nums = [2,3]
    print(subset_sum(nums,0,[],0))