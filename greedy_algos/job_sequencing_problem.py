# Given an 2D array Jobs of size Nx3, where Jobs[i][0] represents JobID , Jobs[i][1] represents Deadline , Jobs[i][2] represents Profit associated with that job. Each Job takes 1 unit of time to complete and only one job can be scheduled at a time.
# The profit associated with a job is earned only if it is completed by its deadline. Find the number of jobs and maximum profit.

class Solution:
  def JobScheduling(self, Jobs):
    jobs = sorted(Jobs,key=lambda row: row[2],reverse=True )
    deadlines = [None]* len(jobs)
    max_profit = 0
    count = 0
    for job in jobs:
      profit = job[2]
      deadline = job[1]
      job_id = job[0]

      free_deadline = deadline - 1
      while free_deadline >=0 and deadlines[free_deadline] is not None :
        free_deadline -= 1

      if free_deadline < 0:
        continue

      if not deadlines[free_deadline]:
        deadlines[free_deadline] = job_id
        count += 1
        max_profit +=profit
    return count, max_profit

if __name__ == "__main__":
  Jobs = [ [1, 4, 20] , [2, 1, 10] , [3, 1, 40] , [4, 1, 30] ]
  print(Solution().JobScheduling(Jobs))