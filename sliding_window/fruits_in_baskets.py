# There is only one row of fruit trees on the farm, oriented left to right. An integer array called fruits represents the trees, where fruits[i] denotes the kind of fruit produced by the ith tree.
# The goal is to gather as much fruit as possible, adhering to the owner's stringent rules:
# 1) There are two baskets available, and each basket can only contain one kind of fruit. The quantity of fruit each basket can contain is unlimited.
# 2) Start at any tree, but as you proceed to the right, select exactly one fruit from each tree, including the starting tree. One of the baskets must hold the harvested fruits.
# 3) Once reaching a tree with fruit that cannot fit into any basket, stop.
# Return the maximum number of fruits that can be picked.

class Solution:
  def totalFruitsOptimal(self, fruits):
    # Length of the input array
    n = len(fruits)
    
    """ Variable to store the 
    maximum length of substring """
    maxLen = 0  
    
    """ Dictionary to track the count of each
    fruit type in the current window """
    mpp = {}
    
    # Pointers for the sliding window approach
    l, r = 0, 0
    
    while r < n:
        mpp[fruits[r]] = mpp.get(fruits[r], 0) + 1
        
        """ If number of different fruits exceeds
          2 shrink the window from the left """
        if len(mpp) > 2:
            mpp[fruits[l]] -= 1
            if mpp[fruits[l]] == 0:
                del mpp[fruits[l]]
            l += 1
        
        """ If number of different fruits 
        is at most 2, update maxLen """
        if len(mpp) <= 2:
            maxLen = max(maxLen, r - l + 1)
        
        r += 1
    
    # Return the maximum fruit
    return maxLen

  def totalFruits(self, fruits):
    l = 0
    r = 0
    max_len =0
    n = len(fruits)
    b1 = None
    b2 = None
    while r < n:
      fruit = fruits[r]

      if b1 == None and fruit != b2:
        b1 = fruit
      elif b2 == None and fruit != b1:
        b2 = fruit
      elif b1 != fruit and b2 != fruit:          
        l = r - 1
        if fruits[l] == b1:
            while l > 0 and fruits[l] != b1:
              l -= 1
            b2 = fruit
        if fruits[l] == b2:
            while l > 0 and fruits[l] != b2:
              l -= 1
            b1 = b2
            b2 = fruit
      if fruit == b1 or fruit == b2:
        max_len = max(max_len,r-l+1)

      r += 1
    return max_len

if __name__ == "__main__":
  fruits = [1,0,1,4,1,4,1,2,3]
  print(Solution().totalFruitsOptimal(fruits))
  