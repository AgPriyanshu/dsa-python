# Given a directed graph with V vertices labeled from 0 to V-1. The graph is represented using an adjacency list where adj[i] lists all nodes connected to node. Determine if the graph contains any cycles.
from collections import deque

class Solution:
  def bfs(self,V,adj): # Kahn's
    indegree = [0]*V
    
    for i in range(V):
      for node in adj[i]:
        indegree[node] += 1

    q = deque()

    for i in range(V):
      if indegree[i] == 0:
        q.append(i)

    ans = []
    while q:
      node = q.popleft()
      ans.append(node)
      for child in adj[node]:
        indegree[child] -= 1
        if indegree[child] == 0:
          q.append(child)
    if len(ans) < V:
      return True
    return False

    
  def dfs(self,node,V,adj,visited,path_visited):
    visited[node] = True
    path_visited[node] = True
    for child in adj[node]:
      if visited[child] and path_visited[child]:
        return True
      elif not visited[child] and not path_visited[child]:
        isCycle = self.dfs(child,V,adj,visited,path_visited)
        if isCycle:
          return True

    path_visited[node] = False 

    return False

  def isCyclic(self, N, adj):
    # visited = [False]*N
    # path_visited = [False]*N
    # for i in range(N):
    #   if not visited[i]:
    #     isCycle = self.dfs(i,N,adj,visited,path_visited) 
    #     if isCycle:
    #       return True
    # return False

    return self.bfs(N,adj)

if __name__ == "__main__":
  # N = 9
  # adj= [ [1], [2], [3], [4,5,6], [], [7 ],[7],[8],[5] ]
  N = 4
  adj= [[1,2], [2], [], [0,2]]
  print(Solution().isCyclic(N,adj))