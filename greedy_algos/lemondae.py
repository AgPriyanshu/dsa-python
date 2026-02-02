# Each lemonade at a booth sells for $5. Consumers are lining up to place individual orders, following the billing order. Every consumer will purchase a single lemonade and may pay with a $5, $10, or $20 bill. Each customer must receive the appropriate change so that the net transaction is $5. Initially, there is no change available.
# Determine if it is possible to provide the correct change to every customer. Return true if the correct change can be given to every customer, and false otherwise.
# Given an integer array bills, where bills[i] is the bill the ith customer pays, return true if the correct change can be given to every customer, and false otherwise.
class Solution:
  def lemonadeChange(self, bills):
    five_dollars = 0
    ten_dollars = 0
    for bill in bills:
      if bill == 5:
        five_dollars += 1
      elif bill == 10:
        five_dollars -= 1
        ten_dollars += 1
      elif bill == 20:
        if ten_dollars > 0 and five_dollars > 0:
          ten_dollars -= 1 
          five_dollars -= 1

        elif five_dollars >= 3:
          five_dollars -= 3
        else:
          return False
    
    return True


if __name__ == "__main__":
  bills = [5, 5, 10, 10, 20]
  print(Solution().lemonadeChange(bills))
