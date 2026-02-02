
# Given an array of N intervals in the form of (start[i], end[i]), where start[i] is the starting point of the interval and end[i] is the ending point of the interval, return the minimum number of intervals that need to be removed to make the remaining intervals non-overlapping.

class Solution:
  def MaximumNonOverlappingIntervals(self, Intervals):
    sorted_intervals = sorted(Intervals,key=lambda x: (x[1],x[0]))
    count = 0
    last_interval = sorted_intervals[0][1]
    for i in range(1,len(sorted_intervals)):
      start = sorted_intervals[i][0]
      end = sorted_intervals[i][1]

      if start < last_interval:
        count += 1
      else:
        last_interval = end
    
    return count



Intervals = [ [1, 10] , [1, 4] , [3, 8] , [3, 4] , [4, 5] ]

print(Solution().MaximumNonOverlappingIntervals(Intervals))