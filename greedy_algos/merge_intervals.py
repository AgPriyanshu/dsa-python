# Given a 2D array Intervals, where Intervals[i] = [start[i], end[i]] represents the start and end of the ith interval, the array represents non-overlapping intervals sorted in ascending order by start[i]. 


# Given another array newInterval, where newInterval = [start, end] represents the start and end of another interval, merge newInterval into Intervals such that Intervals remain non-overlapping and sorted in ascending order by start[i].

class Solution:
    # To insert new interval
    def insertNewInterval(self, intervals, new_interval):
        # Initialize result
        res = []
        
        # Track the index 
        i = 0
        
        # Get total intervals
        n = len(intervals)
        
        # Insert intervals before new_interval
        while i < n and intervals[i][1] < new_interval[0]:
            # Add intervals to the result 
            # list until their end time 
            # is before the start time 
            # of new_interval
            res.append(intervals[i])
            # Move to next interval
            i += 1
        
        # Merge overlapping intervals
        while i < n and intervals[i][0] <= new_interval[1]:
            # Update the start time of new_interval to the minimum 
            # of its current start time and the start time of the 
            # current interval
            new_interval[0] = min(new_interval[0], intervals[i][0])
            # Update the end time of new_interval to the maximum 
            # of its current end time and the end time of the 
            # current interval
            new_interval[1] = max(new_interval[1], intervals[i][1])
            # Move to the next interval
            i += 1
        
        # Insert the merged interval
        res.append(new_interval)
        
        # Insert remaining 
        # intervals after 
        # new_interval
        while i < n:
            # Add the remaining 
            # intervals after new_interval
            # to the result list
            res.append(intervals[i])
            # Move to next interval
            i += 1
        
        # Return result 
        return res

# Intervals = [ [1, 2] , [3, 5] , [6, 7] , [8,10] ] 
# newInterval = [4, 8]
Intervals = [[1, 2], [3, 4], [6, 7], [8, 10], [12, 16]]
newInterval = [5, 8]




print(Solution().insertNewInterval(Intervals,newInterval))