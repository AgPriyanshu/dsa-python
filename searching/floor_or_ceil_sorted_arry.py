# Problem Statement: You're given an sorted array arr of n integers and an integer x. Find the floor and ceiling of x in arr[0..n-1].
# The floor of x is the largest element in the array which is smaller than or equal to x.
# The ceiling of x is the smallest element in the array greater than or equal to x.
from typing import List

def floor_and_ceil(arr: List[int],x: int):
  n = len(arr)
  lb = 0
  ub = n - 1
  floor = -1
  ceil = -1
  while lb < ub:
    mid = ( lb + ub ) // 2
    print(lb,ub,floor,ceil)
    if arr[mid] <= x:
      floor = mid
      lb = mid + 1
    else:
      ceil = mid
      ub = mid -1
  print(lb,ub,floor,ceil) 
  return -1 if floor == -1 else arr[floor], -1 if ceil == -1 else arr[ceil]


if __name__ == "__main__":
        0  1.  2. 3. 4. 5
  arr = [3, 4, 4, 7, 8, 10]
  x = 5
  print(floor_and_ceil(arr, x))