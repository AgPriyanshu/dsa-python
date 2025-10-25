# Problem Statement: Given an integer array arr of size N, sorted in ascending order (with distinct values) and a target value k. Now the array is rotated at some pivot point unknown to you. Find the index at which k is present and if k is not present return -1.


def search_in_rotated_array(nums, target):
    lb = 0
    ub = len(nums) - 1
    while lb <= ub:
        mid = (lb + ub) // 2
        if nums[mid] == target:
            return mid
        elif nums[lb] <= nums[mid]:
            if nums[lb] <= target and target <= nums[mid]:
                ub = mid - 1
            else:
                lb = mid + 1
        elif nums[ub] >= nums[mid]:
            if nums[ub] >= target and target >= nums[mid]:
                lb = mid + 1
            else:
                ub = mid -1
    return -1

if __name__ == "__main__":
    print(search_in_rotated_array([4, 5, 6, 7, 0, 1, 2], 0))
