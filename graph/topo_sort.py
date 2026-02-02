# Given a Directed Acyclic Graph (DAG) with V vertices labeled from 0 to V-1.The graph is represented using an adjacency list where adj[i] lists all nodes connected to node. Find any Topological Sorting of that Graph.

# In topological sorting, node u will always appear before node v if there is a directed edge from node u towards node v(u -> v).

# The function should return an array representing the topological order. The output will be validated by our driver code, which checks the correctness of your topological sort. It will print True if the order is valid, otherwise False.
from collections import deque

class Solution:
  def bfs(self,V,adj):
    indegree = [0]*V
    for i in range(V):
      for node in adj[i]:
        indegree[node] +=1

    q = deque()

    for i in range(V):
      if indegree[i] == 0:
        q.append(i)

    ans = []

    while q:
      node = q.popleft()
      ans.append(node)

      for it in adj[node]:
        indegree[it] -= 1

        if indegree[it] == 0:
          q.append(it)

    return ans    

  def dfs(self,node,V,adj,visited,stack):
    visited[node] = True
    for child in adj[node]:
      if not visited[child]:
        self.dfs(child,V,adj,visited,stack)
    stack.append(node)
        
     
  def topoSort(self, V, adj):
    # visited = [False]*V
    # stack =[]
    # for i in range(V):
    #   if not visited[i]:
    #     self.dfs(i,V,adj,visited,stack)
    # stack.reverse()
    # return stack
    return self.bfs(V,adj)

if __name__ == "__main__":
  V = 6
  adj=[ [ ], [ ], [3], [1], [0,1], [0,2] ]
  print(Solution().topoSort(V,adj))