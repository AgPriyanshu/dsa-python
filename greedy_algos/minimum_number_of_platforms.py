# Given the arrival and departure times of all trains reaching a particular railway station, determine the minimum number of platforms required so that no train is kept waiting. Consider all trains arrive and depart on the same day.


# In any particular instance, the same platform cannot be used for both the departure of one train and the arrival of another train, necessitating the use of different platforms in such cases.


# Note: Time intervals are in the 24-hour format (HHMM) , where the first two characters represent hour (between 00 to 23 ) and the last two characters represent minutes (this will be <= 59 and >= 0). Leading zeros for hours less than 10 are optional (e.g., 0900 is the same as 900).

class Solution:
  def findPlatform(self, Arrival, Departure):
    a = Arrival
    d = sorted(Departure)
    i = 0
    j = 0 
    count = 0
    maxCount = 0
    while i < len(a) and j < len(d):
      if a[i] < d[j]:
        count += 1
        maxCount = max(count,maxCount)
        i += 1
      else:
        count -= 1
        j += 1
    return maxCount
    
Arrival = [900, 940, 950, 1100, 1500, 1800] 
Departure = [910, 1200, 1120, 1130, 1900, 2000]

print(Solution().findPlatform(Arrival,Departure))