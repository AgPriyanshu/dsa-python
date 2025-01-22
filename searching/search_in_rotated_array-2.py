# Problem Statement: Given an integer array arr of size N, sorted in ascending order (may contain duplicate values) and a target value k. Now the array is rotated at some pivot point unknown to you. Return True if k is present and otherwise, return False.


def search_in_rotated_array_2(nums, target):
    low = 0
    high = len(nums) - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid
        elif nums[low] == nums[mid] == nums[high]:  # For duplicates handling.
            low += 1
            high -= 1
        elif nums[low] <= nums[mid]:  # Means left is sorted.
            if target >= nums[low] and target <= nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
        elif nums[high] >= nums[mid]:  # Means right is sorted.
            if target <= nums[high] and target >= nums[mid]:
                low = mid + 1
            else:
                high = mid - 1


if __name__ == "__main__":
    print(search_in_rotated_array_2([3, 1, 2, 3, 3, 3, 3], 3))
