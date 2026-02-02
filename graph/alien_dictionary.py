# Given a sorted dictionary of an alien language having N words and K starting alphabets of a standard dictionary. Find the order of characters in the alien language.

# There may be multiple valid orders for a particular test case, thus you may return any valid order as a string. The output will be True if the order returned by the function is correct, else False denoting an incorrect order. If the given arrangement of words is inconsistent with any possible letter ordering, return an empty string "".
from collections import deque
class Solution:
  def topoSort(self,V,adj):
    indegree = [0]*V
    for i in range(V):
      for it in adj[i]:
        indegree[it] += 1  

    q = deque()
    for i in range(V):
      if indegree[i] == 0:
        q.append(i)
    ans = []
    while q: 
      node = q.popleft()
      ans.append(node)
      for i in adj[node]:
        indegree[i] -= 1
        if indegree[i] == 0:
          q.append(i)
    for index,value in enumerate(ans):
        ans[index] = chr(ord('a') + value)

    return ans

  def findOrder(self, dict, N, K):
    adj = [[] for _ in range(K)]
    n = len(dict)
    for i in range(n-1):
      j = i + 1
      min_length = min(len(dict[i]),len(dict[j]))
      for k in range(min_length):
        if dict[i][k] != dict[j][k]:
          first_word_letter = ord(dict[i][k])  - ord('a')
          second_word_letter = ord(dict[j][k]) - ord('a')

          adj[first_word_letter].append(second_word_letter) 
          break
    
    return " ".join(self.topoSort(K,adj))


if __name__ == "__main__":
  N = 5 
  K = 4 
  dict = ["baa","abcd","abca","cab","cad"]
  print(Solution().findOrder(dict,N,K))  
