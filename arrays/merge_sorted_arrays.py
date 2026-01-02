# Given two integer arrays nums1 and nums2. Both arrays are sorted in non-decreasing order.

# Merge both the arrays into a single array sorted in non-decreasing order.
#     The final sorted array should be stored inside the array nums1 and it should be done in-place.
#     nums1 has a length of m + n, where the first m elements denote the elements of nums1 and rest are 0s.
#     nums2 has a length of n.

class Solution:
    # Function to merge two sorted arrays nums1 and nums2
    def merge(self, nums1, m, nums2, n):
        i, j = m - 1, n - 1
        ind = m + n - 1

        # Until all the elements from nums2 are placed
        while j >= 0:
            # If nums1[i] >= nums2[j]
            if i >= 0 and nums1[i] >= nums2[j]:
                # Place the element
                nums1[ind] = nums1[i]

                # Move both indices back by one place
                ind -= 1
                i -= 1
            # Otherwise
            else:
                # Place the element
                nums1[ind] = nums2[j]

                # Move both indices back by one place
                ind -= 1
                j -= 1