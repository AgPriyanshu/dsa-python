# Given an integer array nums. Return the number of inversions in the array.
# Two elements a[i] and a[j] form an inversion if a[i] > a[j] and i < j.
#     It indicates how close an array is to being sorted.
#     A sorted array has an inversion count of 0.
#     An array sorted in descending order has maximum inversion.

class Solution:
  def merge(self,nums,low,mid,high):
    temp = []
    i = low
    j = mid +1 
    count = 0
    while i <= mid and j <= high:
      if nums[i] <= nums[j]:
        temp.append(nums[i])
        i += 1
      elif nums[i] > nums[j]:
        temp.append(nums[j])
        j += 1
        count += mid-i+1

    while i <= mid:
      temp.append(nums[i])
      i += 1

    while j <= high:
      temp.append(nums[j])
      j += 1

    for k in range(len(temp)):
      nums[low+k] = temp[k]

    return count
  
  def partition(self,nums,low,high):
    mid = (low+high)//2
    count = 0
    if low < high:
      count += self.partition(nums,low,mid)
      count += self.partition(nums,mid+1,high)
      count += self.merge(nums,low,mid,high)
    return count  
  def numberOfInversions(self, nums):
    return self.partition(nums,0,len(nums)-1)

if __name__ == "__main__":
  nums = [-10, -5, 6, 11, 15, 17]
  print(Solution().numberOfInversions(nums))