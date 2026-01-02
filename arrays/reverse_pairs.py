# Given an integer array nums. Return the number of reverse pairs in the array.
# An index pair (i, j) is called a reverse pair if:
#     0 <= i < j < nums.length
#     nums[i] > 2 * nums[j]

class Solution:
    def reversePairs(self, nums):
        return self.merge_sort(nums, 0, len(nums) - 1)

    # Merge sort with reverse pair count
    def merge_sort(self, nums, low, high):
        if low >= high:
            return 0

        mid = (low + high) // 2
        cnt = 0
        cnt += self.merge_sort(nums, low, mid)
        cnt += self.merge_sort(nums, mid + 1, high)
        cnt += self.count_pairs(nums, low, mid, high)
        self.merge(nums, low, mid, high)

        return cnt

    # Count reverse pairs across two sorted halves
    def count_pairs(self, nums, low, mid, high):
        right = mid + 1
        cnt = 0

        for i in range(low, mid + 1):
            while right <= high and nums[i] > 2 * nums[right]:
                right += 1
            cnt += right - (mid + 1)

        return cnt

    # Merge function
    def merge(self, nums, low, mid, high):
        temp = []
        left, right = low, mid + 1

        while left <= mid and right <= high:
            if nums[left] <= nums[right]:
                temp.append(nums[left])
                left += 1
            else:
                temp.append(nums[right])
                right += 1

        while left <= mid:
            temp.append(nums[left])
            left += 1
        while right <= high:
            temp.append(nums[right])
            right += 1

        nums[low:high + 1] = temp



if __name__ == "__main__":
  nums = [-3 -2]
  print(Solution().reversePairs(nums))