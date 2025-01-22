# Problem Statement: Given an integer array arr of size N, sorted in ascending order (with distinct values) and a target value k. Now the array is rotated at some pivot point unknown to you. Find the index at which k is present and if k is not present return -1.


def search_in_rotated_array(nums, target):
    low = 0
    high = len(nums) - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid
        elif nums[low] <= nums[mid]:  # Means left is sorted.
            if target >= nums[low] and target < nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
        elif nums[high] >= nums[mid]:  # Means right is sorted.
            if target <= nums[high] and target > nums[mid]:
                low = mid + 1
            else:
                high = mid - 1
    return -1


if __name__ == "__main__":
    print(search_in_rotated_array([4, 5, 6, 7, 0, 1, 2], 0))
