# Problem Statement: Given two numbers N and M, find the Nth root of M. The nth root of a number M is 
# defined as a number X when raised to the power N equals M. If the 'nth root is not an integer, return -1.

def nth_root(n: int,m: int):
  nums = range(n+1)
  lb = 0
  ub = len(nums) - 1

  while lb <= ub:
    mid = (lb + ub) // 2

    if nums[mid]**n == m:
      return mid
    elif nums[mid]**n > m:
      ub = mid - 1
    else:
      lb = mid + 1
  
  return -1

if __name__ == "__main__":
  n = 4
  m = 69
  print(nth_root(n,m))