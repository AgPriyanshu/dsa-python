# Given an undirected graph with V vertices labeled from 0 to V-1. The graph is represented using an adjacency list where adj[i] lists all nodes connected to node. Determine if the graph is bipartite or not.


# A graph is bipartite if the nodes can be partitioned into two independent sets A and B such that every edge in the graph connects a node in set A and a node in set B.

from collections import deque
class Solution:
  def bfs(self,i,V,adj,color):
    q = deque()
    q.append(i)
    color[i] = 'G'
    while q:
      node = q.popleft()
      for child in adj[node]:
        if color[child] == 'N':
          color[child] = 'G' if color[node] =='Y' else 'Y'
          q.append(child)
        
        elif color[node] == color[child]:
          return False
    return True

  def isBipartite(self, V, adj):
    color = ['N']*(V+1)
    ans = True
    for i in range(V):
      if color[i] == 'N':
        ans = self.bfs(i,V,adj,color)  
      if not ans:
        break
    return ans 

if __name__ == "__main__":
  # V=4
  # adj = [[1,3],[0,2],[1,3],[0,2]]
  V=4
  adj = [[1,2,3],[0,2],[0,1,3],[0,2]]
  print(Solution().isBipartite(V,adj))