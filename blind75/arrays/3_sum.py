# Problem Statement: Given an array of N integers, your task is to find unique triplets that add up to give a sum
# of zero.
# In short, you need to return an array of all the unique triplets [arr[a], arr[b], arr[c]] such that
# i!=j, j!=k, k!=i, and their sum is equal to zero.


def three_sum(nums, target=0):
    n = len(nums)
    s = set()
    nums.sort()
    for i in range(n - 1):
        # remove duplicates:
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        j = i + 1
        k = n - 1
        while j < k:
            total_sum = nums[i] + nums[j] + nums[k]
            if total_sum == 0:
                temp = (nums[i], nums[j], nums[k])
                s.add(temp)
                j += 1
                k -= 1

                # To remove duplicates if asked
                # while j < k and nums[j] == nums[j + 1]:
                #     j += 1
                # while k > j and nums[k] == nums[k - 1]:
                #     k -= 1
            elif total_sum > 0:
                k -= 1
            else:
                j += 1
    return list(s)


if __name__ == "__main__":
    print(
        three_sum(
            [-2, 0, 0, 2, 2],
        )
    )
