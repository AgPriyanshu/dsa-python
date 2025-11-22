# Given an integer array nums and an integer target. Return all quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:


#     a, b, c, d are all distinct valid indices of nums.


#     nums[a] + nums[b] + nums[c] + nums[d] == target.


# Notice that the solution set must not contain duplicate quadruplets. One element can be a part of multiple quadruplets. The output and the quadruplets can be returned in any order.



def four_sum_optimal(nums, target=0):
    n = len(nums)
    nums = sorted(nums)
    result = []
    i = 0
    while i < n:
        j = i + 1
        while j < n:            
            k = j + 1
            l = n - 1 

            while k < l and k < n: 
                if nums[i] + nums[j] + nums[k] + nums[l] < target:
                    k += 1
                elif nums[i] + nums[j] +  nums[k] + nums[l] > target:
                    l -= 1
                else:
                    result.append([nums[i],nums[j],nums[k],nums[l]])
                    # To remove duplicates.
                    while nums[k] == nums[k+1] and k < l:
                        k += 1
                    while nums[l] == nums[l-1] and l > k:
                        l -= 1
                    k += 1
                    l -= 1

            while j+1 < n and nums[j] == nums[j+1]:
                j += 1
            j += 1
        while i+1 < n and nums[i] == nums[i+1]:
            i += 1
        i += 1
    
    return result


            



if __name__ == "__main__":
    print(
        four_sum_optimal(
 [1,1,3,4,-3],target=5
        )
    )
