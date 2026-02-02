# Given one meeting room and N meetings represented by two arrays, start and end, where start[i] represents the start time of the ith meeting and end[i] represents the end time of the ith meeting, determine the maximum number of meetings that can be accommodated in the meeting room if only one meeting can be held at a time.

class Solution:
  def maxMeetings(self, start, end):
    new = []
    for i in range(len(start)):
      new.append([start[i],end[i]])

    new = sorted(new,key=lambda x: (x[1],x[0]))
    print(new)
    last_end_time = 0
    count = 0
    for meeting in new:
      start = meeting[0]
      end = meeting[1]
      if start > last_end_time:
        count += 1
        last_end_time = end
    
    return count

Start = [1, 3, 0, 5, 8, 5]
End = [2, 4, 6, 7, 9, 9]

print(Solution().maxMeetings(Start,End))