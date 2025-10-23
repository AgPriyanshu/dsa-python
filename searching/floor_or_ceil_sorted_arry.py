# Problem Statement: You're given an sorted array arr of n integers and an integer x. Find the floor and ceiling of x in arr[0..n-1].
# The floor of x is the largest element in the array which is smaller than or equal to x.
# The ceiling of x is the smallest element in the array greater than or equal to x.
from typing import List

def floor_and_ceil(arr: List[int],x: int):
  n = len(arr)
  lb = 0
  ub = n - 1
  floor = n
  ceil = n 
  while lb < ub:
    mid = ( lb + ub ) // 2
    if arr[mid] < x:
      floor = mid
      lb = mid + 1
    elif arr[mid] == x:
      floor = mid
      return arr[mid], arr[mid]
    else:
      ub = mid -1 
  return arr[floor], arr[floor + 1]


if __name__ == "__main__":
  arr = [3, 4, 4, 7, 8, 10]
  x = 8
  print(floor_and_ceil(arr, x))