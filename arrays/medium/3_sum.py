# Problem Statement: Given an array of N integers, your task is to find unique triplets that add up to give a sum
# of zero.
# In short, you need to return an array of all the unique triplets [arr[a], arr[b], arr[c]] such that
# i!=j, j!=k, k!=i, and their sum is equal to zero.


def three_sum_better(nums,target=0):
    triplet = set()
    n = len(nums)
    for i in range(n):
        hash_map = {}
        for j in range(n):
            third = -(nums[i] + nums[j])
            if hash_map.get(third):
                triplet.add(tuple(sorted([nums[i],third,nums[j]])))
            else:
                hash_map[nums[j]] = j

    return list(triplet)

def three_sum_optimal(nums, target=0):
    n = len(nums)
    nums = sorted(nums)
    result = []
    i = 0
    while i < n:
        j = i + 1
        k = n - 1
        while j < k and j < n: 
            if nums[i] + nums[j] + nums[k] < target:
                j += 1
            elif nums[i] + nums[j] + nums[k] > target:
                k -= 1
            else:
                result.append([nums[i],nums[j],nums[k]])
                # To remove duplicates.
                while nums[j] == nums[j+1] and j < k:
                    j += 1
                while nums[k] == nums[k-1] and k > j:
                    k -= 1
                j+=1
                k-=1

        while i+1 < n and nums[i] == nums[i+1]:
            i += 1
        i += 1
    
    return result


            



if __name__ == "__main__":
    print(
        three_sum_optimal(
            [2, -1,  -1, 3, -1],
        )
    )
