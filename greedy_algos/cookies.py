# Consider a scenario where a teacher wants to distribute cookies to students, with each student receiving at most one cookie.
# Given two arrays, student and cookie, the ith value in the Student array describes the minimum size of cookie that the ith student can be assigned. The jth value in the Cookie array represents the size of the jth cookie. If Cookie[j] >= Student[i], the jth cookie can be assigned to the ith student.
# Maximize the number of students assigned with cookies and output the maximum number.

class Solution:
  def findMaximumCookieStudents(self, Student, Cookie):
    students = sorted(Student)
    cookies = sorted(Cookie)

    i,j = 0,0
    count = 0
    while i < len(students) and j < len(cookies):
      if cookies[j] >= students[i]:
        count += 1
        i += 1
        j += 1
      
      else:
        j += 1

    return count

if __name__ == "__main__":
  student = [1, 2] 
  cookie = [1, 2, 3]
  print(Solution().findMaximumCookieStudents(student,cookie))