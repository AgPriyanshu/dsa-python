# Problem Statement: You are given a positive integer n. Your task is to find and return its square root.
#  If ‘n’ is not a perfect square, then return the floor value of sqrt(n). 

def bs_sqrt(n: int):
  nums = range(n+1)
  lb = 0
  ub = len(nums) - 1

  while lb <= ub:
    mid = (lb + ub) // 2

    if nums[mid]**2 == n:
      return mid
    elif nums[mid]**2 > n:
      ub = mid - 1
    else:
      lb = mid + 1
  
  return ub

if __name__ == "__main__":
  n = 64
  print(bs_sqrt(n))